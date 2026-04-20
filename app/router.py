import numpy as np
from app.embeddings import index, embed_text, persona_ids

def route_post_to_bots(post_content: str, threshold: float = 0.3):
    post_embedding = embed_text(post_content)

    D, I = index.search(np.array(post_embedding), k=3)

    matched = []

    for dist, idx in zip(D[0], I[0]):
        similarity = 1 / (1 + dist)

        print(f"[Router] Bot: {persona_ids[idx]}, Score: {similarity:.3f}")

        if similarity > threshold:
            matched.append(persona_ids[idx])

    return matched