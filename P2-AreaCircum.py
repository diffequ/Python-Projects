# B.KORYAN - July 28 2017
# Description : Area and Circumference calculator for :
#               # Square
#               # Rectangle
#               # Circle
#               # Triangle
# Note: Incomplete.Changes will be made (July 31)
########################################################

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


def perimCircle(data):
    if(checkDigit(data)):
        print(3.1415926*2*float(data))

def areasq (length,width):
    if(checkDigit(length)):
        if(checkDigit(width)):
            print(float(data)**2)

def perimsq (data):
    if(checkDigit(data)):
        print(float(data)*4)

def arearect (data):
    # L*W
def perimrect (data):
    # 2*(L+W)
def areatri (data):
    # (h*b)/2
def perimtri (data):
    # side + base + side

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
        arearect (data = input("enter the radius:"))
    elif (select == '6'):
        perimrect (data = input("enter the radius:"))
    elif (select == '7'):
        areatri (data = input("enter the radius:"))
    elif (select == '8'):
        perimtri (data = input("enter the radius:"))
    else :
        print("Wrong Choice! GoodBye!")
        exit()
main()
