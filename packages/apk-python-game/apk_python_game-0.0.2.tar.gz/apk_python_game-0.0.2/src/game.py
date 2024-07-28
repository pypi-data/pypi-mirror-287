import os
import time
nameList = ['Mango','Banana','Orange','Papaya','Lemone','Pinapple','Apple','Waterlemon','Grape','Cherrey']

def pageOne():
    for ind ,lst in enumerate(nameList,start=1):
        print(" "*8 +f"[ {ind} ]. {lst}")
    print()
    print("")
    
def clssrc():
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')


def pagehead():
    print()
    print()
    print(" "*5 +"*"*35)
    print()
    print(" "*13 +"WELLCOME TO OUR GAME")
    print()
    print(" "*5 +"*"*35)
    print()
    print()

def disspage(pg=1,lst=[]):
    clssrc()
    pagehead()
    ln=0
    for lstt in lst:
        ln +=1
        print(" "*8 +f"[ {ln} ]. {nameList[lstt]}")
    print()    
    ans = input(" "*6 +"Is it here (y/n)?. ")
    if ans=='y' or ans=='Y':
        return pg
    else:
        return 0
        
def ansgame(ans):
    clssrc()
    pagehead()
    print()
    print()
    msg = "";
    print(" "*6,end="")
    if(ans==0):
        msg = "Your answer is not correct. Try again.."
    else:
        msg = f"You think {nameList[ans - 1]}"

    for ll in msg:
        print(ll, end="")
        time.sleep(0.1)
    print("")    
    time.sleep(2)