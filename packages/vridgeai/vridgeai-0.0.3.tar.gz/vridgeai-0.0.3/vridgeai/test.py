import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import numpy as np 
import tensorflow as tf 
from tensorflow.keras import layers, models

from tensorflow.python.client import device_lib

from model_utils import * 
from dataset_utils import *

optimizer = 'adam'
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model = get_model(optimizer=optimizer, loss=loss)
train_images, train_labels, test_images, test_labels = get_dataset()

epochs = 20
history = train(epochs, model, train_images, train_labels, test_images, test_labels) # print history 
 
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(test_acc)

save_model_path(model, 'hello.keras')