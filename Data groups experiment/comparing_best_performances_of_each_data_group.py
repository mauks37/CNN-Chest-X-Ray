# -*- coding: utf-8 -*-
"""Comparing best performances of each data group.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FkdfbUInaEaQuLi2biLmg0WtS2Nk_RbL
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import tensorflow as tf
import pandas as pd
import random
import cv2
from sklearn.metrics import classification_report, confusion_matrix

gpu_info = !nvidia-smi
gpu_info = '\n'.join(gpu_info)
if gpu_info.find('failed') >= 0:
  print('Select the Runtime > "Change runtime type" menu to enable a GPU accelerator, ')
  print('and then re-execute this cell.')
else:
  print(gpu_info)

from google.colab import drive
drive.mount('/content/drive')

image_shape = (224,224,3)
batch_size = 32

from tensorflow.keras.preprocessing.image import ImageDataGenerator

image_gen = ImageDataGenerator()

from keras.models import load_model

def int_predict (pred_probabilities):
  predictions = np.zeros((pred_probabilities.shape[0],1),dtype=int)
  i = 0
  while i < pred_probabilities.shape[0]:
    predictions[i,:] = [np.argmax(pred_probabilities[i])]
    i = i + 1

  return predictions

"""**All without augmentation**

Loading best model
"""

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds mix/VGG19_fine-tuning_avg_4_classes_mix_data_part2345.h5')

"""TEST"""

test_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/RXT teste mix_data/'

valid_image_gen = image_gen.flow_from_directory(test_dir,
                                               #target_size=image_shape[:2],
                                               color_mode='rgb',
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)

ac1v = model.evaluate(valid_image_gen)
ac1v

pred_probabilities = model.predict(valid_image_gen)

classes1v = valid_image_gen.classes
#classes1v

pred1v = predictions = int_predict(pred_probabilities)
#pred1v

valid_image_gen.class_indices

confusion_matrix(valid_image_gen.classes,predictions)

print(classification_report(valid_image_gen.classes,predictions))

from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from itertools import cycle

y_score = pred_probabilities
num_classes = valid_image_gen.num_classes

# Obtenha as etiquetas verdadeiras de todas as imagens no gerador
y_test = valid_image_gen.classes
y_test = label_binarize(y_test, classes=range(num_classes))

# Calcule as métricas ROC e AUC para cada classe
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(num_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plote a curva ROC para cada classe
colors = cycle(['aqua', 'darkorange', 'cornflowerblue', 'green'])
for i, color in zip(range(num_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic for multi-class')
plt.legend(loc="lower right")
plt.show()

# Agora, vamos dar zoom em na parte superior esquerda do gráfico.
plt.figure()
for i, color in zip(range(num_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 0.2])  # Ajusta o limite do eixo X para focar no início do gráfico
plt.ylim([0.8, 1.05])  # Ajusta o limite do eixo Y para focar na parte superior do gráfico
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Zoom na parte superior da Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()

"""**All with augmentation**

Loading best model
"""

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds mix aumentado/VGG19_fine-tuning_RandAugm_avg_4_classes_mix_data_part2345.h5')

"""TEST"""

test_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/RXT teste mix_data/'

valid_image_gen = image_gen.flow_from_directory(test_dir,
                                               #target_size=image_shape[:2],
                                               color_mode='rgb',
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)

ac1v = model.evaluate(valid_image_gen)
ac1v

pred_probabilities = model.predict(valid_image_gen)

classes1v = valid_image_gen.classes
#classes1v

pred1v = predictions = int_predict(pred_probabilities)
#pred1v

valid_image_gen.class_indices

confusion_matrix(valid_image_gen.classes,predictions)

print(classification_report(valid_image_gen.classes,predictions))

from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from itertools import cycle

y_score = pred_probabilities
num_classes = valid_image_gen.num_classes

# Obtenha as etiquetas verdadeiras de todas as imagens no gerador
y_test = valid_image_gen.classes
y_test = label_binarize(y_test, classes=range(num_classes))

# Calcule as métricas ROC e AUC para cada classe
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(num_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plote a curva ROC para cada classe
colors = cycle(['aqua', 'darkorange', 'cornflowerblue', 'green'])
for i, color in zip(range(num_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic for multi-class')
plt.legend(loc="lower right")
plt.show()

# Agora, vamos dar zoom em na parte superior esquerda do gráfico.
plt.figure()
for i, color in zip(range(num_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 0.2])  # Ajusta o limite do eixo X para focar no início do gráfico
plt.ylim([0.8, 1.05])  # Ajusta o limite do eixo Y para focar na parte superior do gráfico
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Zoom na parte superior da Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()

"""**HCFMRP with augmentation**

Loading best model
"""

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds nosso aumentado/VGG19_fine-tuning_RandAugm_avg_4_classes_nosso_data_part1345.h5')

"""TEST"""

test_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/RXT teste nosso_data/'

valid_image_gen = image_gen.flow_from_directory(test_dir,
                                               #target_size=image_shape[:2],
                                               color_mode='rgb',
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)

ac1v = model.evaluate(valid_image_gen)
ac1v

pred_probabilities = model.predict(valid_image_gen)

classes1v = valid_image_gen.classes
#classes1v

pred1v = predictions = int_predict(pred_probabilities)
#pred1v

valid_image_gen.class_indices

confusion_matrix(valid_image_gen.classes,predictions)

print(classification_report(valid_image_gen.classes,predictions))

from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from itertools import cycle

y_score = pred_probabilities
num_classes = valid_image_gen.num_classes

# Obtenha as etiquetas verdadeiras de todas as imagens no gerador
y_test = valid_image_gen.classes
y_test = label_binarize(y_test, classes=range(num_classes))

# Calcule as métricas ROC e AUC para cada classe
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(num_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Plote a curva ROC para cada classe
colors = cycle(['aqua', 'darkorange', 'cornflowerblue', 'green'])
for i, color in zip(range(num_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic for multi-class')
plt.legend(loc="lower right")
plt.show()

# Agora, vamos dar zoom em na parte superior esquerda do gráfico.
plt.figure()
for i, color in zip(range(num_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 0.2])  # Ajusta o limite do eixo X para focar no início do gráfico
plt.ylim([0.8, 1.05])  # Ajusta o limite do eixo Y para focar na parte superior do gráfico
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Zoom na parte superior da Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()