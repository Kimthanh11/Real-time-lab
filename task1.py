from keras.models import load_model
import cv2
import numpy as np

class Task1:
    def __init__(self, index):
        print("Init task 1")
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = load_model("keras_Model.h5", compile=False)

        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        self.camera = cv2.VideoCapture(index)
        self.cameraID =  index
        return
    def Task1_Run(self):
        print("Task 1 is activated")
