import json

from TrafficReportModule.DriveStatus import DriveStatus

class TrafficReportModule:
    def __init__(self):
        self.statuses = []
        self.path = "./TrafficReportModule/status.json"
    def insertStatus( self,description , severaty):
        newStatus= DriveStatus(description,severaty)
        with open(self.path,'r') as openFile:
            self.statuses = json.load(openFile)
            if(self.statuses.Length > 0):
                self.statuses.append(newStatus)
        with open(self.path , "w") as outfile:
            json.dump(self.statuses.__dict__ ,outfile)

    def getStatuses(self):
        with open(self.path,'r') as openFile:
            jsonStr = json.load(openFile)
            return jsonStr