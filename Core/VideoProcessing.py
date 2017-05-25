#!/usr/bin/python2.7
# -*-encoding=utf-8-*-

import cv2
import numpy as np
import os
import shutil
import os.path as path

video_dir = '/home/yangzheng/testData'
video_name = 'hand.mp4'
images_dir = path.join(video_dir,path.splitext(video_name)[0])
video_capture = cv2.VideoCapture(path.join(video_dir,video_name))
success, frame = video_capture.read()

while True:
    try:
        os.mkdir(images_dir)
        break
    except Exception,e:
        shutil.rmtree(images_dir)

#获得码率及尺寸
fps = video_capture.get(cv2.CAP_PROP_FPS)
size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print fps, size
n_frame = 0
n_save_frame = 0

name_width=5

while success:
    fr = cv2.resize(frame,(int(size[0]/5), int(size[1]/5)))
    fr = np.transpose(fr,(1,0,2))
    if n_frame%2==0:
        frame_name = str(n_save_frame)
        if len(frame_name)<name_width:
            frame_name = (name_width-len(frame_name))*'0'+frame_name
        fram_name = frame_name+'.jpg'
        cv2.imwrite(path.join(images_dir,fram_name),fr)
        n_save_frame=n_save_frame+1
    n_frame = n_frame + 1
    # cv2.imshow('video', fr)
    # cv2.waitKey(int(1000/60))
    # cv2.waitKey(1)
    success, frame = video_capture.read()