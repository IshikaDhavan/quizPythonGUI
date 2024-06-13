import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#name = "Write your name: "
ipaddr = "127.0.0.1"
port = 7500

client.connect((ipaddr,port))
print("connected with server")

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width= False, height= False)
        self.login.configure(width= 400, height= 300)

        self.pls = Label(self.login, text="Login to continue", justify= CENTER, font="Helvetica 14 bold")
        self.pls.place(relheight= 0.15, relx= 0.2, rely=0.07)

        self.labelName = Label(self.login, text="Enter Name", font="Helvetica 12")
        self.labelName.place(relheight= 0.1, relx= 0.1, rely= 0.3)

        self.entryName = Entry(self.login, font="Helvetica 12")
        self.entryName.place(relwidth= 0.4,relheight= 0.12,relx= 0.35, rely= 0.3)

        self.go = Button(self.login,text="Continue", font="Helvetica 14 bold", command= lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx = 0.4, rely= 0.55)

        self.Window.mainloop()

    def goAhead(self,name):
        self.login.destroy()

        self.name = name
        rcv = Thread(target= self.receive)
        rcv.start()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occured")
                client.close()
                break


g = GUI()


#def write():
#    while True:
#        message = input('')
#        client.send(message.encode('utf-8'))

#recieve_thread = Thread(target= receive)
#recieve_thread.start()

#write_thread = Thread(target= write)
#write_thread.start()