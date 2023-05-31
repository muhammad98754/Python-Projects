"""filters are designed to improve the quality of the image. These filters are an example of complex machine learning algorithms that are deployed in production to serve Instagram. So if these filters are created by machine learning algorithms, it means that we can also create Instagram filters with Python."""

"""While building a neural network to create Instagram filters is a complex task. In this article, I will use the Instafilter library in Python which will help us to use Instagram filters with Python. 
install this library by using the pip command – pip install instafilter.
To use OpenCV we do not import it by the same name, we import it by the name of cv2 (import cv2)."""
from instafilter import Instafilter

model = Instafilter("Lo-fi")
new_image = model("image.jpg")

# To save the image, use cv2
import cv2
cv2.imwrite("modified_image.jpg", new_image)
