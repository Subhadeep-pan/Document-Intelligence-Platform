import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def create_embeddings(chunks):
    embeddings = []
    for chunk in chunks:
        result = genai.embed_content(
            model="models/embedding-001",  # ← change this line
            content=chunk
        )
        embeddings.append(result["embedding"])
    return embeddings