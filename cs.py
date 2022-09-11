import socket
import threading
from termcolor import colored
import os

#clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Connecting To Server
host = input(colored("Enter server IP Address: ", "green"))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, 55555))

# Choosing Nickname
nickname = input(colored("Choose your nickname: ", "green"))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(colored(message, "green"))
        except:
            # Close Connection When Error
            colored("An error occured!", "green")
            print(colored("An error occured!", "green"))
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()