from ObjectClassification.objects import objects
from Services.Camera.CameraController import cameraController
from Services.CheckDistance import check_distance
from Services.FrontLedDisplay import matrix_display
from Services.MotorDrive import MotorDrive
from TrafficReportModule.httpServer import startHttpServer
from Traffic_sign_classification.predict import traffic
from Services.AlertPlayer import alertPlayer
from Services.getIR import recive_command_from_remote,init_id


if __name__ == '__main__':   #Program entry
    
#    print(object_detection.predict())
   traffic_sign_predict = traffic("./Services/Camera/status.jpg") 
   object_detection = objects("./Services/Camera/status.jpg")
   object_detection.load_model()
   init_id()
   startHttpServer()
   alert = alertPlayer()
   motorDrive = MotorDrive()
   camera = cameraController()
   while True:
        command = recive_command_from_remote()
        if(command != 0x00):
          isPictureTaken = camera.getStatus()
          motorDrive.drive_cmd(command)
          matrix_display(command)
          if(isPictureTaken):
            sign = traffic_sign_predict.trafficsign()
            detected_objects = object_detection.predict()
          distance_from_object = check_distance()
          if(distance_from_object < 40):
            alert.play()

#    while True:
#         isPictureTaken = camera.getStatus()
#         print(isPictureTaken)
#         if(isPictureTaken):
#             sign = traffic_sign_predict.trafficsign()
#             print(sign)
#             if (sign == "STOP"):
#                 print(sign)
#                 alert.play()
