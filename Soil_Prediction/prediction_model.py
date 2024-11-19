from tensorflow.keras.models import load_model
import numpy as np

# Load the model
model = load_model("soil_analysis_model.h5")

# Predict soil type for a new image
def predict_soil_type(image_path):
    image = load_image(image_path)
    image = preprocess_image(image)
    image = cv2.resize(image, (128, 128)) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    soil_classes = ['Sandy', 'Clay', 'Loamy']
    return soil_classes[np.argmax(prediction)]

# Test prediction
print(predict_soil_type("path_to_new_soil_image.jpg"))
