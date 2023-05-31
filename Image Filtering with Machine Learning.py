"""Image filtering is used to enhance the edges in images and reduce the noisiness of an image. This technology is used in almost all smartphones. Although improving an image using the image filtering techniques can help in the process of object detection, face recognition and all tasks involved in computer vision

The mean filter is used to give a blur effect to an image to remove the existing noisiness. It determines the mean of the pixels within the n×n method. Then it replaces the intensity of pixels by the mean. This reduces some of the noisiness present in the image and also improves the edges of an image.

Let’s go through Image Filtering using the mean filter method; I will start by importing all the libraries and a picture of a WWE Superstar CM Punk, to explore image filtering techniques in Machine Learning."""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
%matplotlib inline
image = cv2.imread('cm.jpg') # reads the image
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV
figure_size = 9 # the dimension of the x and y axis of the kernal.
new_image = cv2.blur(image,(figure_size, figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Mean filter')
plt.xticks([]), plt.yticks([])
plt.show()

# The image will first be converted to grayscale
image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
figure_size = 9
new_image = cv2.blur(image2,(figure_size, figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Mean filter')
plt.xticks([]), plt.yticks([])
plt.show()

#The Gaussian filter is very similar to the mean filter, but it involves a weighted mean of the pixels with a parameter as sigma. Let’s go through this method of Image Filtering:

new_image = cv2.GaussianBlur(image, (figure_size, figure_size),0)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])
plt.show()

# Now let’s have a look whether the Gaussian Filter removes the marks when converted into a grayscale:

new_image_gauss = cv2.GaussianBlur(image2, (figure_size, figure_size),0)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image_gauss, cmap='gray'),plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])
plt.show()

#The median filter computes the median of the intensity of pixels. It then replaces the norm with the pixel intensity of mean pixels. Now let’s go through this technique:

new_image = cv2.medianBlur(image, figure_size)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Median Filter')
plt.xticks([]), plt.yticks([])
plt.show()

#The median effect leaves a better output by removing the noisiness of the image. It also did not leave any marks in the image that we saw in the above methods. Now let’s convert it into a grayscale image:

new_image = cv2.medianBlur(image2, figure_size)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Median Filter')
plt.xticks([]), plt.yticks([])
plt.show()

#Now I will create our own filter for Filtering Images than can improve the quality of the image and improves the smoothness of the picture. I will first create a function to design my own Image filter:

def safeer(data, filter_size):
  temp = []
  indexer = filter_size // 2
  new_image = data.copy()
  nrow, ncol = data.shape
  for i in range(nrow):
    for j in range(ncol):
      for k in range(i-indexer, i+indexer+1):
        for m in range(j-indexer, j+indexer+1):
          if (k &gt; -1) and (k &lt; nrow):
            if (m &gt; -1) and (m &lt; ncol):
              temp.append(data[k,m])
      temp.remove(data[i,j])
      max_value = max(temp)
      min_value = min(temp)
      if data[i,j] &gt; max_value:
        new_image[i,j] = max_value
      elif data[i,j] &lt; min_value:
        new_image[i,j] = min_value
        temp =[]
    return new_image.copy()
  
 #Now let’s use our filter to improve the quality of the grayscale image:

new_image = safeer(image2,5)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Image Filteration')
plt.xticks([]), plt.yticks([])
plt.show()

