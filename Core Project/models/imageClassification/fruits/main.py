from data_processing import create_data_generators
from model_building import build_model
from model_training import train_model
import os

def main():
    base_dir = 'fruits_data/test'  # Path to your fruit image data folder
    train_generator, validation_generator = create_data_generators(base_dir)

    # Automatically get the number of fruit classes from the directories
    fruit_classes = sorted(os.listdir(base_dir))
    num_classes = len(fruit_classes)
    print(f"Number of classes: {num_classes}")

    # Create label.txt by writing the class names
    with open('label.txt', 'w') as f:
        for fruit in fruit_classes:
            f.write(f"{fruit}\n")

    print(f"label.txt created with {num_classes} classes.")

    # Build and train the model
    model = build_model(input_shape=(224, 224, 3), num_classes=num_classes)
    history = train_model(model, train_generator, validation_generator)

    # Save the trained model
    model.save('fruit_classifier_model.h5')
    print("Model saved as 'fruit_classifier_model.h5'")

if __name__ == "__main__":
    main()
