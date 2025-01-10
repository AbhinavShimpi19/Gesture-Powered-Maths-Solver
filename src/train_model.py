import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.preprocessing.image import ImageDataGenerator

# Set up your model architecture
def create_model():
    model = Sequential()
    model.add(Flatten(input_shape=(28, 28, 1)))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(15, activation='softmax'))  # Assuming 15 classes (0-9, +, -, *, /, π)
    return model

# Compile and train the model
def train_model():
    model = create_model()
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Example data generator (modify as necessary)
    datagen = ImageDataGenerator(rescale=1./255)
    train_data = datagen.flow_from_directory(
        'path_to_training_data',  # Replace with your training data directory
        target_size=(28, 28),
        color_mode='grayscale',
        class_mode='categorical',
        batch_size=32
    )

    model.fit(train_data, epochs=10)  # Adjust epochs as needed
    model.save('models/socratic.h5')

if __name__ == '__main__':
    train_model()
