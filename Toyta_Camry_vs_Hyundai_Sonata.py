# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G5h6HP8O8ZT--Zhbl8Dw9_kd4q97LHKy
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

model = keras.models.load_model('keras_model.h5')

from google.colab import files
from PIL import Image
import numpy as np

uploaded = files.upload()

img = Image.open('images.jpeg').convert('RGB')
img = img.resize((224, 224))
img_array = np.array(img) / 255.0
img_array = img_array.reshape(1, 224, 224, 3)

prediction = model.predict(img_array)
print("Prediction values:", prediction)

classes = ['Toyota Camry', 'Hyundai Sonata']
predicted_class = classes[np.argmax(prediction)]
print("Predicted class:", predicted_class)

plt.imshow(img)
plt.title(f'Prediction: {predicted_class}')
plt.axis('off')
plt.show()