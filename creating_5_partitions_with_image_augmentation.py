# -*- coding: utf-8 -*-
"""Creating 5 partitions with image augmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AhSHwEgN1T2fsdEf1IS2Lq5ZZg0v72Zn
"""

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from matplotlib.image import imread
import tensorflow as tf
import random
import cv2
from tensorflow import keras

!pip install keras-cv

import keras_cv

from google.colab import drive
drive.mount('/content/drive')

origem_data_dir = '/content/drive/My Drive/Colab Notebooks/Mestrado final/RXT 224x224 mix_data/'
trein_1234 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-2-3-4/'
trein_1235 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-2-3-5/'
trein_1245 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-2-4-5/'
trein_1345 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 1-3-4-5/'
trein_2345 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/trein 2-3-4-5/'
part_1 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/1/'
part_2 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/2/'
part_3 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/3/'
part_4 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/4/'
part_5 = '/content/drive/My Drive/Colab Notebooks/Mestrado final/KFolds mix_data aumentado/5/'

tf.io.gfile.listdir(origem_data_dir)

print('Tamanho normais :' + str(len(tf.io.gfile.listdir(origem_data_dir + 'normais'))))
print('Tamanho dip :' + str(len(tf.io.gfile.listdir(origem_data_dir + 'dip'))))
print('Tamanho covid :' + str(len(tf.io.gfile.listdir(origem_data_dir + 'covid'))))
print('Tamanho tuberculose :' + str(len(tf.io.gfile.listdir(origem_data_dir + 'tuberculose'))))

print('Tamanho trein_1234 :' + str(len(tf.io.gfile.listdir(trein_1234 + 'tuberculose'))))
print('Tamanho trein_1235 :' + str(len(tf.io.gfile.listdir(trein_1235 + 'tuberculose'))))
print('Tamanho trein_1245 :' + str(len(tf.io.gfile.listdir(trein_1245 + 'tuberculose'))))
print('Tamanho trein_1345 :' + str(len(tf.io.gfile.listdir(trein_1345 + 'tuberculose'))))
print('Tamanho trein_2345 :' + str(len(tf.io.gfile.listdir(trein_2345 + 'tuberculose'))))

def distribuir_imagens_particoes (nome_classe, num_part):

  #pegando nomes imagens de uma classe
  images_names = tf.io.gfile.listdir(origem_data_dir + nome_classe)
  random.shuffle(images_names)

  teste_size = 0
  total_part_size = (len(images_names)-teste_size)
  part_size = np.around(total_part_size/num_part).astype(int)

  #copiando para partições (sem aumentar)
  part1 = images_names[teste_size:(part_size+teste_size)]
  part2 = images_names[(part_size+teste_size):(part_size*2+teste_size)]
  part3 = images_names[(part_size*2+teste_size):(part_size*3+teste_size)]
  part4 = images_names[(part_size*3+teste_size):(part_size*4+teste_size)]
  part5 = images_names[(part_size*4+teste_size):]

  for i in part1:
    img = cv2.imread(origem_data_dir + nome_classe + '/' + i)
    cv2.imwrite(part_1 + nome_classe + '/' + i, img)

  for i in part2:
    img = cv2.imread(origem_data_dir + nome_classe + '/' + i)
    cv2.imwrite(part_2 + nome_classe + '/' + i, img)

  for i in part3:
    img = cv2.imread(origem_data_dir + nome_classe + '/' + i)
    cv2.imwrite(part_3 + nome_classe + '/' + i, img)

  for i in part4:
    img = cv2.imread(origem_data_dir + nome_classe + '/' + i)
    cv2.imwrite(part_4 + nome_classe + '/' + i, img)

  for i in part5:
    img = cv2.imread(origem_data_dir + nome_classe + '/' + i)
    cv2.imwrite(part_5 + nome_classe + '/' + i, img)

  print(nome_classe)
  print('Tamanho origem :' + str(len(tf.io.gfile.listdir(origem_data_dir + nome_classe))))
  print('Tamanho Folder1 :' + str(len(tf.io.gfile.listdir(part_1 + nome_classe))))
  print('Tamanho Folder2 :' + str(len(tf.io.gfile.listdir(part_2 + nome_classe))))
  print('Tamanho Folder3 :' + str(len(tf.io.gfile.listdir(part_3 + nome_classe))))
  print('Tamanho Folder4 :' + str(len(tf.io.gfile.listdir(part_4 + nome_classe))))
  print('Tamanho Folder5 :' + str(len(tf.io.gfile.listdir(part_5 + nome_classe))))

distribuir_imagens_particoes('covid', 5)

distribuir_imagens_particoes('dip', 5)

distribuir_imagens_particoes('normais', 5)

