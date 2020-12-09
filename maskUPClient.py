## MASKUP - Authors: Andrew P, Mohamed B ##

# Imports
import cv2
import io
import socket
import struct
import time
import pickle
import zlib
from tkinter import *
from PIL import Image

## Connecting to the server.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('YOUR IP HERE', "YOUR PORT HERE"))
connection = client_socket.makefile('wb')

# Initiating the video capture with cv2
cam = cv2.VideoCapture(0)

cam.set(3, 320)
cam.set(4, 240)

im_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
recived = ""
  
# This is the main while loop that is capturing, sending, and reciving the data from the client to the server.
while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame, 0)
    size = len(data)

    print("{}: {}".format(im_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    im_counter += 1
    recived = client_socket.recv(1024)
    print(recived)
    if(recived == b'1'):
        img = Image.open("assets/NETWORK.PNG")
        #img.show("Image")
    elif(recived == b'0'):
        img = Image.open("assets/NETWORK2.PNG")
        #img.show("Image")

#Close the connection and 
client_socket.close()
cam.release()
