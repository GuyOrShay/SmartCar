from pydoc import describe
from ObjectClassification.object__detection import test_tensor
from ObjectClassification.objects import objects
from Services.Camera.CameraController import cameraController
from Services.CheckDistance import check_distance
from Services.FrontLedDisplay import matrix_display
from Services.LaneAsistent import init_lane_sensors, is_car_in_road
from Services.MotorDrive import MotorDrive
from TrafficReportModule.StatusManagement import insertStatus
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
            distance_from_object = check_distance()
            for obj in detected_objects:
              accuracy = int(obj.accuracy * 100)
              if (accuracy > 80):
                if(distance_from_object < 10):
                  describe = "You close to crash into " , obj.name , " (" ,obj.accuricy, ") " 
                  insertStatus( describe,"Error")
                else:
                  describe = "You close to " , obj.name , " (" ,obj.accuricy, ") " , distance_from_object , " cm"
                  insertStatus(describe,"Warning")

          if(is_car_in_road() == False):
            insertStatus(" deviating from the path ","Error")
          camera.moveHorizontal()
#    while True:
#         isPictureTaken = camera.getStatus()
#         print(isPictureTaken)
#         if(isPictureTaken):
#             sign = traffic_sign_predict.trafficsign()
#             print(sign)
#             if (sign == "STOP"):
#                 print(sign)
#                 alert.play()
