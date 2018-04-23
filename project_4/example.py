import ping, socket
import urllib.request as ulibr

#print (socket.gethostbyname(socket.gethostname()))
target = "www.dataandroses.com/"
print (socket.gethostbyname_ex(target))

#ip = ulibr.urlopen('./publicIP.php').read()

#using curl command
