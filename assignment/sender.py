import socket,pyttsx3
from cryptography.fernet import Fernet
target_ip = "127.0.0.1"
target_port = 1236
# now we are creating udp socket -- this is for all sender and reciever
# it means we use ipv4,UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#this is only for reciever
# s.bind((target_ip,target_port))

while True:
#this is for sender
	msg = input("please enter your message : ")
	cipher_key=b'GzDqzcu4kz52ZOyu7haSaWY4t4mE2jzSKD4JuYfm7VE='
	#cipher_key = Fernet.generate_key()
	#print(cipher_key)
	cipher = Fernet(cipher_key) # initailizing
	message = msg.encode() # to convert it to bytes
	encrypted = cipher.encrypt(message) #CONVERTING TO ENCRYTED MESSAGE	
	#new_msg = msg.encode('ascii')
	#message = b'the quick brown fox jumps over the lazy dog'
	#encrypted_message = cipher.encrypt(message)
	out_message=encrypted.decode()# turn it into a string to send
	new_msg = out_message.encode('ascii') # it will sent in bytes in ascii
	#print(new_msg)
	# we have to encode string to byte like object in python3 only
	s.sendto(new_msg,(target_ip,target_port)) # sending the message
	# reply section
	client_data = s.recvfrom(1000) # recieving the reply
	#client_data_s = client_data[0].decode('ascii') # converting the message to string
	#print(client_data_s)
	#client_data_b = client_data_s.encode() # converting the message to bytes
	print(client_data[0])
	cipher = Fernet(cipher_key) # initailizing
	decrypted = cipher.decrypt(client_data[0]) # decryting the message
	decrypted_message = decrypted.decode('ascii')
	print(decrypted_message)
	audio2 = pyttsx3.init()
	audio2.say(decrypted_message)
	audio2.runAndWait()
	print("the decrypted message is ",decrypted_message) # printing the decrypted message
	
 
