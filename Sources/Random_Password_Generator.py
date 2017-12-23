import string
from random import *
characters = string.ascii_letters + string.digits
password = "".join(choice(characters) for x in range(randint(1,2)))
print password
// www.youtube.com/priyankgada
