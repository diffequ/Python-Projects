# LM35 Temperature sensor with PIC16F877 and Python Interface
# Burak Koryan | e-mail : burak@koryan.ca | web: http://koryan.ca

import time
import serial

def init():
    print('\n\t\t A thermometer with LM35 and PIC16FXXXX')
    print('\tBurak Koryan | January 30 2018 | http://koryan.ca')
    print('1) Check temperature')
    print('2) Set Alarm')
    print('3) Check sensor status')
    print('4) Set information interval')
    print('5) Exit\n')
    return;

def check_temp():
    print('\nConnecting to the PIC...')
    print('Reading the sensor!')
    print('Retreiving Data!')
    return;

def set_alarm():
    temp_alarm = input('Enter the temperature you want alarm to be set at:')

    return;

def check_sensor():
    print('Checking the sensor...')
    return;

def set_interval():
    int_data = input('Enter the interval you want to display:')
    return;

def config_serial():
    ser = serial.Serial(0)
    print ser.portstr
    ser.write("hello")
    ser.close()

    return;

def main():

    init()
    config_serial()
    usr_select = input("Choose one of the options above:\n")

    if (usr_select == 1):
        check_temp()
        main()
    elif(usr_select == 2):
        set_alarm()
        main()
    elif(usr_select == 3):
        check_sensor()
        main()
    elif(usr_select == 4):
        set_interval()
        main()
    elif(usr_select == 5):
        print('Exiting program..Goodbye!\n\n')
    else:
        print('Wrong Entry!')
        main()


main()
