#Python For Hackers - Priyank Gada
#www.youtube.com/priyakgada
#Requires Py2exe module extention 
#for Tutorial check youtube channel

from distutils.core import setup
import py2exe #module to convert file
import sys
import os #for operations
sys.argv.append("py2.exe")
setup(
    options={'py2exe':{'bundle_files':1}}
    windows = [{'script':"convert.py"}] #convert.py is the name of the file to convert 
    zipfile=None, #No zip files 
)

#subscribe 
