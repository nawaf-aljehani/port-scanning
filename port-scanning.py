import sys

#host = sys.argv[1]
#port_range = sys.argv[2]
#port_list = port_range.split('_')
#start_port = int(port_list[0])
#end_port = int(port_list[1])
from socket import socket, AF_INET, SOCK_STREAM

host = "172.217.18.46"
start_port = 75  #from
end_port = 83    #to

for port in range(start_port,end_port):
     s = socket(AF_INET,SOCK_STREAM)
     s.settimeout(5)
    result = s.connect_ex((host,port))

if result == 0:
         print(f"the port {port} is running")
else:
        print(f"the port {port} is not running")
