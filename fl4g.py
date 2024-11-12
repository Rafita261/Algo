#This script encrypts our users' passwords
import math
def ln(x):return math.log(x)
def gagazo(n) :
    k=""
    for elem in n :
        x = ord(elem)-47
        k+=chr(int(x*ln(x)))
    return k
