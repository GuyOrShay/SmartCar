from ipaddress import ip_address
import socket
from webbrowser import get
from Services.LcdI2CWriter import LcdI2CWriter   

def getIp():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)   
    return IPAddr


def displayIpOnLed():
    lcdWriter = LcdI2CWriter()
    ip = getIp()
    lcdWriter.Write(ip)