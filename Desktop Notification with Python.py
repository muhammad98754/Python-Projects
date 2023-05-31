import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! It has been an hour!",
            timeout = 10
        )
        time.sleep(3600)
        
  #For this task you need to install a Python library known as Plyer, which is used to access the hardware components of your system. 
  #This library can be easily installed by using the pip command; pip install pyler.
