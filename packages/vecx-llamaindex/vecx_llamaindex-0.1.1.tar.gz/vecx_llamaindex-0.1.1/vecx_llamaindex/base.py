import logging
from collections import Counter
from functools import partial
from typing import Any, Callable, Dict, List, Optional, cast

from llama_index.core.bridge.pydantic import PrivateAttr
from llama_index.core.schema import BaseNode, MetadataMode, TextNode
from llama_index.core.vector_stores.types import (
    BasePydanticVectorStore,
    MetadataFilters,
    VectorStoreQuery,
    VectorStoreQueryMode,
    VectorStoreQueryResult,
)
from llama_index.core.vector_stores.utils import (
    DEFAULT_TEXT_KEY,
    legacy_metadata_dict_to_node,
    metadata_dict_to_node,
    node_to_metadata_dict,
)

from vecx import vectorx, index
from datetime import datetime

def _import_vectorx() -> Any:
    """
    Try to import vectorx module. If it's not already installed, instruct user how to install.
    """
    try:
        import vecx
    except ImportError as e:
        raise ImportError(
            "Could not import vectorx python package. "
            "Please install it with `pip install vecx`."
        ) from e
    return vecx

ID_KEY = "id"
VECTOR_KEY = "values"
SPARSE_VECTOR_KEY = "sparse_values"
METADATA_KEY = "metadata"

DEFAULT_BATCH_SIZE = 100

_logger = logging.getLogger(__name__)



def build_dict(input_batch: List[List[int]]) -> List[Dict[str, Any]]:
    """
    Build a list of sparse dictionaries from a batch of input_ids.

    NOTE: taken from https://www.pinecone.io/learn/hybrid-search-intro/.

    """
    # store a batch of sparse embeddings
    sparse_emb = []
    # iterate through input batch
    for token_ids in input_batch:
        indices = []
        values = []
        # convert the input_ids list to a dictionary of key to frequency values
        d = dict(Counter(token_ids))
        for idx in d:
            indices.append(idx)
            values.append(float(d[idx]))
        sparse_emb.append({"indices": indices, "values": values})
    # return sparse_emb list
    return sparse_emb


def generate_sparse_vectors(
    context_batch: List[str], tokenizer: Callable
) -> List[Dict[str, Any]]:
    """
    Generate sparse vectors from a batch of contexts.

    NOTE: taken from https://www.pinecone.io/learn/hybrid-search-intro/.

    """
    # create batch of input_ids
    inputs = tokenizer(context_batch)["input_ids"]
    # create sparse dictionaries
    return build_dict(inputs)


import_err_msg = (
    "`vectorx` package not found, please run `pip install vecx` to install it.`"
)


