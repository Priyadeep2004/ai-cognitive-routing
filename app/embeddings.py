from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from app.personas import personas

model = SentenceTransformer('all-MiniLM-L6-v2')

persona_ids = list(personas.keys())
persona_texts = list(personas.values())

persona_embeddings = model.encode(persona_texts)

index = faiss.IndexFlatL2(persona_embeddings.shape[1])
index.add(np.array(persona_embeddings))


def embed_text(text: str):
    return model.encode([text])