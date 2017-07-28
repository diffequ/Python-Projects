# B.KORYAN - July 28 2017
# Description : Number base converter
#               - ascii to binary
#               - ascii to octal
#               - ascii to decimal
# Built-in functions bin(),oct(),and ord()
# has been used to make this project.
###########################################

def asctobin(char1):
    print("\nThe binary(base2) equivalent of",char1,"is:")
    print(bin(ord(char1)))

def asctooct(char2):
    print("\nThe octal(base8) equivalent of",char2,"is:")
    print(oct(ord(char2)))

def asctodec(char3):
    print("\nThe decimal(base10) equivalent of",char3,"is:")
    print(ord(char3))

def main():

    print("Number Base Converter - July 2017\n")
    print("1: ascii to binary\n2: ascii to octal\n3: ascii to decimal\n")

    choice = input("make a choice:")

    if (choice == '1'):
        char1 = input("enter a character:")
        asctobin(char1)
    elif (choice == '2'):
        char2 = input("enter a character:")
        asctooct(char2)
    elif (choice == '3'):
        char3 = input("enter a character:")
        asctodec(char3)
    else:
        print("Wrong Choice: Goodbye!")
main()
