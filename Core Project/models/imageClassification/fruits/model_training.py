import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam 

def train_model(model, train_generator, validation_generator):
    """
    Train the CNN model using fine-tuning.
    """
    early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

    # Fine-tuning: Unfreeze the base model after initial training
    model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // train_generator.batch_size,
        epochs=20,  # Initial training without fine-tuning
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // validation_generator.batch_size,
        callbacks=[early_stopping]
    )

    # Unfreeze all layers of the base model to fine-tune
    model.trainable = True
    for layer in model.layers[:-3]:  # Freeze the last few layers to fine-tune only the later layers
        layer.trainable = False

    # Re-compile the model after unfreezing
    model.compile(optimizer=Adam(learning_rate=1e-5), loss='categorical_crossentropy', metrics=['accuracy'])

    # Fine-tune the model with a smaller learning rate
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // train_generator.batch_size,
        epochs=30,  # Fine-tuning for more epochs
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // validation_generator.batch_size,
        callbacks=[early_stopping]
    )

    # Plot the accuracy and loss graphs
    plot_history(history)
    return history


def plot_history(history):
    """
    Plot accuracy and loss graphs.
    """
    # Plot accuracy
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    # Plot loss
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
