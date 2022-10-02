from ObjectClassification.objects import objects
from Services.Camera.CameraController import cameraController
from TrafficReportModule.httpServer import startServer
from Traffic_sign_classification.predict import traffic
from Services.AlertPlayer import alertPlayer
import multiprocessing


if __name__ == '__main__':   #Program entry
   object_detection = objects("./Services/Camera/status.jpg")
   object_detection.load_model()
   print(object_detection.predict())
   traffic_sign_predict = traffic("./Services/Camera/status.jpg") 
   
   alert = alertPlayer()
   p = multiprocessing.Process(target=startServer, args=())
   p.daemon = True
   p.start()

   camera = cameraController()
   
   while True:
        isPictureTaken = camera.getStatus()
        print(isPictureTaken)
        if(isPictureTaken):
            sign = traffic_sign_predict.trafficsign()
            print(sign)
            if (sign == "STOP"):
                print(sign)
                alert.play()
