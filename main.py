import time
from unicodedata import name
import cv2 
from flask import Flask, render_template,Response
from flask import jsonify
from numpy import True_ 
from camera import VideoCamera

app = Flask(__name__,template_folder='template')

@app.route('/')
def indexx():
    return '<html><body><h1>My First Heading</h1><img id="bg" src="{{  url_for('video_feed')  }}" ></body></html>'

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
        b'content-type: image/jpeg\r\n\r\n'+frame
        + b'\r\n\r\n') 
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
        mimetype='multipart/x-mixed-replace;boundary=frame')
     

if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000',debug=True_)