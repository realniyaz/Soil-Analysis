from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import cv2

# Load the pre-trained model
model = load_model("soil_analysis_model.h5")
soil_classes = ['Sandy', 'Clay', 'Loamy']

# Initialize Flask App
app = Flask(__name__)

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((128, 128))
    image_array = np.array(image) / 255.0  # Normalize
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/analyze', methods=['POST'])
def analyze_soil():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file:
        # Save and preprocess image
        image_path = f"uploaded_images/{file.filename}"
        file.save(image_path)
        image_array = preprocess_image(image_path)

        # Predict soil type
        prediction = model.predict(image_array)
        soil_type = soil_classes[np.argmax(prediction)]

        return jsonify({'soil_type': soil_type})

    return jsonify({'error': 'Invalid file format'}), 400

if __name__ == "__main__":
    app.run(debug=True)
``
