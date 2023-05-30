from keras.models import load_model
import cv2
import numpy as np

class Detection:
    model = None
    class_names = None
    image = None
    camera = None
    cameraID = None
    delay = None
    count = None
    def __init__(self, index, delay):
        print("Init task 1")
        np.set_printoptions(suppress=True)
        self.delay = delay
        self.count = delay
        # Load the model
        self.model = load_model("lab_tensorflow\\keras_model.h5", compile=False)

        # Load the labels
        self.class_names = open("lab_tensorflow\\labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on the default camera of your computer
        self.camera = cv2.VideoCapture(index)
        self.cameraID = index
        self.update_image()

    def update_image(self):
        ret, image = self.camera.read()
        self.image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    def prediction(self):
        image = np.asarray(self.image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predict the model
        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]
        print("=============================")
        print("Camera " + str(self.cameraID))
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
    def run(self):
        if(self.count == 0):
            self.count = self.delay
            self.prediction()
        self.count = self.count - 1
        self.update_image()
        cv2.imshow("Cam " + str(self.cameraID), self.image)
        
        cv2.waitKey(1)  # Update the camera feed continuously

