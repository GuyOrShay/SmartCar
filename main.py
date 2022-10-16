from ObjectClassification.object__detection import test_tensor
from ObjectClassification.objects import objects
from Services.Camera.CameraController import cameraController
from Services.CheckDistance import check_distance
from Services.FrontLedDisplay import matrix_display
from Services.LaneAsistent import init_lane_sensors, is_car_in_road
from Services.MotorDrive import MotorDrive
from TrafficReportModule.httpServer import startHttpServer
from Traffic_sign_classification.predict import traffic
from Services.AlertPlayer import alertPlayer
from Services.getIR import recive_command_from_remote,init_id
import time


if __name__ == '__main__':   #Program entry
   # test_tensor()
   # print(object_detection.predict())
   traffic_sign_predict = traffic("./Services/Camera/status.jpg") 
   object_detection = objects("./Services/Camera/status.jpg")
   object_detection.load_model()
   init_id()
   startHttpServer()
   alert = alertPlayer()
   motorDrive = MotorDrive()
   camera = cameraController()
   init_lane_sensors()
   object_detection.predict()
   print("Start listening..... !!")
   while True:
        command = recive_command_from_remote()
        if(command != 0x00):
          isPictureTaken = camera.getStatus()
          motorDrive.drive_cmd(command)
          matrix_display(command)
          if(isPictureTaken):
            # sign = traffic_sign_predict.trafficsign()
            detected_objects = object_detection.predict()
            for obj in detected_objects:
              print(obj.name , " - " , obj.accuracy)
          distance_from_object = check_distance()
          print("Distance :  {:.2f} cm".format(distance_from_object))
          if(distance_from_object < 40):
            alert.play()
          if(is_car_in_road()):
            print("The Car in road")

#    while True:
#         isPictureTaken = camera.getStatus()
#         print(isPictureTaken)
#         if(isPictureTaken):
#             sign = traffic_sign_predict.trafficsign()
#             print(sign)
#             if (sign == "STOP"):
#                 print(sign)
#                 alert.play()
