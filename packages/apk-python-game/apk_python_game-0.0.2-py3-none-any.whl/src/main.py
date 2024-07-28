import os
import game

def welcome():
    print()
    print()
    print(" "*5 +"*"*35)
    print()
    print(" "*13 +"WELLCOME TO OUR GAME")
    print()
    print(" "*5 +"*"*35)
    print()
    print()


while True:
    game.clssrc()
    welcome()
    game.pageOne()
    tol = 0
    print(" "*6 +"Think of one of these.")
    print()
    print(" "*6 +"If you want to EXIT . Type exit . ")
    print(" "*6 +"If you want to Continute , Press any key.... ")
    ex = input(" "*6 +"Enter Your Choise ?.")
    if ex=='exit' or ex=='EXIT' :
        break
    else:
        #pass
        tol = game.disspage(1,[0,2,3,7,9])
        tol += game.disspage(2,[1,2,4,8,5,9])
        tol += game.disspage(3,[6,3,4,8,7,9])
        tol += game.disspage(4,[9,7,5,8,6])
        
        game.ansgame(tol)
