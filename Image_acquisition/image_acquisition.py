import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Image Acquisition
def load_image(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

# Step 2: Preprocessing
def preprocess_image(image):
    # Resize for uniform processing
    resized_image = cv2.resize(image, (256, 256))
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)
    return blurred_image

# Step 3: Feature Extraction
def extract_features(image):
    # Convert to grayscale for texture analysis
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Extract color features using KMeans
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_.astype(int)
    return gray_image, dominant_colors

# Step 4: Analysis Techniques
def analyze_texture(gray_image):
    # Calculate texture properties using GLCM (Haralick features)
    texture = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return texture

# Main Function
def main(file_path):
    # Load and preprocess image
    image = load_image(file_path)
    processed_image = preprocess_image(image)

    # Feature extraction
    gray_image, dominant_colors = extract_features(processed_image)
    texture_score = analyze_texture(gray_image)

    # Display results
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")

    plt.subplot(1, 2, 2)
    plt.imshow(processed_image)
    plt.title("Processed Image")

    print("Dominant Colors (RGB):", dominant_colors)
    print("Texture Score:", texture_score)
    plt.show()

# Run the code
if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Replace with your image path
    main(image_path)
