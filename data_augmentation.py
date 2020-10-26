# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 23:55:22 2020

@author: Raul Ortega Ochoa
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from elastic_transform import elastic_transform
import data_utils
from skimage.transform import resize
import matplotlib

drive_path = ""
path_save = ""
image_size = (100, 100)


for index in range(1, 1584):
    print(index)
    im_path = drive_path + 'images/{}.jpg'.format(index)
    image = imread(im_path, as_gray=True)
    image = data_utils.pad2square(image)  # Make the image square
    image = resize(image, output_shape=image_size, mode='reflect', anti_aliasing=True)  # resizes the image
    # plt.imshow(image, cmap='gray')
    # plt.axis('off')
    # plt.show()

    image = np.atleast_3d(image)
    # print(image.shape)
    transf_image = elastic_transform(image, alpha=70, sigma=3, random_state=None)
    transf_image = np.squeeze(transf_image, axis=None)
    # plt.imshow(transf_image, cmap='gray')
    # plt.axis('off')
    # plt.show()
    save_path = path_save + 'images_1/{}.jpg'.format(index)
    matplotlib.image.imsave(save_path, transf_image)