import math
def flag(n) :
    k=""
    for elem in n:
        k+=chr(int(ord(elem)*math.log(ord(elem)))-2*ord(elem))
    return k


test = input("Saisir votre chance :\n ")
if flag(test)=="Ì£§ÈřĖÈòÝYÏÅòċ±ù š" :
    print("Arabaina !!!")
else :
    print("Manandrama hafa")