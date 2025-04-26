from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam

def build_model(input_shape=(224, 224, 3), num_classes=10):
    """
    Build and compile the model using MobileNetV2 with transfer learning,
    and additional custom layers for better accuracy.
    """
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=input_shape)

    # Freeze the base model to retain the pre-trained features
    base_model.trainable = False

    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.BatchNormalization(),                      # ➔ Add BatchNormalization for stability
        layers.Dense(512, activation='relu'),              # ➔ Bigger Dense layer
        layers.Dropout(0.5),                               # ➔ Dropout for regularization
        layers.BatchNormalization(),                      # ➔ Again BatchNorm
        layers.Dense(256, activation='relu'),              # ➔ Another Dense layer
        layers.Dropout(0.4),                               # ➔ Dropout to prevent overfitting
        layers.Dense(128, activation='relu'),              # ➔ One more Dense layer
        layers.Dropout(0.3),                               # ➔ Smaller Dropout
        layers.Dense(num_classes, activation='softmax')   # ➔ Final Output Layer
    ])

    # Compile the model with a lower learning rate
    optimizer = Adam(learning_rate=0.0001)

    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    model.summary()
    return model
