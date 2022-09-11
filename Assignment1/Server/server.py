import socket as s
import os

BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"
port = 11315

s = s.socket(s.AF_INET, s.SOCK_STREAM)
print("Socket created! ")
s.bind(('127.0.0.1',port))
s.listen()
c,addr = s.accept()
print('Got connection from',addr)

def command_cwd():
    return os.getcwd()

def command_LS():
    path = command_cwd()
    lt = os.listdir(path)
    ans = ""
    for i in lt:
        ans += i
        ans += " "
    return ans

def command_chdir(path):
    try :
        os.chdir(path)
        return "with  status OK"
    except:
        return "with status NOT OK"

def command_DWD(file,c):
    try:

        with open(file, "rb") as f:

            while True:
                bytes_read = f.read(BUFFER_SIZE)
                print(bytes_read)
                if not bytes_read:
                    c.send("status OK".encode())
                    break
                c.sendall(bytes_read)
            
        return "with status OK"

    except:

        c.send("status NOK".encode())
        return "with status NOT OK"

def command_UPD(file,c):
    file_name = file.split("/")[-1]
    with open(os.path.join(os.getcwd(),file_name), "wb") as f:

        while True:

            bytes_read = c.recv(BUFFER_SIZE)
            print(bytes_read)
            if bytes_read.decode()[-9:]=="status OK":
                f.write(bytes_read[:-9])
                print("Received from Client with status OK")    
                break
            elif bytes_read.decode()=="status NOK":
                print("Received from Client with status NOK")    
                os.remove(file_name)
                break
            else:
                f.write(bytes_read)
    

while True:

    cmd = c.recv(1024).decode()
    if(len(cmd)==0 or cmd=="exit"):
        break
    
    flag = 0 

    print("Command received from the terminal",cmd)
    lt = cmd.split(" ")

    ans = "invalid commqand"
    if(lt[0] == "CWD"):
        ans = command_cwd()
    
    elif lt[0] == "LS":
        ans = command_LS()

    elif lt[0] == "CD":
        ans = command_chdir(lt[1])
    
    elif lt[0] == "DWD":
        ans = command_DWD(lt[1],c)
        flag = 1
    
    elif lt[0] == "UPD":
        print("ok ok")
        command_UPD(lt[1],c)
        flag = 1

    
    if(flag==0):
        r = "Respone from the server "+ans
        c.send(r.encode())

s.close()