class VectorXVectorStore(BasePydanticVectorStore):

    stores_text: bool = True
    flat_metadata: bool = False

    api_key: Optional[str]
    key: Optional[str]
    index_name: Optional[str]
    environment: Optional[str]
    namespace: Optional[str]
    insert_kwargs: Optional[Dict]
    add_sparse_vector: bool
    text_key: str
    batch_size: int
    remove_text_from_metadata: bool

    _vectorx_index: Any = PrivateAttr()

    def __init__(
        self,
        vectorx_index: Optional[Any] = None,
        api_key: Optional[str] = None,
        key: Optional[str] = None,
        index_name: Optional[str] = None,
        environment: Optional[str] = None,
        namespace: Optional[str] = None,
        insert_kwargs: Optional[Dict] = None,
        add_sparse_vector: bool = False,
        text_key: str = DEFAULT_TEXT_KEY,
        batch_size: int = DEFAULT_BATCH_SIZE,
        remove_text_from_metadata: bool = False,
        **kwargs: Any,
    ) -> None:
        insert_kwargs = insert_kwargs or {}

        super().__init__(
            index_name=index_name,
            environment=environment,
            api_key=api_key,
            index_namespace=namespace,
            insert_kwargs=insert_kwargs,
            add_sparse_vector=add_sparse_vector,
            text_key=text_key,
            batch_size=batch_size,
            remove_text_from_metadata=remove_text_from_metadata,
        )

        # TODO: Make following inst ance check stronger -- check if vectorx_index is not vectorX.index, else raise
        #  ValueError
        if isinstance(vectorx_index, str):
            raise ValueError(
                "`vectorx_index` cannot be of type `str`; should be an instance of vectorX.index, "
            )
        
        print(vectorx_index)
        self._vectorx_index = vectorx_index or self._initialize_vectorx_index(api_key, key, index_name)

    @classmethod
    def _initialize_vectorx_index(
        cls,
        api_key: Optional[str],
        key: Optional[str],
        index_name: Optional[str],
    ) -> Any:

        vectorx = _import_vectorx()
        vx = vectorx.VectorX(api_key)
        return index.Index(name=index_name, key=key, vx=vx)


    @classmethod
    def from_params(
        cls,
        api_key: Optional[str] = None,
        key: Optional[str] = None,
        index_name: Optional[str] = None,
        batch_size: int = DEFAULT_BATCH_SIZE,
    ) -> "VectorXVectorStore":
        vectorx_index = cls._initialize_vectorx_index(api_key, key, index_name)

        return cls(
            vectorx_index=vectorx_index,
            api_key=api_key,
            index_name=index_name,
            batch_size=batch_size,
        )

    @classmethod
    def class_name(cls) -> str:
        return "VectorXVectorStore"

    def add(
        self,
        nodes: List[BaseNode],
        **add_kwargs: Any,
    ) -> List[str]:
        """
        Add nodes to index.

        Args:
            nodes: List[BaseNode]: list of nodes with embeddings

        """
        ids = []
        entries = []
        for node in nodes:
            node_id = node.node_id

            metadata = node_to_metadata_dict(node)
            entry = {
                "id": node_id,
                "filter": {"file_name": metadata["file_name"] ,"doc_id": metadata['doc_id']},
                "meta": metadata,
                "vector": node.get_embedding(),
            }

            ids.append(node_id)
            entries.append(entry)
        self._vectorx_index.upsert(entries)
        return ids

    def delete(self, ref_doc_id: str, **delete_kwargs: Any) -> None:
        """
        Delete nodes using with ref_doc_id.
        Args:
            ref_doc_id (str): The id of the vector to delete.

        """
        self._vectorx_index.delete_with_filter(filter={"doc_id": ref_doc_id})

    @property
    def client(self) -> Any:
        """Return vectorX index client."""
        return self._vectorx_index

    def query(self, query: VectorStoreQuery, **kwargs: Any) -> VectorStoreQueryResult:
        """
        Query index for top k most similar nodes.

        Args:
            query_embedding (List[float]): query embedding
            similarity_top_k (int): top k most similar nodes

        """

        # vectorx requires a query embedding, so default to 0s if not provided
        if query.query_embedding is not None:
            dimension = len(query.query_embedding)
        else:
            dimension = self._vectorx_index.describe()["dimensions"]
        query_embedding = [0.0] * dimension

        if query.mode in (VectorStoreQueryMode.DEFAULT, VectorStoreQueryMode.HYBRID):
            query_embedding = cast(List[float], query.query_embedding)
            if query.alpha is not None:
                query_embedding = [v * query.alpha for v in query_embedding]

        response = self._vectorx_index.query(
            vector=query_embedding,
            top_k=query.similarity_top_k,
            log=False,
            include_vectors=False,
        )

        top_k_nodes = []
        top_k_ids = []
        top_k_scores = []
        for res in response:
            node = metadata_dict_to_node(res['meta'])
            if 'vector' in res:
                node.embedding = res['vector']
            else:
                node.embedding = None
            top_k_ids.append(res['id'])
            top_k_nodes.append(node)
            top_k_scores.append(res['similarity'])

        return VectorStoreQueryResult(
            nodes=top_k_nodes, similarities=top_k_scores, ids=top_k_ids
        )
