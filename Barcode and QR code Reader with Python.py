#The first step is to install the following three libraries: Pillow, OpenCV and Pyzbar. Pillow is the extension of PIL, which stands for Python Image Library.

#OpenCV is a well-known library, especially when working with computer vision tasks. And the last library we need is Pyzbar, a python library that will help us read barcode and QR codes. You can easily install all the libraries using the pip command.

import cv2
from pyzbar import pyzbar

"""Now the next step is to write the decode function, where most of the cool stuff will happen. The decode function will mainly do three things and can be listed as follows:

Recognize and decode the barcode / QR code that we are going to show to the camera.
Added information stored as text on recognized barcode / QR code.
And finally, export the stored information as a text document."""


#Now let’s define the decoding function:

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame
  
  
  """Now let’s go through the above function to understand what I did:

First, we decode the barcode or QR code information. And then draw a rectangle around it. It helps us to see if our machine detected the barcode / Qr code.
Second, we add text above the rectangle that has been created. The text will display the decoded information.
Third, we export the information to a text document.
Now the next step is to write the main function for building a Barcode and QR code reader with Python. Let’s create our main function:"""
def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
    
    """Now let’s go through the main function above to understand what I did:

First of all, we turn on the computer camera using OpenCV. If you have an external camera, you need to change the value 0 to 1 depending on the device.
Second, we run a while loop to continue performing the decode function until the “Esc” key is pressed. Otherwise, the loop will not stop and cause problems.
Third, we launch the camera that we turned on in the first step. And then we close the application window. OpenCV does all the work, just call the methods.
Finally, we call the main function to trigger the program."""
