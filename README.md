# Roboy Snapchat Filter
Feature for applying Snapchat-alike filters like Roboy mask, mustache, pixelated sunglasses, flies, hat, crown and rainbow automatic in-face superposition in real time: 

![alt text](https://github.com/Roboy/roboy_snapchat/blob/master/imgs/roboy_filters.png) 

Multiple filters can be applied simultaneously:

![alt text](https://github.com/Roboy/roboy_snapchat/blob/master/imgs/all.png)

The implementation of Roboy Snapchat Filter uses a [Histogram of Oriented Gradients (HOG)](https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients) feature combined with a linear classifier, an image pyramid, and sliding window detection scheme to detect faces. Then it finds the 68 facial landmarks using an [Ensemble of Regression Trees](https://pdfs.semanticscholar.org/d78b/6a5b0dcaa81b1faea5fb0000045a62513567.pdf) to detect the face characteristics and to estimate the tilt angle of the face. The points around the mouth are used to detect wether it is open and if so, display a rainbow coming out.


## Requirements

* OpenCV 3.0+ with python bindings
* Python 2.7
     * pillow
     * numpy
     * tkinter
* Python bindings of dlib.
* [ROS Kinetic](http://wiki.ros.org/kinetic)
* [Catkin Workspace](https://github.com/Roboy)



## Prerequisites

Install OpenCV, see [this web page](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/) or install the light version with `sudo apt-get install libopencv-dev python-opencv`

For installing Tkinter execute `apt-get install python-tk`

For installing NumPy execute `sudo apt-get install build-essential python-dev`

For installing Pillow excute `sudo apt install python-pil`

For Dlib installation make sure you have the prerequisites:
```
sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev
```
Finally install it with `pip install dlib`



## ROS service

Roboy Snapchat Filter is a ROS package and depens on `roboy_communication_cogntion`. To start it's ROS server do following:

- Start ROS master in terminal with 
```
roscore
```

- In a new terminal change directory to
```
cd roboy_snapchat/roboy_snapchat_filter/scripts/
```
here, start the snapchat server with
```
rosrun roboy_snapchat_filter snapchat_server.py
```

- Use following ROS service call to trigger a filter
```
rosservice call /roboy/cognition/apply_filter "name: 'hat'"
```

Replace `hat` with one of the other filters:
`roboy`, `mustache`, `sunglasses`, `flies`, `crown`


When opening the mouth, the `rainbow` filter will automatically be applied
