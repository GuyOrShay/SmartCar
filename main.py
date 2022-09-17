from Services.Camera.CameraController import cameraController
from Traffic_sign_classification.predict import traffic
from Services.AlertPlayer import alertPlayer


if __name__ == '__main__':   #Program entry

   traffic_sign_predict = traffic("./Services/Camera/status.jpg") 
   
   alert = alertPlayer()
   camera = cameraController()
   print("Start")

   alert.play();  
   print("Finish")
   while True:
        isPictureTaken = camera.getStatus()
        print(isPictureTaken)
        if(isPictureTaken):
            sign = traffic_sign_predict.trafficsign()
            print(sign)
            if (sign == "STOP"):
                print(sign)
                alert.play()
            


