from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import PineconeVectorStore
import pinecone
import os

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="us-west1-gcp")
index_name = "research-index"
vector_store = PineconeVectorStore(index_name=index_name)

# Connect LlamaIndex to Pinecone
index = VectorStoreIndex.from_documents([], vector_store=vector_store)

