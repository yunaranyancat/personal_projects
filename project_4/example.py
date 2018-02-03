# import socket
# print (socket.gethostbyname(socket.gethostname()))
import urllib.request as ulibr
ip = ulibr.urlopen('./publicIP.php').read()

#using curl command
