import cv2
import numpy as np
from insightface.app import FaceAnalysis

# Initialize the face analysis app
app = FaceAnalysis(providers=['CPUExecutionProvider'])  # Use CPU since CUDA isn't available
app.prepare(ctx_id=-1, det_size=(640, 640))  # ctx_id=-1 for CPU

def extract_face_embeddings(image_path):
    """Extract face embeddings from an image"""
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not load image: {image_path}")
        return None, None
    
    # Get faces
    faces = app.get(img)
    
    if len(faces) == 0:
        print("No faces detected in the image")
        return None, None
    
    # Return first face's embedding and bounding box
    face = faces[0]
    embedding = face.embedding  # 512-dimensional vector
    bbox = face.bbox  # [x1, y1, x2, y2]
    
    return embedding, bbox

def compare_faces(embedding1, embedding2, threshold=0.6):
    """Compare two face embeddings"""
    if embedding1 is None or embedding2 is None:
        return False, 0.0
    
    # Calculate cosine similarity
    similarity = np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
    
    # Check if faces match
    is_match = similarity > threshold
    
    return is_match, similarity

def process_image_with_visualization(image_path, output_path=None):
    """Process image and draw face detections"""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not load image: {image_path}")
        return
    
    faces = app.get(img)
    
    # Draw rectangles around detected faces
    for i, face in enumerate(faces):
        bbox = face.bbox.astype(int)
        # Draw rectangle
        cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        
        # Add face info
        age = int(face.age) if hasattr(face, 'age') else 0
        gender = 'M' if face.sex == 1 else 'F' if hasattr(face, 'sex') else 'U'
        
        # Put text
        cv2.putText(img, f'Face {i+1}: {gender}, {age}', 
                   (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    # Save or display result
    if output_path:
        cv2.imwrite(output_path, img)
        print(f"Result saved to: {output_path}")
    else:
        cv2.imshow('Face Detection', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    # Test with a single image
    image_path = "images/img.jpeg"  # Replace with your image patham
    image2_path = "images/img2.jpeg"
    
    print("Testing face detection and embedding extraction...")
    
    # Extract embeddings
    embedding, bbox = extract_face_embeddings(image_path)
    embedding2, bbox2 = extract_face_embeddings(image2_path)

    
    if embedding is not None:
        print(f"✅ Face detected!")
        print(f"📊 Embedding shape: {embedding.shape}")
        print(f"📍 Bounding box: {bbox}")
        print(f"🔢 Embedding preview: {embedding[:5]}...")  # Show first 5 values
        
        # Process and visualize
        process_image_with_visualization(image_path, "output_with_faces.jpg")
        
    else:
        print("❌ No face detected in the image")

    
    match , sim = compare_faces(embedding, embedding2)
    print(embedding)

    
    