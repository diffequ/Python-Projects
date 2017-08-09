# B.KORYAN - Aug 8 2017
# Python projects - Imaginary/Real number calculator
# Note: There'll be an update on Aug 9

import math


def checkDigit(data):
    if(data.replace(".","",1).isdigit()):
        return True
    else:
        print("Mistake! Try Again!")
        exit()

def conv_polar(Real,Imag):
        real_num = ((float(Real)**2)+(float(Imag)**2))**(1/2)
        rad = math.atan(float(Imag)/float(Real))
        deg = round(math.degrees(rad))

        print("\nReal part:%.3f\n" % real_num)
        print("Degree:",deg)
        return;

def conv_imag(Real_part,degree):
        # a + bi
        a = float(Real_part)*math.cos(math.radians(float(degree)))
        b = float(Real_part)*math.sin(math.radians(float(degree)))
        print("%.2f" % a)
        print("%.2f" % b)
        return;

def main():

    print("\nWhat conversion would you like to do?\n")
    print("1)Rectangular to Polar\n2)Polar to Rectangular")
    choice = input("Enter:")

    if(choice == '1'):
            Imag = input("Enter the Imag:")
            Real = input("Enter the Real:")
            if (checkDigit(Imag) and checkDigit(Real)):
                    conv_polar(Real,Imag)
    elif(choice == '2'):
            Real_part = input("Enter the real:")
            degree = input("Enter the degree:")
            if (checkDigit(Real_part) and checkDigit(degree)):
                    conv_imag(Real_part,degree)
    else:
            print("Invalid choice!")
            exit()

main()
