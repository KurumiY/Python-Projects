#Kurumi Yamada
#ISE2900
#Project with Python

import os
print(os.environ['USERNAME'])

#Imports
import math

#Functions
#Sine function
def sin_function(x_value):
    print('sin(' + str(x_value) + ') = ' + str(math.sin(math.radians(x_value))))

#Cosine function
def cos_function(x_value):
    print('cos(' + str(x_value) + ') = ' + str(math.cos(math.radians(x_value))))

#Tangent function
def tan_function(x_value):
    print('tan(' + str(x_value) + ') = ' + str(math.tan(math.radians(x_value))))

#Arcsine function
def asin_function(x_value):
    print('asin(' + str(x_value) + ') = ' + str(math.degrees(math.asin(x_value))))

#Arccosine function
def acos_function(x_value):
    print('acos(' + str(x_value) + ') = ' + str(math.degrees(math.acos(x_value))))

#Arctangent function
def atan_function(x_value):
    print('atan(' + str(x_value) + ') = ' + str(math.degrees(math.atan(x_value))))

#Natural log function
def ln_function(x_value):
    print('ln(' + str(x_value) + ') = ' + str(math.log(x_value)))

#Square root function
def sqrt_function(x_value):
    print('sqrt(' + str(x_value) + ') = ' + str(math.sqrt(x_value)))

#Factorial function
def factorial_fuction(x_value):
    print('factorial(' + str(x_value) + ') = ' + str(math.factorial(x_value)))

#List for history of arguements
operations = []
arguements = []

#Going through the values in a while loop until quit or exit is entered
while True:
    val = input('Enter the number of operation that you want to execute <type exit or quit to end program>\n1. Sin(x)\n2. Cos(x)\n3. Tan(x)\n4. Asin(x)\n5. Acos(x)\n6. Atan(x)\n7. Ln(x)\n8. Sqrt(x)\n9. Factorial(x)\n10. History\n')

    #Makes it so case sensitivity doesn't matter
    val = val.lower()
    if val == 'quit' or val == 'exit':
        break
    #Sine
    elif val == '1':
        while True:
            x_value = input('Enter a number for sine function: ')
            try:
                x_value = int(x_value)
            except ValueError:
                print('Invalid arguement should not be a word please try again.')
            else:
                operations.append(val)
                arguements.append(x_value)
                sin_function(x_value)
                break
    #Cosine
    elif val == '2':
        while True:
            x_value = input('Enter a number for cosine function: ')
            try:
                x_value = int(x_value)
            except ValueError:
                print('Invalid arguement should not be a word please try again.')
            else:
                operations.append(val)
                arguements.append(x_value)
                cos_function(x_value)
                break
    #Tangent
    elif val == '3':
        while True:
            x_value = input('Enter a number for tangent function (Anything that is not divisible by 90): ')
            try:
                x_value = int(x_value)
            except ValueError:
                print('Invalid arguement should not be divisble by 90 please try again.')
            else:
                #Adds the values to history
                if (x_value % 90 == 0):
                    print('Invalid arguement should not be divisble by 90 please try again')
                else:
                    operations.append(val)
                    arguements.append(x_value)
                    tan_function(x_value)
                    break
    #Arcsine
    elif val == '4':
        while True:
            x_value = input('Enter a number for arcsine function (-1 to 1): ')
            try:
                x_value = float(x_value)
            except ValueError:
                print('Invalid arguement. Should be between -1 and 1 please try again.')
            else:
                try:
                    asin_function(x_value)
                except ValueError:
                    print('Invalid arguement. Should be between -1 and 1 please try again.')
                else:
                    #Adds the values to history
                    operations.append(val)
                    arguements.append(x_value)
                    break
    #Arccosine
    elif val == '5':
        while True:
            x_value = input('Enter a number for arccosine function (-1 to 1): ')
            try:
                x_value = float(x_value)
            except ValueError:
                print('Invalid arguement. Should be between -1 and 1 please try again.')
            else:
                try:
                    acos_function(x_value)
                except ValueError:
                    print('Invalid arguement. Should be between -1 and 1 please try again.')
                else:
                    #Adds the values to history
                    operations.append(val)
                    arguements.append(x_value)
                    break
    elif val == '6':
        while True:
            x_value = input('Enter a number for arctangent function (-90 to 90): ')
            try:
                x_value = float(x_value)
            except ValueError:
                print('Invalid arguement. Should be between -90 and 90 please try again.')
            else:
                try:
                    atan_function(x_value)
                except ValueError:
                    print('Invalid arguement. Should be between -90 and 90 please try again.')
                else:
                    #Adds the values to history
                    operations.append(val)
                    arguements.append(x_value)
                    break
    #Natural log
    elif val == '7':
        while True:
            x_value = input('Enter a number for natural log function (Bigger than 0): ')
            try:
                x_value = float(x_value)
            except ValueError:
                print('Invalid arguement. Should be bigger than 0 please try again.')
            else:
                try:
                    ln_function(x_value)
                except ValueError:
                    print('Invalid arguement. Should be bigger than 0 please try again.')
                else:
                    #Adds the values to history
                    operations.append(val)
                    arguements.append(x_value)
                    break
    elif val == '8':
        while True:
            x_value = input('Enter a number for square root function (Equal to or bigger than 0): ')
            try:
                x_value = float(x_value)
            except ValueError:
                print('Invalid arguement. Should be equal to or bigger than 0 please try again.')
            else:
                try:
                    sqrt_function(x_value)
                except ValueError:
                    print('Invalid arguement. Should be equal to or bigger than 0 please try again.')
                else:
                    #Adds the values to history
                    operations.append(val)
                    arguements.append(x_value)
                    break
    elif val == '9':
        while True:
            x_value = input('Enter a number for factorial function (Equal to or bigger than 0): ')
            try:
                x_value = float(x_value)
            except ValueError:
                print('Invalid arguement. Should be equal to or bigger than 0 please try again.')
            else:
                try:
                    factorial_fuction(x_value)
                except ValueError:
                    print('Invalid arguement. Should be equal to or bigger than 0 please try again.')
                else:
                    #Adds the values to history
                    operations.append(val)
                    arguements.append(x_value)
                    break
    elif val == '10':
        print(len(operations))
        while operations:
            print('Operation: ' + str(operations.pop()) + ' and arguement: ' + str(arguements.pop()))
    else:
        print(val + ' is not a correct value. Please try again')

#Printing the history of arguements prints in most recent to first order
for x in operations:
    print('Operation: ' + str(operations.pop()) + ' and arguement: ' + str(arguements.pop()))
