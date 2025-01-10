import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Function to create the model
def create_model():
    model = Sequential()
    model.add(Flatten(input_shape=(28, 28, 1)))  # Adjust input shape as necessary
    model.add(Dense(128, activation='relu'))
    model.add(Dense(15, activation='softmax'))  # Assuming 15 classes (0-9, +, -, *, /, π)
    return model

# Function to train the model
def train_model():
    model = create_model()
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Set up data generator
    datagen = ImageDataGenerator(rescale=1./255)

    # Assuming your training data is organized in 'path_to_training_data'
    train_data = datagen.flow_from_directory(
        'path_to_training_data',  # Replace with your training data directory
        target_size=(28, 28),
        color_mode='grayscale',
        class_mode='categorical',
        batch_size=32,
        shuffle=True  # Shuffle the data
    )

    model.fit(train_data, epochs=10)  # Adjust epochs as needed

    # Ensure models/ directory exists
    if not os.path.exists('models'):
        os.makedirs('models')

    model.save('models/socratic.h5')

if __name__ == '__main__':
    train_model()
