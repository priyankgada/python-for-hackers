from uuid import getnode as get_mac #imports getnode
mac = get_mac() #mac = get_mac function
print(mac) #prints Mac address 
print(hex(mac)) #converts and prints hex of mac address
macString = ':'.join(("%012X" % mac) [i:i+2] for i in range(0,12,2)) #joints everything with : 
print('[' + macString + ']') #prints final mac address.
#www.youtube.com/priyankgada
