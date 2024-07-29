import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.python.client import device_lib


def get_device_type():
    devices = device_lib.list_local_devices()
    return any(device.device_type == 'GPU' for device in devices)


def test_cnn_model():  
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10))
    return model


def get_model(optimizer, loss):
    model = test_cnn_model()  # load cnn model for test
    model.compile(optimizer=optimizer,
              loss=loss,
              metrics=['accuracy'])
    return model


def print_model_summary(model):
    model.summary()


def train(epochs, model, train_images, train_labels, test_images, test_labels):
    history = model.fit(train_images, train_labels, epochs=epochs,
                        validation_data=(test_images, test_labels))
    return history


def test(model):
    pass


def print_test_train_loss(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print(f'test_loss: {test_loss}')
    print(f'test_acc: {test_acc}')


def save_model_path(model, path):
    model.save(path)


if __name__ == "__main__":
    optimizer = 'adam'
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
    model = get_model(optimizer=optimizer, loss=loss)