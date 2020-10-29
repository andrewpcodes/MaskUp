<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">MaskUP</h3>	

<div align="center">	

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 	
  [![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/aptracky/MaskUp/issues)	
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/aptracky/MaskUp/pulls)	
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)	

</div>	

---	

<p align="center"> This project is all about keeping people safe. A project using the OpenCV to use facial rec and some custom haar files to detect wheater someone has a mask properly on.	
    <br> 	
</p>	

## 📝 Table of Contents	
- [About](#about)	
- [Getting Started](#getting_started)	
- [Deployment](#deployment)	
- [Usage](#usage)	
- [Built Using](#built_using)	
- [TODO](../TODO.md)	
- [Contributing](../CONTRIBUTING.md)	
- [Authors](#authors)	
- [Acknowledgments](#acknowledgement)	

## 🧐 About <a name = "about"></a>	
    MaskUP is a client server application that its basic functionality is detecting whether or not a person is wearing a face mask properly. The client uses a camera to scan for faces and scrapes and formats that face to be ready for facial detection. This entails turning the face into a grayscale image. The client will then send the array of grayscale values to the server for detection. The server receives the data and uses OpenCV to detect facial features using a HAAR file. Then the server sends back a boolean value of whether or not the subject is wearing a face mask properly. The client will then display one of two images. 


## 🏁 Getting Started <a name = "getting_started"></a>	
Instructions to come!!!	

### Prerequisites	
Python 3.x
OpenCV Installed
Webcam or Camera
(or)
Can use images insated...exmaples bellow

### Installing	
COMING SOON

## 🎈 Usage <a name="usage"></a>	
- Telling People to Wear there Mask!!!
- Unlocking Doors
- Creating a library of images for a deep leanring library
- Could be implemented in:
    - Businesses
    - Schools
    - Dinning Halls
    - Appartment Buildings
    - Anywhere there is a need for people to weare a mask properly.

## 🚀 Deployment <a name = "deployment"></a>	
Add additional notes about how to deploy this on a live system.	

## ⛏️ Built Using <a name = "built_using"></a>	
- [Python](https://www.python.org/) - Language	
- [OpenCV](https://opencv.org/) - Face Detection Package

## ✍️ Authors <a name = "authors"></a>	
- [@aptracky](https://github.com/aptracky) - Idea & Work	


## 🎉 Acknowledgements <a name = "acknowledgement"></a>	
- Hat tip to anyone whose code was used	
- Inspiration: The people that walk around campus with there mask not on correctly	
- References: OpenCV