distribuir_imagens_particoes('tuberculose', 5)

def mover_pastas_treinam (nome_classe):

  part1_names = tf.io.gfile.listdir(part_1 + nome_classe)
  part2_names = tf.io.gfile.listdir(part_2 + nome_classe)
  part3_names = tf.io.gfile.listdir(part_3 + nome_classe)
  part4_names = tf.io.gfile.listdir(part_4 + nome_classe)
  part5_names = tf.io.gfile.listdir(part_5 + nome_classe)

  #partição 5 de fora
  for i in part1_names:
    img = cv2.imread(part_1 + nome_classe + '/' + i)
    cv2.imwrite(trein_1234 + nome_classe + '/' + i, img)
  for i in part2_names:
    img = cv2.imread(part_2 + nome_classe + '/' + i)
    cv2.imwrite(trein_1234 + nome_classe + '/' + i, img)
  for i in part3_names:
    img = cv2.imread(part_3 + nome_classe + '/' + i)
    cv2.imwrite(trein_1234 + nome_classe + '/' + i, img)
  for i in part4_names:
    img = cv2.imread(part_4 + nome_classe + '/' + i)
    cv2.imwrite(trein_1234 + nome_classe + '/' + i, img)

  #partição 4 de fora
  for i in part1_names:
    img = cv2.imread(part_1 + nome_classe + '/' + i)
    cv2.imwrite(trein_1235 + nome_classe + '/' + i, img)
  for i in part2_names:
    img = cv2.imread(part_2 + nome_classe + '/' + i)
    cv2.imwrite(trein_1235 + nome_classe + '/' + i, img)
  for i in part3_names:
    img = cv2.imread(part_3 + nome_classe + '/' + i)
    cv2.imwrite(trein_1235 + nome_classe + '/' + i, img)
  for i in part5_names:
    img = cv2.imread(part_5 + nome_classe + '/' + i)
    cv2.imwrite(trein_1235 + nome_classe + '/' + i, img)

  #partição 3 de fora
  for i in part1_names:
    img = cv2.imread(part_1 + nome_classe + '/' + i)
    cv2.imwrite(trein_1245 + nome_classe + '/' + i, img)
  for i in part2_names:
    img = cv2.imread(part_2 + nome_classe + '/' + i)
    cv2.imwrite(trein_1245 + nome_classe + '/' + i, img)
  for i in part5_names:
    img = cv2.imread(part_5 + nome_classe + '/' + i)
    cv2.imwrite(trein_1245 + nome_classe + '/' + i, img)
  for i in part4_names:
    img = cv2.imread(part_4 + nome_classe + '/' + i)
    cv2.imwrite(trein_1245 + nome_classe + '/' + i, img)

  #partição 2 de fora
  for i in part1_names:
    img = cv2.imread(part_1 + nome_classe + '/' + i)
    cv2.imwrite(trein_1345 + nome_classe + '/' + i, img)
  for i in part5_names:
    img = cv2.imread(part_5 + nome_classe + '/' + i)
    cv2.imwrite(trein_1345 + nome_classe + '/' + i, img)
  for i in part3_names:
    img = cv2.imread(part_3 + nome_classe + '/' + i)
    cv2.imwrite(trein_1345 + nome_classe + '/' + i, img)
  for i in part4_names:
    img = cv2.imread(part_4 + nome_classe + '/' + i)
    cv2.imwrite(trein_1345 + nome_classe + '/' + i, img)

  #partição 1 de fora
  for i in part5_names:
    img = cv2.imread(part_5 + nome_classe + '/' + i)
    cv2.imwrite(trein_2345 + nome_classe + '/' + i, img)
  for i in part2_names:
    img = cv2.imread(part_2 + nome_classe + '/' + i)
    cv2.imwrite(trein_2345 + nome_classe + '/' + i, img)
  for i in part3_names:
    img = cv2.imread(part_3 + nome_classe + '/' + i)
    cv2.imwrite(trein_2345 + nome_classe + '/' + i, img)
  for i in part4_names:
    img = cv2.imread(part_4 + nome_classe + '/' + i)
    cv2.imwrite(trein_2345 + nome_classe + '/' + i, img)


  print(nome_classe)
  print('Tamanho trein_1234:' + str(len(tf.io.gfile.listdir(trein_1234+nome_classe))))
  print('Tamanho trein_1235:' + str(len(tf.io.gfile.listdir(trein_1235+nome_classe))))
  print('Tamanho trein_1245:' + str(len(tf.io.gfile.listdir(trein_1245+nome_classe))))
  print('Tamanho trein_1345:' + str(len(tf.io.gfile.listdir(trein_1345+nome_classe))))
  print('Tamanho trein_2345:' + str(len(tf.io.gfile.listdir(trein_2345+nome_classe))))

