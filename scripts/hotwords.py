#!/usr/bin/env python
import snowboydecoder
import sys
import signal

import rospy
from std_msgs.msg import String
# Demo code for listening two hotwords at the same time

import rospkg

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

rospack = rospkg.RosPack()
path = rospack.get_path('roboy_snapchat_filter') + '/resources/'
models = [path+"roboy.pmdl", path+"cheese.pmdl"]
rospy.init_node("snowboy")
publisher = rospy.Publisher("/roboy/cognition/apply_filter", String, queue_size=1)

def publish(string):
    print('detected %s'%string)
    publisher.publish(string)

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: True,
             lambda: publish("cheese")]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
