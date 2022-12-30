from flask import Flask, render_template, request
import eventlet
import eventlet.wsgi
import socketio
from flask_socketio import join_room, leave_room
from engineio.payload import Payload

Payload.max_decode_packets = 500000000000
sio = socketio.Server(cors_allowed_origins="*", logger=False, async_handlers=True)
# sio = socketio.AsyncServer(async_mode='aiohttp')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

import logging

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
app.logger.disabled = True

room = "1"


@sio.on("connect")
def connect(sid, environ):
    print(sid, "connected")
    sio.enter_room(sid, "video_users")
    print("entered room")


@sio.on("disconnect")
def disconnect(sid):
    print(sid, "disconnected")


@sio.on("message")
def handle_message(sid, msg):
    sio.emit("browser", msg, room="video_users")


if __name__ == "__main__":
    eventlet.wsgi.server(
        eventlet.listen(("127.0.0.1", 5000)), app, log=None, log_output=0
    )
