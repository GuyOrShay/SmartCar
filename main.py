import RPi.GPIO as GPIO
from ObjectClassification.object__detection import test_tensor
from ObjectClassification.objects import objects
from Services.Camera.CameraController import cameraController
from Services.CheckDistance import check_distance
from Services.FrontLedDisplay import matrix_display
from Services.LaneAsistent import init_lane_sensors, is_car_in_road
from Services.MotorDrive import MotorDrive
from TrafficReportModule.StatusManagement import TrafficReportModule
from TrafficReportModule.httpServer import startHttpServer
from Traffic_sign_classification.predict import traffic
from Services.AlertPlayer import alertPlayer
from Services.getIR import recive_command_from_remote,init_id
import cv2
import time

def start(TrafficReportModule):
   trafficReportModule = TrafficReportModule
   traffic_sign_predict = traffic("./Services/Camera/status.jpg") 
   object_detection = objects("./Services/Camera/status.jpg")
   object_detection.load_model()
   init_id()
   alert = alertPlayer()
   motorDrive = MotorDrive()
   camera = cameraController()
   init_lane_sensors()
   object_detection.predict()
   prevoius_lane_status = True
   print("Start listening..... !!")
   while True:
        command = recive_command_from_remote()
        if(command != 0x00):
          motorDrive.drive_cmd(command)
          matrix_display(command)
          isPictureTaken = camera.getStatus()
          if(True):
            # sign = traffic_sign_predict.trafficsign()
            detected_objects = object_detection.predict()
            distance_from_object = check_distance()
            for obj in detected_objects:
              accuracy = int(obj.accuracy * 100)
              print(obj.name , " ___ ",accuracy)
              accuracy = int(obj.accuracy * 100)
              if (accuracy > 80):
                print("Insert document")
                if(distance_from_object < 10):
                  describe = "You close to crash into " , obj.name , " (" ,accuracy, ") " 
                  trafficReportModule.insertStatus( describe,"Error")
                else:
                  describe = "You close to " , obj.name , " (" ,obj.accuracy, ") " , distance_from_object , " cm"
                  trafficReportModule.insertStatus(describe,"Warning")
          else:
            print("Error : Picture can't be taken") 
          lane_status = is_car_in_road()
          if(prevoius_lane_status != lane_status):  
            if(lane_status == False):
              trafficReportModule.insertStatus(" deviating from the path ","Error")
            prevoius_lane_status = lane_status

if __name__ == '__main__':   #Program entry
  # test_tensor()
  trafficReportModule = TrafficReportModule()
  server = startHttpServer(trafficReportModule) 
  try:
    start(trafficReportModule)
  except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
    server.kill()  
    cv2.VideoCapture(0).release()

 
