# B.KORYAN - Aug 3 2017
# Description : Calculator for:
                # Ohm's law
                # Power (using the 3 basic formulas)
                # inductance
                # reactance
                # frequency
# Note : Version 1.Will be updated again.
# Update : float number can be input too now. (Aug 6)
########################################################

def findI(V,R):
    print("\nthe I:",float(V)/float(R),"Amps")
    return;

def findR(V,I):
    print("\nthe R:",float(V)/float(I),"Ohms")
    return;

def findV(I,R):
    print("\nthe V:",float(I)*float(R),"Volts")
    return;

def findPwithVR(V,R):
    print("\nthe P:",(float(V)**2)/float(R),"Watts")
    return;

def findVwithPR(P,R):
    print("\nthe V:",((float(P)*float(R))**(1/2)),"Volts")
    return;

def findRwithVP(V,P):
    print("\nthe R:",(float(V)**2)/float(P),"Ohms")
    return;

def findxL(f,L):
    pi = 3.14159
    print("\nthe xL:",(2*pi*float(f)*float(L)),"Ohms")
    return;

def findF(xL,L):
    pi = 3.14159
    print("\nthe F:",(float(xL)/(2*pi*float(L))),"Hz")
    return;

def findL(xL,f):
    pi = 3.14159
    print("\nthe L:",float(xL)/(2*pi*float(f)),"H")
    return;

def checkDigit(data):
    if(data.replace(".","",1).isdigit()):
        return True
    else:
        print("Mistake! Try Again!")
        exit()

def init():
    print("\n-----------------------------------------------")
    print("Electrical Engineering Calculator - August 2017")
    print("-----------------------------------------------")

    print("Pick one from the following list:\n")
    print("Using Ohm's Law:\n")
    print("1) Find I using V and R:\n")
    print("2) Find V using I and R:\n")
    print("3) Find R using V and I:\n")
    print("Using generic power formula:\n")
    print("4) Find P using V and R:\n")
    print("5) Find V using P and R:\n")
    print("6) Find R using V and P:\n")
    print("Using Reactance formulas:\n")
    print("7) Find xL using f and L:\n")
    print("8) Find f using xL and L:\n")
    print("9) Find L using f and xL:\n")
    return;

def main():
        init()

        select = input("\nchoose one of the options:\n")

        if (select == '1'):
            V = input ("Enter V:")
            R = input ("Enter R:")
            if(checkDigit(V) and checkDigit(R)):
                findI(V,R)
        elif (select == '2' ):
            I = input ("Enter I:")
            R = input ("Enter R:")
            if(checkDigit(I) and checkDigit(R)):
                findV(I,R)
        elif (select == '3' ):
            V = input ("Enter V:")
            I = input ("Enter I:")
            if(checkDigit(V) and checkDigit(I)):
                findR(V,I)
        elif (select == '4' ):
            V = input ("Enter V:")
            R = input ("Enter R:")
            if(checkDigit(V) and checkDigit(R)):
                findPwithVR(V,R)
        elif (select == '5' ):
            P = input ("Enter P:")
            R = input ("Enter R:")
            if(checkDigit(P) and checkDigit(R)):
                findVwithPR(P,R)
        elif (select == '6' ):
            V = input ("Enter V:")
            P = input ("Enter P:")
            if(checkDigit(V) and checkDigit(P)):
                findRwithVP(V,P)
        elif (select == '7' ):
            f = input("Enter f:")
            L = input("Enter L:")
            if(checkDigit(f) and checkDigit(L)):
                findxL(f,L)
        elif (select == '8' ):
            xL = input("Enter xL:")
            L = input("Enter L:")
            if(checkDigit(xL) and checkDigit(L)):
                findF(xL,L)
        elif (select == '9' ):
            xL = input("Enter xL:")
            f = input("Enter f:")
            if(checkDigit(xL) and checkDigit(f)):
                findL(xL,f)
        else:
            print("Invalid choice!")
        exit()


main()
