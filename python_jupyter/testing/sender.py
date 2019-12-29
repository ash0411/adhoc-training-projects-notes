import socket
target_ip = "127.0.0.1"
target_port = 1234
# now we are creating udp socket -- this is for all sender and reciever
# it means we use ipv4,UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#this is only for reciever
# s.bind((target_ip,target_port))

while True:
#this is for sender
    msg = input("please enter your message : ")
#now we can send to target
    new_msg = msg.encode('ascii')
#print(new_msg)
# we have to encode string to byte like object in python3 only
    s.sendto(new_msg,(target_ip,target_port))
    print(s.recvfrom(100))
 
