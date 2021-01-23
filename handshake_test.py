'''
Code for handshake detection
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import stats
import glob
import os
from natsort import natsorted
from util import *
plt.rcParams['figure.figsize'] = [10, 5]

videopath = 'videos/ut-interaction_set2/seq18.avi'
vid_name = os.path.split(videopath)[1].split('.')[0]
savepath = 'results/'+vid_name
output_name = savepath+'/'+vid_name+'.json'

json_data = read_json(output_name)

cv2.namedWindow('frame')
cap = cv2.VideoCapture(videopath)

frame_num = 0
size = (512,288)

while (1):
    ret, frame = cap.read()
    frame = cv2.resize(frame, size)

    start_pt = []
    end_pt = []

    # Create start point and end point arrays
    for ind in json_data:
        if str(ind).isdigit() and json_data[ind] != {}:
            if int(ind) == frame_num:
                for shake in json_data[ind]:
                    start_pt.append(json_data[ind][shake]['start_pt'])
                    end_pt.append(json_data[ind][shake]['end_pt'])

    # Draw bounding box
    if ret == True:
        img_ = np.array(frame, copy=True)
        for s_id in range(len(start_pt)):
            cv2.rectangle(img_, tuple(start_pt[s_id]), tuple(end_pt[s_id]), [0, 0, 255], 2)
        cv2.imshow('frame', img_)

        frame_num += 1

        k = cv2.waitKey(0) & 0xff
        if k == ord('q'):
            break

    else:
        cv2.destroyAllWindows()
        break

