from ObjectClassification.objects import objects
from Services.Camera.CameraController import cameraController
from Services.FrontLedDisplay import matrix_display
from Services.MotorDrive import MotorDrive
from TrafficReportModule.httpServer import startServer
from Traffic_sign_classification.predict import traffic
from Services.AlertPlayer import alertPlayer
from Services.getIR import recive_command_from_remote,init_id
import multiprocessing


if __name__ == '__main__':   #Program entry
#    object_detection = objects("./Services/Camera/status.jpg")
#    object_detection.load_model()
#    print(object_detection.predict())
   #traffic_sign_predict = traffic("./Services/Camera/status.jpg") 
   init_id()
   matrix_display("forword")
   alert = alertPlayer()
   p = multiprocessing.Process(target=startServer, args=())
   p.daemon = True
   p.start()
   motorDrive = MotorDrive()
   camera = cameraController()
   while True:
        command = recive_command_from_remote()
        if(command != 0x00):
            print(command)
            motorDrive.drive_cmd(command)
#    while True:
#         isPictureTaken = camera.getStatus()
#         print(isPictureTaken)
#         if(isPictureTaken):
#             sign = traffic_sign_predict.trafficsign()
#             print(sign)
#             if (sign == "STOP"):
#                 print(sign)
#                 alert.play()
