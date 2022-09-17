from ipaddress import ip_address
import socket   

def getIp():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)   
    return ip_address