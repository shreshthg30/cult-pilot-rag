import logging
from logging_config import setup_logging
from langchain_nomic.embeddings import NomicEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import OllamaEmbeddings
import dotenv
from langchain_community.vectorstores import Chroma
# from langchain_community.vectorstores import FAISS
# from langchain_pinecone import PineconeVectorStore
from src.retriever.config import ANSWERS_CSV_PATH, ANSWERS_CHROMA_PATH, EMBEDDINGS_MODEL, COLLECTION_NAME, RETRIEVER_K, INDEX_NAME

setup_logging()
dotenv.load_dotenv()


class CreateRetriever:
    def __init__(self):
        try:
            self.loader = CSVLoader(file_path=ANSWERS_CSV_PATH, encoding="utf-8")
            self.answers = self.loader.load()
            logging.info("CSV loaded successfully")

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            texts = text_splitter.split_documents(self.answers)

            embeddings = NomicEmbeddings(model="nomic-embed-text-v1.5", dimensionality=256)

            # embeddings = OllamaEmbeddings(model="nomic-embed-text")

            
            # self.answers_vector_db = PineconeVectorStore.from_documents(
            #     texts, embeddings, index_name=INDEX_NAME
            # )

            self.answers_vector_db = Chroma.from_documents(
                documents=texts,
                collection_name=COLLECTION_NAME,
                embedding=embeddings,
                persist_directory=ANSWERS_CHROMA_PATH
            )

            # self.answers_vector_db = FAISS.from_documents(texts, embeddings)

         
        except Exception as e:
            logging.error(f"Error initializing CreateRetriever: {e}")
            raise

    def get_retriever(self):
        try:
            return self.answers_vector_db.as_retriever(search_type = "mmr", search_kwargs = {"scope_threshold":0.8, "k":RETRIEVER_K})
        except Exception as e:
            logging.error(f"Error getting retriever: {e}")
            raise

