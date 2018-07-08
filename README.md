# Roboy Snapchat Filter
Feature for applying Snapchat-alike filters like Roboy mask, mustache, pixelated sunglasses, flies, hat, crown and rainbow automatic in-face superposition in real time.

![alt text](https://github.com/Roboy/roboy_snapchat/blob/master/sprites/roboy.png) ![alt text](https://github.com/Roboy/roboy_snapchat/blob/master/sprites/roboy.png) ![alt text](https://github.com/Roboy/roboy_snapchat/blob/master/sprites/roboy.png)




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
