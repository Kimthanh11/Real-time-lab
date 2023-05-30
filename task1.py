from keras.models import load_model
import cv2
import numpy as np
from  Adafruit_IO import  MQTTClient

class Task1:
    client = None
    model = None
    class_names = None
    camera = None
    index = None
    def connect(self):
        self.client = MQTTClient("name_goes_here" , "key_goes_here")
        self.client.connect()
        self.client.loop_background()
        return

    def __init__(self):

        print("Init task 1")

        self.connect()
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = load_model("keras_model.h5", compile=False)

        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        self.camera = cv2.VideoCapture(0)
        return
    
    def modelPredict(self, image):
        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]
        return class_name, confidence_score
    
    def Task1_Run(self):
        print("Task 1 is activated")

        # Grab the webcamera's image.
        ret, image = self.camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        class_name, confidence_score = self.modelPredict(image)

        # Print prediction and confidence score
        final_score = str(np.round(confidence_score * 100))[:-2]
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", final_score, "%")

        self.client.publish("acceptance rate", final_score)
