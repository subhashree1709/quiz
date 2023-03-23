import socket
from threading import Thread

nickname= input('CHOOSE YOUR NICKNAME: ')

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address= '127.0.0.1'
port= 8000
client.connect((ip_address,port))

print('connected to server...')

def recieve():
    while True:
        try:
            message= client.recv(2048).decode('utf-8')
            if message== 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else :
                print(message)
        except:
            print('an error occured')
            client.close()
            break

def write():
    while True:
        message= '{}: {}'.format(nickname,input(''))
        client.send(message.encdoe('utf-8'))

recieve_thread= Thread(target=recieve)
recieve_thread.start()
write_thread= Thread(target=write)
write_thread.start()