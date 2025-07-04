import numpy as np

# def compare_faces(embedding, embedding_list, threshold=0.6):
#     """Compare two face embeddings"""
#     if embedding is None or embedding_list is None:
#         print("no face")
#         return False, 0.0, embedding
    

#     for avg in range(len(embedding_list)):
#         similarity = np.dot(embedding, embedding_list[avg]) / (np.linalg.norm(embedding) * np.linalg.norm(embedding_list[avg]))
#         is_match = similarity > threshold
#         if is_match:
#             average_e = embedding_list[avg]
#             return is_match, similarity, average_e
    
#         else:
#             print("no match")
#             return False, 0.0, embedding



import numpy as np

def compare_faces(embedding, embedding_list, threshold=0.6):
    """
    Compare a face embedding against a list of embeddings
    
    Args:
        embedding: numpy array - face embedding to compare
        embedding_list: list of numpy arrays - stored embeddings to compare against
        threshold: float - similarity threshold for a match
        
    Returns:
        tuple: (is_match, highest_similarity, best_match_embedding)
    """
    # Input validation
    if embedding is None or embedding_list is None or len(embedding_list) == 0:
        print("Invalid input: embedding or embedding_list is empty")
        return False, 0.0, None
    
    if not isinstance(embedding, np.ndarray) or any(not isinstance(e, np.ndarray) for e in embedding_list):
        print("Inputs must be numpy arrays")
        return False, 0.0, None
    
    # Initialize variables to track best match
    highest_similarity = -1
    best_match = None
    best_match_idx = -1
    
    # Compare against all embeddings
    for idx, stored_embedding in enumerate(embedding_list):
        try:
            # Flatten arrays to ensure 1D
            emb1 = embedding.flatten()
            emb2 = stored_embedding.flatten()
            
            # Check for equal length
            if len(emb1) != len(emb2):
                print(f"Dimension mismatch: {len(emb1)} vs {len(emb2)}")
                continue
                
            # Calculate cosine similarity
            dot_product = np.dot(emb1, emb2)
            norm_product = np.linalg.norm(emb1) * np.linalg.norm(emb2)
            
            # Avoid division by zero
            if norm_product < 1e-10:  # Small epsilon
                similarity = 0.0
            else:
                similarity = dot_product / norm_product
            
            # Track best match
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = stored_embedding
                best_match_idx = idx
                
        except Exception as e:
            print(f"Error comparing embeddings: {str(e)}")
            continue
    
    # Determine if best match meets threshold
    is_match = highest_similarity > threshold
    if is_match:
        print(f"Match found with similarity: {highest_similarity:.4f}")
    else:
        print(f"No match found. Highest similarity: {highest_similarity:.4f}")
    
    return is_match, highest_similarity, best_match