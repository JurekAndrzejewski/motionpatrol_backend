import cv2
from MovementDetection import MovementDetection
import base64

from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from waitress import serve 


prev_frame1 = None
prev_frame2 = None
prev_frame3 = None

class Cam1(Resource):
    def get(self):
        global prev_frame1
        ret, img1 = vid1.read()
        if prev_frame1 is None:
            prev_frame1 = img1.copy()
        frame, prev_frame1 = MovementDetection(img1, prev_frame1, "1")
        image = cv2.imencode(".jpg", frame)[1]
        prev_frame1 = img1.copy()
        return {"data": str(base64.b64encode(image))}

class Cam2(Resource):
    def get(self):
        global prev_frame2
        ret, img2 = vid2.read()
        frame, prev_frame2 = MovementDetection(img2, prev_frame3, "2")
        image = cv2.imencode(".jpg", frame)[1]
        
        prev_frame2 = img2.copy()
        return {"data": str(base64.b64encode(image))}
    
class Cam3(Resource):
    def get(self):
        global prev_frame3
        ret, img3 = vid3.read()
        frame, prev_frame3 = MovementDetection(img3, prev_frame3, "3")
        image = cv2.imencode(".jpg", frame)[1]
        return {"data": str(base64.b64encode(image))}
    
def main():    
    global vid1
    global vid2
    global vid3
    
    vid1 = cv2.VideoCapture(0)
    #vid2 = cv2.VideoCapture(4)
    #vid3 = cv2.VideoCapture(0)

    app = Flask(__name__)
    api = CORS(app)
    api = Api(app)

    api.add_resource(Cam1, "/cam1")
    #api.add_resource(Cam2, "/cam2")
    #api.add_resource(Cam3, "/cam3")

    serve(app, host='127.0.0.1', port=5000, threads=6)
    
    vid1.release()
    #vid2.release()
    #vid3.release()

if __name__ == "__main__":
    main()
