"""we need to read the image in RBG format and then convert it to a grayscale image. This will turn an image into a classic black and white photo.

Then the next thing to do is invert the grayscale image also called negative image, this will be our inverted grayscale image. Inversion can be used to enhance details.

Then we can finally create the pencil sketch by mixing the grayscale image with the inverted blurry image. This can be done by dividing the grayscale image by the inverted blurry image. Since images are just arrays, we can easily do this programmatically using the divide function from the cv2 library in Python."""

"""The only library we need for converting an image into a pencil sketch with Python is an OpenCV library in Python. It can be used by using the pip command; pip install opencv-python. But it is not imported by the same name. Let’s import it to get started with the task:"""

import cv2

#Now the next thing to do is to read the image:

image = cv2.imread("dog.jpg")
cv2.imshow("Dog", image)
cv2.waitKey(0)

#Now after reading the image, we will create a new image by converting the original image to greyscale:

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Dog", gray_image)
cv2.waitKey(0)

#Now the next step is to invert the new grayscale image:

inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

#Now the next step in the process is to blur the image by using the Gaussian Function in OpenCV:

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

#Then the final step is to invert the blurred image, then we can easily convert the image into a pencil sketch:

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

#And finally, if you want to have a look at both the original image and the pencil sketch then you can use the following commands:

cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
