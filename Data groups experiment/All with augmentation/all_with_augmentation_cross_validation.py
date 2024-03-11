# -*- coding: utf-8 -*-
"""All with augmentation Cross-validation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bGw_8RW4wLJ2oDPGTGgb0t1zhLkvfBgI
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

test_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/RXT teste mix_data/'

"""#**PART 1**"""

data_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 2-3-4-5/'
valid_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/1/'

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds mix aumentado/VGG19_fine-tuning_RandAugm_avg_4_classes_mix_data_part2345.h5')

"""VALIDATION"""

valid_image_gen = image_gen.flow_from_directory(valid_dir,
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

"""#**PART 2**"""

data_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-3-4-5/'
valid_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/2/'

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds mix aumentado/VGG19_fine-tuning_RandAugm_avg_4_classes_mix_data_part1345.h5')

"""VALIDATION"""

valid_image_gen = image_gen.flow_from_directory(valid_dir,
                                               #target_size=image_shape[:2],
                                               color_mode='rgb',
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)

ac2v = model.evaluate(valid_image_gen)
ac2v

pred_probabilities = model.predict(valid_image_gen)

classes2v = valid_image_gen.classes
#classes1v

pred2v = predictions = int_predict(pred_probabilities)
#pred1v

valid_image_gen.class_indices

confusion_matrix(valid_image_gen.classes,predictions)

print(classification_report(valid_image_gen.classes,predictions))

"""#**PART 3**"""

data_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-2-4-5/'
valid_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/3/'

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds mix aumentado/VGG19_fine-tuning_RandAugm_avg_4_classes_mix_data_part1245.h5')

"""VALIDAÇÃO"""

valid_image_gen = image_gen.flow_from_directory(valid_dir,
                                               #target_size=image_shape[:2],
                                               color_mode='rgb',
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)

ac3v = model.evaluate(valid_image_gen)
ac3v

pred_probabilities = model.predict(valid_image_gen)

classes3v = valid_image_gen.classes
#classes1v

pred3v = predictions = int_predict(pred_probabilities)
#pred1v

valid_image_gen.class_indices

confusion_matrix(valid_image_gen.classes,predictions)

print(classification_report(valid_image_gen.classes,predictions))

"""#**PART 4**"""

data_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-2-3-5/'
valid_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/4/'

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds mix aumentado/VGG19_fine-tuning_RandAugm_avg_4_classes_mix_data_part1235.h5')

"""VALIDAÇÃO"""

valid_image_gen = image_gen.flow_from_directory(valid_dir,
                                               #target_size=image_shape[:2],
                                               color_mode='rgb',
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)

ac4v = model.evaluate(valid_image_gen)
ac4v

pred_probabilities = model.predict(valid_image_gen)

classes4v = valid_image_gen.classes
#classes1v

pred4v = predictions = int_predict(pred_probabilities)
#pred1v

valid_image_gen.class_indices

confusion_matrix(valid_image_gen.classes,predictions)

print(classification_report(valid_image_gen.classes,predictions))

"""#**PART 5**"""

data_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-2-3-4/'
valid_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/5/'

model = tf.keras.models.load_model('/content/drive/My Drive/Colab Notebooks/Mestrado final/Novos treinamentos/KFolds mix aumentado/VGG19_fine-tuning_RandAugm_avg_4_classes_mix_data_part1234.h5')

valid_image_gen = image_gen.flow_from_directory(valid_dir,
                                               #target_size=image_shape[:2],
                                               color_mode='rgb',
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               shuffle=False)

ac5v = model.evaluate(valid_image_gen)
ac5v

pred_probabilities = model.predict(valid_image_gen)

classes5v = valid_image_gen.classes
#classes1v

pred5v = predictions = int_predict(pred_probabilities)
#pred1v

valid_image_gen.class_indices

confusion_matrix(valid_image_gen.classes,predictions)

print(classification_report(valid_image_gen.classes,predictions))

"""#**Calculations**"""

acv_media = np.mean([ac1v[1],ac2v[1],ac3v[1],ac4v[1],ac5v[1]])
acv_media

todas_classesv = np.concatenate((classes1v,classes2v,classes3v,classes4v,classes5v),axis=0)

todas_predv = np.concatenate((pred1v,pred2v,pred3v,pred4v,pred5v),axis=0)

from sklearn.metrics import classification_report, confusion_matrix

"""*   0: covid
*   1: dip
*   2: normais
*   3: tuberculose


"""

confusion_matrix(todas_classesv,todas_predv)

print(classification_report(todas_classesv,todas_predv))

"""*   0: covid
*   1: dip
*   2: normais
*   3: tuberculose


"""