# B.KORYAN - July 28 2017
# Description : Area and Circumference calculator for :
#               # Square
#               # Rectangle
#               # Circle
#               # Triangle
# Note: Incomplete.Changes will be made (July 31)
# Note : Functions are completed.Needs to be more user friendly(Aug 1)
########################################################################

def checkDigit(data):
    if(data.isdigit()):
        return True
    else:
        print("Mistake! Try Again!")
        exit()

def circArea(data):
    pi = 3.1415926
    if(checkDigit(data)):
        print(pi*(float(data)**2))
        return;

def perimCircle(data):
    if(checkDigit(data)):
        print(3.1415926*2*float(data))
        return;

def areasq (length,width):
    if(checkDigit(length)):
        if(checkDigit(width)):
            print(float(data)**2)
            return;

def perimsq (data):
    if(checkDigit(data)):
        print(float(data)*4)
        return;
def arearect (length,width):
    if(checkDigit(length)):
        if(checkDigit(width)):
            print(float(length)*float(width))
            return;

def perimrect (length,width):
    if(checkDigit(length)):
        if(checkDigit(width)):
            print(2*(float(length)+float(width)))
            return;

def areatri (height,base):
    if(checkDigit(height)):
        if(checkDigit(base)):
            print((float(height)*float(base))/2)
            return;
def perimtri (side1,base,side2):
    if(checkDigit(side1)):
        if(checkDigit(base)):
            if(checkDigit(side2)):
                print(float(side1)+float(base)+float(side2))
                return;

def main():
    print ("\nArea and perimeter calculator - July 2017")
    print ("\nMake a choice:\n")
    print ("1) Find area of circle:\n")
    print ("2) Find perimeter of circle:\n")
    print ("3) Find area of square:\n")
    print ("4) Find perimeter of square:\n")
    print ("5) Find area of rectangle:\n")
    print ("6) Find perimeter of rectangle:\n")
    print ("7) Find area of triangle:\n")
    print ("8) Find perimeter of triangle:\n")

    select = input ("\nmake a choice:")

    if (select == '1'):
        circArea (data = input("enter the radius:"))
    elif (select == '2' ):
        perimCircle (data = input("enter the radius:"))
    elif (select == '3'):
        areasq (length = input("enter the radius:"),width = input("enter the width:"))
    elif (select == '4'):
        perimsq (data = input("enter the radius:"))
    elif (select == '5'):
        arearect (length = input("enter the length:"),width = input("enter the width:"))
    elif (select == '6'):
        perimrect (length = input("enter the length:"),width = input("enter the width:"))
    elif (select == '7'):
        areatri (height = input("enter the height:"),base = input("enter the base:"))
    elif (select == '8'):
        perimtri (side1 = input("enter the side1:"),base = input("enter the base:"),side2 = input("enter the side2:"))
    else :
        print("Wrong Choice! GoodBye!")
        exit()
main()
