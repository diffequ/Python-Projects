# B.KORYAN - July 28 2017
# Description : Number base converter
#               - ascii to binary
#               - ascii to octal
#               - ascii to decimal
#               - ascii to hex
# Built-in functions bin(),oct(),and ord()
# has been used to make this project.
###########################################


def asctobin(char):
    print("\nThe binary(base2) equivalent of",char,"is:")
    print(bin(ord(char)))

def asctooct(char):
    print("\nThe octal(base8) equivalent of",char,"is:")
    print(oct(ord(char)))

def asctodec(char):
    print("\nThe decimal(base10) equivalent of",char,"is:")
    print(ord(char))

def asctohex(char):
    print("\nThe hex(base16) equivalent of",char,"is:")
    print(hex(ord(char)))

def main():

    print("\nNumber Base Converter - July 2017\n")
    print("1: ascii to binary\n2: ascii to octal\n3: ascii to decimal\n4: ascii to hex\n")

    choice = input("make a choice:")


    if (choice == '1'):
        asctobin(char = input("enter a character:"))
    elif (choice == '2'):
        asctooct(char = input("enter a character:"))
    elif (choice == '3'):
        asctodec(char = input("enter a character:"))
    elif (choice == '4'):
        asctohex(char = input("enter a character:"))
    else:
        print("Wrong Choice: Goodbye!")
        exit()
main()
