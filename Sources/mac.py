import random
// used to generate random variables

def randomMAC():
    return [ 0x00, 0x50, 0x56,
             random.randint(0x00, 0x7f),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff)]
// generates 3 random numbers with 3 default numbers
def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))
    // joint everything with :

if __name__=='__main__':
    print(MACprettyprint(randomMAC()))
// main function . runs everything.
// www.youtube.com/priyankgada
