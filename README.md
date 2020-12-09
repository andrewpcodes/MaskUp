![Build and Test](https://github.com/aptracky//workflows/Build%20and%20Test/badge.svg)

# MASKUP
## Introduction

    MaskUP is a client server application that its basic functionality is detecting whether or not a person is wearing a face mask properly. The client uses a camera to scan for faces and scrapes and formats that face to be ready for facial detection. This entails turning the face into a grayscale image. The client will then send the array of grayscale values to the server for detection. The server receives the data and uses OpenCV to detect facial features using a HAAR file. Then the server sends back a boolean value of whether or not the subject is wearing a face mask properly. The client will then display one of two images. 

## Features
List all the features (use cases) of your application.
1. Detect facecoverings
2. Could be used to create a library for ML
3. Respond to the user if they are wearing there mask properly.
4. Light weight Client (Allows for implmintation with exsisting infurastructure with ease)

## Getting Started
### Installation and Setup
1. Make sure you have the latest python version installed. (python --version). You can check the latest version on the python website.
2. Clone the repo to your local workspace. (https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
3. Use pip to install cv2. (python -m pip install opencv-python)
4. Change the HOST and PORT variables at the top of both the client and server!!!

### Run
1. Run maskUpServer.py
2. Run maskUpClient.py
3. Enjoy!

## Demo video


## Acknowledgements
- Hat tip to anyone whose code was used	
- Inspiration: The people that walk around campus with there mask not on correctly
- References: OpenCV, python
## Contributors

* @aptracky, Team Lead/Developer
* @benmaizamatwit, Developer
