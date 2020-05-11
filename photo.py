import cv2
import datetime
import re

SAVE_DIR = './img_640480/'

video_input = cv2.VideoCapture(0)
video_input.set(cv2.CAP_PROP_FPS, 60)           # カメラFPSを60FPSに設定
video_input.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # カメラ画像の横幅を1280に設定
video_input.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # カメラ画像の縦幅を720に設定

if (video_input.isOpened() == False):
    exit()

while(True):
    ret, frame = video_input.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)&0xff

    #pで写真を撮る
    if key == ord('p'):
        now = datetime.datetime.now()
        filename = SAVE_DIR + now.strftime('%Y%m%d_%H%M%S') + '.jpg'
        print(filename)
        cv2.imwrite(filename, frame)

    #qで終了
    if key == ord('q'):
        cv2.destroyAllWindows()
        exit()

video_input.release()
