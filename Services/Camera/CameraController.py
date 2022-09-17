
import cv2
class cameraController:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 480)  # Gets the video frame width
        self.capture.set(10, 55)  # Screen brightness

    def getStatus(self):
        if (self.capture.isOpened()):
            # Open the camera and read the image
            flag, image = self.capture.read()
            if(flag):
                    cv2.imwrite("status.jpg", image)
        self.capture.release()
        return flag

    def playVideo(self):
            while self.capture.isOpened():
                flag, image = self.capture.read()
                if(flag):
                    cv2.imshow("image", image)
            
            self.capture.release()
            # Close all Windows
            cv2.destroyAllWindows()