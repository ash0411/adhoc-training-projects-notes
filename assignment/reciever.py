target_ip = "127.0.0.1"
target_port = 1235
from cryptography.fernet import Fernet
# now we are creating udp socket -- this is for all sender and reciever
# it means we use ipv4,UDP
import socket,time,pyttsx3,subprocess
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#this is only for reciever
s.bind((target_ip,target_port))
while True:
   # time.sleep(1)
	client_data = s.recvfrom(100)
	client_datas = ''.join(client_data)
	print(type(client_datas))
	cipher_key =b'WDrevvK8ZrPn8gmiNFjcOp2xovBr40TCwJlZOyI94IY='
	cipher = Fernet(cipher_key)
	decrypted_message = cipher.decrypt(client_data)   #decrypted_message = cipher.decrypt(encrypted_message)
	print("\nreceived message =",str(decrypted_message.decode("utf-8")))
	audio1 = pyttsx3.init()
	audio1.say(client_data[0].decode('ascii'))
	audio1.runAndWait()
	print(client_data)
	print("now replying  to ",client_data[1][0])
	s.sendto("hii guys thanks for the message ".encode('ascii'),client_data[1])
	subprocess.getoutput("touch " + client_data[1][0] + ".txt")
	with open(client_data[1][0]+".txt","a") as f:
		f.write(client_data[0].decode('ascii'))
		f.write("\n")
