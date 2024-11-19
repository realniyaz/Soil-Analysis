from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Example: Augmenting a single image
image = load_image("path_to_image.jpg")  # Preprocess the image
image = np.expand_dims(image, axis=0)
augmented_images = datagen.flow(image, batch_size=1)

# Save augmented images
for i, batch in enumerate(augmented_images):
    new_image = batch[0]
    plt.imsave(f"augmented_image_{i}.jpg", new_image)
    if i > 10:  # Limit to 10 augmented samples
        break
