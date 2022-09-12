import socket as s
import os
import sys
from tempfile import tempdir

sys.path.append("/home/kali/Desktop/CS433_Assignments_AY2022/Assignment1")
import crypto

BUFFER_SIZE = 1024
port = 11298


s = s.socket(s.AF_INET, s.SOCK_STREAM)
s.connect(('127.0.0.1',port))

def command_UPD(file,s, opt):
    try:

        with open(file, "rb") as f:

            while True:

                bytes_read = crypto.encrypt(f.read(BUFFER_SIZE).decode(),opt)
                print("Encrypted Data is ",bytes_read)
                if not bytes_read:
                    #send msg to the server that you read everything.
                    temp_str = " status OK"
                    temp_str = crypto.encrypt(temp_str,opt)
                    s.send(temp_str.encode())
                    break
                s.sendall(bytes_read.encode())
            
        return "with status OK"

    except:

        #send msg to the server that you don't read anything as file path is bad
        s.send(crypto.encrypt("status NOK",opt).encode())
        return "with status NOT OK"



while True:
    flag = 0                    # to identify the commands DWD and UD commmands
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
            # print(file_name)
            with open(os.path.join(os.getcwd(),file_name), "wb") as f:

                while True:

                    bytes_read = s.recv(BUFFER_SIZE)
                    bytes_read = crypto.decrypt(bytes_read.decode(), int(lt[2]))
                    print("Decrypted information is", bytes_read)

                    # if decrypted string contain the last 9 characters correspond to status ok then break from the loop
                    if bytes_read[-9:]=="status OK":
                        f.write(bytes_read[:-9].encode())
                        print("Received from Server with status OK")    
                        break
                    
                    # if decrypted string correspond to status NOK then break from the loop
                    elif bytes_read=="status NOK":
                        print("Received from Server with status NOK")    
                        os.remove(file_name)
                        break
                    else:
                        print(bytes_read)
                        f.write(bytes_read.encode())
        
        if(lt[0]=="UPD"):
            flag = 1
            msg = command_UPD(lt[1], s, int(lt[2]))
            print("file upload is done",msg)
        

    if(flag==0):
        print(s.recv(1024).decode())
