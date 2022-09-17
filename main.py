from Services.Camera.CameraController import cameraController
from Traffic_sign_classification.predict import traffic
from Services.AlertPlayer import alertPlayer


if __name__ == '__main__':   #Program entry

   traffic_sign_predict = traffic("Camera/status.jpg") 
   alert = alertPlayer()
   camera = cameraController()
   while True:
        isPictureTaken = camera.getStatus()
        if(isPictureTaken):
            sign = traffic_sign_predict.trafficsign()
            if (sign != "ERROR"):
                print(sign)
                alert.play()
            

