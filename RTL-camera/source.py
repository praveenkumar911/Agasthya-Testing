import cv2
import json
import socketio
from flask_socketio import send, emit
import time
import base64

RECONNECT_FREQ = 1
SERVER_IP = r"http://65.1.162.104:5000"

sio = socketio.Client(engineio_logger=False)
cap = cv2.VideoCapture(0)


@sio.on("connect")
def on_connect():
    print("starting camera loop")
    handle_my_custom_event()


@sio.on("disconnect")
def on_disconnect():
    print("lost connection")
    sio.disconnect()
    reconnectsio()


def handle_my_custom_event():
    print("hi from camera loop")
    # try:
    while cap.isOpened():
        ret, img = cap.read()
        #print(0)
        if ret:
           # print(1)
           # k = 8
            k=1
            fps = 30
            img = cv2.resize(img, (k * 32, k * 32), fx=0.5, fy=0.5)
            frame = cv2.imencode(".jpg", img)[1].tobytes()
            frame = base64.encodebytes(frame).decode("utf-8")

           # print(2)
            sio.send(frame)
           # print(3)
            time.sleep(1 / fps)
        time.sleep(2)
    print("exiting camera loop")
    # except:
    #     pass


def reconnectsio():
    COUNT = 0
    while True:
        COUNT += 1
        try:
            print("trying to connect", COUNT)
            sio.connect(SERVER_IP)
            break
        except:
            pass
        time.sleep(RECONNECT_FREQ)
    print("connection established")


if __name__ == "__main__":
    reconnectsio()
    
    
    
