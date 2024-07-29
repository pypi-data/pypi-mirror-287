import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras import datasets


def get_dataset():
    """
    Using the cifar10 dataset for testing

    Dataset storage path: 
    (for Window) C:/Users/<username>/.keras
    """
    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
    data_preprocessing(train_images, test_images)
    return train_images, train_labels, test_images, test_labels


def data_preprocessing(train_images, test_images):
    # Normalize pixel values to be between 0 and 1
    train_images, test_images = train_images / 255.0, test_images / 255.0
    return train_images, test_images


def view_dataset(train_images, train_labels):
    """
    Using the cifar10 dataset for testing
    """

    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i])
        # The CIFAR labels happen to be arrays, 
        # which is why you need the extra index
        plt.xlabel(class_names[train_labels[i][0]])
    plt.show()

