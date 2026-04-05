from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma"

def view_database():
    # Load 
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=None)
    
    items = db.get(include=["metadatas", "documents", "embeddings"]) 
    
    for i, (metadata, document, embedding) in enumerate(zip(items['metadatas'], items['documents'], items['embeddings'])):
        print(f"Document {i+1}:")
        print(f"Metadata: {metadata}")
        print(f"Content: {document}")
        print(f"Embedding Vector (first 20 values): {embedding[:20]}...")  
        print(f"Full Embedding Vector Length: {len(embedding)}") 
        print("-" * 80)

if __name__ == "__main__":
    view_database()
