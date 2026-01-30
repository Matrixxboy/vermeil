import os
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
import warnings
import uuid

# Suppress hypothetical warnings
warnings.filterwarnings("ignore")

class RAGSystem:
    def __init__(self, db_path="chroma_db", collection_name="knowledge_base"):
        """
        Initializes the RAG system using ChromaDB.
        """
        self.client = chromadb.PersistentClient(path=db_path)
        
        # Use a good generic embedding model
        # 'all-MiniLM-L6-v2' is fast and efficient
        self.embedding_model = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_model
        )
        print(f"🧠 RAG System Initialized. Collection: {collection_name}")

    def ingest(self, directory_path):
        """
        Reads all .txt and .md files from the directory and adds them to the vector DB.
        """
        if not os.path.exists(directory_path):
            print(f"⚠️ Knowledge base directory not found: {directory_path}")
            return

        documents = []
        metadatas = []
        ids = []

        print(f"📥 Scanning {directory_path} for documents...")
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt") or filename.endswith(".md"):
                file_path = os.path.join(directory_path, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if content.strip():
                            # Simple chunking: split by paragraphs or just ingest file
                            # For better results, use a recursive character text splitter.
                            # Here, we treat the file as one document for simplicity, 
                            # or split by double newlines.
                            chunks = content.split("\n\n") 
                            for i, chunk in enumerate(chunks):
                                if len(chunk.strip()) > 20: # Skip tiny chunks
                                    documents.append(chunk)
                                    metadatas.append({"source": filename, "chunk_id": i})
                                    ids.append(f"{filename}_{i}_{str(uuid.uuid4())[:8]}")
                except Exception as e:
                    print(f"❌ Error reading {filename}: {e}")

        if documents:
            print(f"💾 Ingesting {len(documents)} chunks into memory...")
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print("✅ Ingestion complete.")
        else:
            print("ℹ️ No new documents found to ingest.")

    def query(self, query_text, n_results=3):
        """
        Queries the database for relevant context.
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        
        # Flatten results
        retrieved_docs = results['documents'][0]
        sources = results['metadatas'][0]
        
        if not retrieved_docs:
            return ""

        context_string = ""
        for i, doc in enumerate(retrieved_docs):
            source = sources[i]['source']
            context_string += f"--- Source: {source} ---\n{doc}\n\n"
            
        return context_string

# Verification block
if __name__ == "__main__":
    rag = RAGSystem()
    # Test ingestion
    rag.ingest("core_project/knowledge_base")
    # Test query
    res = rag.query("Who is user?")
    print("Query Result:", res)
