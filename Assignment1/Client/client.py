import socket as s
import os
import sys 

BUFFER_SIZE = 1024
port = 11315


s = s.socket(s.AF_INET, s.SOCK_STREAM)
s.connect(('127.0.0.1',port))

def command_UPD(file,s):
    try:

        with open(file, "rb") as f:

            while True:

                bytes_read = f.read(BUFFER_SIZE)
                print(bytes_read)
                if not bytes_read:
                    s.send("status OK".encode())
                    break
                s.sendall(bytes_read)
            
        return "with status OK"

    except:

        s.send("status NOK".encode())
        return "with status NOT OK"



while True:
    flag = 0                    # to identify the commands DWD and UD
    cmd = input()
    if cmd =="exit" or len(cmd) == 0:
        s.close()
        sys.exit()

    elif len(cmd)>0:
        
        s.send(cmd.encode())
        lt = cmd.split(" ")
        if(lt[0]=="DWD"):

            flag = 1
            file_name = lt[1].split("/")[-1]
            print(file_name)
            with open(os.path.join(os.getcwd(),file_name), "wb") as f:

                while True:

                    bytes_read = s.recv(BUFFER_SIZE)
                    print(bytes_read)
                    if bytes_read.decode()[-9:]=="status OK":
                        f.write(bytes_read[:-9])
                        print("Received from Server with status OK")    
                        break
                    elif bytes_read.decode()=="status NOK":
                        print("Received from Server with status NOK")    
                        os.remove(file_name)
                        break
                    else:
                        f.write(bytes_read)
        
        if(lt[0]=="UPD"):
            flag = 1
            msg = command_UPD(lt[1], s)
            print("file upload is done",msg)
        

    if(flag==0):
        print(s.recv(1024).decode())
