# Function to estimate moisture level based on brightness
def estimate_moisture(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    brightness = hsv_image[:, :, 2].mean()  # Mean of the 'V' channel
    moisture_level = "High" if brightness < 50 else "Medium" if brightness < 100 else "Low"
    return moisture_level

# Adding contours for particle size distribution
def analyze_particle_size(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours), contours

# Update Main Function
def main(file_path):
    image = load_image(file_path)
    processed_image = preprocess_image(image)

    # Extract features
    gray_image, dominant_colors = extract_features(processed_image)
    texture_score = analyze_texture(gray_image)
    moisture_level = estimate_moisture(processed_image)
    particle_count, contours = analyze_particle_size(processed_image)

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
    print("Moisture Level:", moisture_level)
    print("Particle Count:", particle_count)

    # Visualize contours
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    plt.figure()
    plt.imshow(contour_image)
    plt.title("Particle Contours")
    plt.show()

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"
    main(image_path)
