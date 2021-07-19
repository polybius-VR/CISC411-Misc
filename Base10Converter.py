from my_utils import *

def recursiveConversionIntFromBase10(convertee, base, converted=""):
    print(converted)
    if convertee > 0:
        print(convertee)
        return recursiveConversionIntFromBase10(convertee // base, base, str(convertee % base) + converted)
    else:
        return converted

def recursiveConversionFloatFromBase10(convertee, base, converted=""):
    return 0

def iterativeConversionIntToBase10(convertee, base):
    sum = 0
    i = 0
    lst = [int(i) for i in str(convertee)]
    lstLen = len(lst)
    while i < lstLen:
        print(str(lst[lstLen - (i + 1)]) + " * (" + str(base) + "^" + str(i) + ") (" + str(base ** i) + ") (" + str(lst[lstLen - (i + 1)] * base ** i) + ")")
        sum = sum + (lst[lstLen - (i + 1)] * base ** i)
        i = i + 1
    return sum

def iterativeConversionFloatToBase10(convertee, base):
    sum = 0
    i = 0
    lst = [int(i) for i in str(convertee)]
    lstLen = len(lst)
    for i in range(0, lstLen):
        print(str(lst[i]) + " * (" + str(base) + "^-" + str(i+1) + ") (" + str(base ** ((i+1)*-1)) + ") (" + str(lst[i] * (base ** ((i+1)*-1))) + ")")
        sum = sum + lst[i] * (base ** ((i+1)*-1))
    return sum


def convertCalc():
    loop = True
    while loop:
        print("Enter 0 to convert to base 10\nEnter 1 to convert from base 10\nEnter 2 to convert base 10 to Hex\nEnter 3 to convert Hex to base 10\nEnter q to exit")
        option = input()

        if option == "0":
            convertee = inputFlo("Enter the number you want to convert: ", " is an invalid input")
            base = inputInt("Enter the base of this number (2-16): ", " not an integer value", 10, 2)
            strConvertee = str(convertee).split('.', 2)
            val = iterativeConversionIntToBase10(strConvertee[0], base)
            if strConvertee[1] != "0":
                val = val + iterativeConversionFloatToBase10(strConvertee[1], base)
            print("Result: " + str(val))

        elif option == "1":
            convertee = inputFlo("Enter a base 10 number: ")
            base = inputInt("Enter the base you want to convert to: ")
            strConvertee = str(convertee).split('.', 2)
            if convertee <= 0:
                print("Error! can't convert negative numbers yet")
            else:
                val = recursiveConversionIntFromBase10(int(strConvertee[0]), base)
                if strConvertee[1] != "0":
                    val2 = recursiveConversionFloatFromBase10(int(strConvertee[1]), base)
                    print("Result: " + val + "." + str(val2))
                else:
                    print("Result: " + val)

        elif option == "2":
            pass

        elif option == "3":
            pass
        
        elif option == "q":
            loop = False
        else:
            print("Invalid option")

convertCalc()