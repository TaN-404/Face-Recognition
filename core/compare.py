import numpy as np

def compare_faces(embedding, embedding_list, threshold=0.6):
    """Compare two face embeddings"""
    if embedding is None or embedding_list is None:
        return False, 0.0
    

    # print(embedding_list)
    
    # Calculate cosine similarity
    for avg in range(len(embedding_list)):
        similarity = np.dot(embedding, embedding_list[avg]) / (np.linalg.norm(embedding) * np.linalg.norm(embedding_list[avg]))
        is_match = similarity > threshold
        if is_match:
            average_e = embedding_list[avg]
            break
    
    
    return is_match, similarity, average_e
