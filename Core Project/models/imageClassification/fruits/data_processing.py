from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_data_generators(base_dir, target_size=(224, 224), batch_size=32, validation_split=0.2):
    """
    Create data generators for training and validation data with augmentation.
    """
    datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,  # Random rotations
        width_shift_range=0.2,  # Horizontal shifts
        height_shift_range=0.2,  # Vertical shifts
        shear_range=0.2,  # Shearing transformations
        zoom_range=0.2,  # Zoom transformations
        horizontal_flip=True,  # Horizontal flips
        fill_mode='nearest',  # Pixel fill strategy for transformations
        brightness_range=[0.8, 1.2],  # Brightness range
        validation_split=0.2,  # Added for splitting data (adjust as needed)
        channel_shift_range=20.0,  # Randomly shifts color channels
        contrast_range=[0.8, 1.2],  # Adjusts contrast randomly
        height_shift_range=0.2,  # Randomly shift images vertically
        zoom_range=[0.9, 1.2],  # Adds zoom variations from 90% to 120%
        random_crop=True  # Cropping to get varied image sizes (if supported by your version)
    )


    # Training generator
    train_generator = datagen.flow_from_directory(
        base_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    # Validation generator
    validation_generator = datagen.flow_from_directory(
        base_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    return train_generator, validation_generator
