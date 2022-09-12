import socket as s
import os
import sys

#put the absolute path of assignment here
sys.path.append("/home/kali/Desktop/CS433_Assignments_AY2022/Assignment1")
import crypto


BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"
port = 11298

s = s.socket(s.AF_INET, s.SOCK_STREAM)
print("Socket created! ")
s.bind(('127.0.0.1',port))
s.listen()

# c is the client that server is listening to
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

def command_DWD(file,c,opt):
    try:

        with open(file, "rb") as f:

            while True:
                bytes_read = f.read(BUFFER_SIZE)
                bytes_read = crypto.encrypt(bytes_read.decode(),opt)
                print("Encrypted data is",bytes_read)
                
                if not bytes_read:
                    #send msg to the server that you read everything.
                    temp_str = " status OK"
                    temp_str = crypto.encrypt(temp_str,opt)
                    c.send(temp_str.encode())
                    break
                c.sendall(bytes_read.encode())
            
        return "with status OK"

    except:

        #send msg to the server that you don't read anything as file path is bad
        c.send(crypto.encrypt("status NOK",opt).encode())
        return "with status NOT OK"

def command_UPD(file,c,opt):
    # here file is the file path, c is client and opt is the option which type of crypto service we want from the command line
    file_name = file.split("/")[-1]
    with open(os.path.join(os.getcwd(),file_name), "wb") as f:

        while True:

            bytes_read = crypto.decrypt(c.recv(BUFFER_SIZE).decode(),opt)

            print("Decrypted Data is",bytes_read)

            # if decrypted string contain the last 9 characters correspond to status ok then break from the loop
            if bytes_read[-9:]=="status OK":
                f.write(bytes_read[:-9].encode())
                print("Received from Client with status OK")    
                break
            
            # if decrypted string correspond to status NOK then break from the loop
            elif bytes_read=="status NOK":
                print("Received from Client with status NOK")    
                os.remove(file_name)
                break
            
            else:
                f.write(bytes_read.encode())
    
while True:

    cmd = c.recv(1024).decode()
    if(len(cmd)==0 or cmd=="exit"):
        break
    
    flag = 0 # Created a flag for the two commands DWD and UPD

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
        ans = command_DWD(lt[1],c, int(lt[2]))
        flag = 1
    
    elif lt[0] == "UPD":
        command_UPD(lt[1],c, int(lt[2]))
        flag = 1
    
    if(flag==0):
        r = "Respone from the server "+ans
        c.send(r.encode())

s.close()