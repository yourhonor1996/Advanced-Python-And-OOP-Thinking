import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host_ip = socket.gethostbyname('www.quera.ir') 
port = 80
s.connect((host_ip, port)) 

print("The socket has successfully connected to Quera on port == {}".format(host_ip))
s.close()