from insightface.app import FaceAnalysis
import cv2
import numpy as np

output_path = '/temp'
imgp = 'images/img.jpeg'
img = cv2.imread(imgp)
app = FaceAnalysis(providers=['CPUExecutionProvider'])  # Use CPU since CUDA isn't available
app.prepare(ctx_id=-1, det_size=(640, 640))  # ctx_id=-1 for CPU



def embed_image(image):
    if image is None:
        print("image corrupted")
        return None
    
    faces = app.get(image)
    if len(faces) == 0:
        print("No faces detected in the image")
        return None
    
    face = faces[0]
    embedding = face.embedding  
    # bbox = face.bbox 
    # cv2.imwrite(output_path, image)
    return embedding


embed_image(img)