mover_pastas_treinam('covid')

mover_pastas_treinam('dip')

mover_pastas_treinam('normais')

mover_pastas_treinam('tuberculose')

def aumentar_imagens (nome_classe, magnitude_x=0.2, augmentations_per_image_x=3, n_transformacoes=3):

  trein_1234_names = tf.io.gfile.listdir(trein_1234 + nome_classe)
  trein_1235_names = tf.io.gfile.listdir(trein_1235 + nome_classe)
  trein_1245_names = tf.io.gfile.listdir(trein_1245 + nome_classe)
  trein_1345_names = tf.io.gfile.listdir(trein_1345 + nome_classe)
  trein_2345_names = tf.io.gfile.listdir(trein_2345 + nome_classe)

  #partição 1
  for i in trein_1234_names:    #manda a original
    img = cv2.imread(trein_1234 + nome_classe + '/' + i)
    for j in range(n_transformacoes):
      aug_img = keras_cv.layers.RandAugment(value_range=(0, 255), magnitude=magnitude_x,magnitude_stddev = 0.15,augmentations_per_image=augmentations_per_image_x,rate = 1,geometric = True)(img)
      aug_img_nump = aug_img.numpy().astype('int')
      cv2.imwrite(trein_1234 + nome_classe + '/' + 't' + str(j) + '_' + i, aug_img_nump)

  #partição 2
  for i in trein_1235_names:    #manda a original
    img = cv2.imread(trein_1235 + nome_classe + '/' + i)
    for j in range(n_transformacoes):
      aug_img = keras_cv.layers.RandAugment(value_range=(0, 255), magnitude=magnitude_x,magnitude_stddev = 0.15,augmentations_per_image=augmentations_per_image_x,rate = 1,geometric = True)(img)
      aug_img_nump = aug_img.numpy().astype('int')
      cv2.imwrite(trein_1235 + nome_classe + '/' + 't' + str(j) + '_' + i, aug_img_nump)

  #partição 3
  for i in trein_1245_names:    #manda a original
    img = cv2.imread(trein_1245 + nome_classe + '/' + i)
    for j in range(n_transformacoes):
      aug_img = keras_cv.layers.RandAugment(value_range=(0, 255), magnitude=magnitude_x,magnitude_stddev = 0.15,augmentations_per_image=augmentations_per_image_x,rate = 1,geometric = True)(img)
      aug_img_nump = aug_img.numpy().astype('int')
      cv2.imwrite(trein_1245 + nome_classe + '/' + 't' + str(j) + '_' + i, aug_img_nump)

  #partição 4
  for i in trein_1345_names:    #manda a original
    img = cv2.imread(trein_1345 + nome_classe + '/' + i)
    for j in range(n_transformacoes):
      aug_img = keras_cv.layers.RandAugment(value_range=(0, 255), magnitude=magnitude_x,magnitude_stddev = 0.15,augmentations_per_image=augmentations_per_image_x,rate = 1,geometric = True)(img)
      aug_img_nump = aug_img.numpy().astype('int')
      cv2.imwrite(trein_1345 + nome_classe + '/' + 't' + str(j) + '_' + i, aug_img_nump)

  #partição 5
  for i in trein_2345_names:    #manda a original
    img = cv2.imread(trein_2345 + nome_classe + '/' + i)
    for j in range(n_transformacoes):
      aug_img = keras_cv.layers.RandAugment(value_range=(0, 255), magnitude=magnitude_x,magnitude_stddev = 0.15,augmentations_per_image=augmentations_per_image_x,rate = 1,geometric = True)(img)
      aug_img_nump = aug_img.numpy().astype('int')
      cv2.imwrite(trein_2345 + nome_classe + '/' + 't' + str(j) + '_' + i, aug_img_nump)

  print(nome_classe)
  print('Tamanho partição 1234 aumen:' + str(len(tf.io.gfile.listdir(trein_1234 + nome_classe))))
  print('Tamanho partição 1235 aumen:' + str(len(tf.io.gfile.listdir(trein_1235 + nome_classe))))
  print('Tamanho partição 1245 aumen:' + str(len(tf.io.gfile.listdir(trein_1245 + nome_classe))))
  print('Tamanho partição 1345 aumen:' + str(len(tf.io.gfile.listdir(trein_1345 + nome_classe))))
  print('Tamanho partição 2345 aumen:' + str(len(tf.io.gfile.listdir(trein_2345 + nome_classe))))

aumentar_imagens('covid', 0.2,3,2)

aumentar_imagens('dip', 0.2,3,4)

aumentar_imagens('normais', 0.2,3,2)

aumentar_imagens('tuberculose', 0.2,3,2)