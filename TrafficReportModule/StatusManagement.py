import json

from TrafficReportModule.DriveStatus import DriveStatus

statuses = []
def insertStatus( description , severaty):
    newStatus= DriveStatus(description,severaty)
    statuses.append(newStatus.__dict__)

def getStatuses():
    jsonStr = json.dumps(statuses)
    return jsonStr