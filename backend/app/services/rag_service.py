import google.generativeai as genai
import os
from backend.app.services.chroma_service import collection

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def retrieve_context(question):
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=question
    )
    query_embedding = result["embedding"]

    result = genai.embed_content(
    model="models/embedding-001",  # ← change this line
    content=question
    )

    documents = result["documents"][0]
    metadatas = result["metadatas"][0]

    context = "\n".join(documents)

    sources = []
    for metadata in metadatas:
        if metadata is None:
            continue
        doc_id = metadata.get("doc_id")
        if doc_id and doc_id not in sources:
            sources.append(doc_id)

    return {"context": context, "sources": sources}