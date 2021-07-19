def inputInt(msg="Input an integer value: ", errormsg=" is not an integer number", maxval=None, minval=None):
    loop = True
    while loop:
        valid = True
        usrinput = input(msg)
        try:
            val = int(usrinput)
            if maxval == None and minval == None:
                loop = False
            else:
                if maxval != None:
                    if val > maxval:
                        valid = False
                        print(usrinput, " is higher than ", str(maxval))
                if minval != None:
                    if val < minval:
                        valid = False
                        print(usrinput, " is smaller than ", str(minval))
                if maxval == minval or maxval < minval:
                    valid = False
                    print(str(maxval), " can't be smaller than ", (minval))
                if valid == True:
                    loop = False
        except ValueError:
            print(usrinput, errormsg)
    return val

def inputFlo(msg="Input a float value: ", errormsg=" is not a decimal number"):
    loop = True
    while loop:
        usrinput = input(msg)
        try:
            val = float(usrinput)
            loop = False
        except ValueError:
            print(usrinput, errormsg)
    return val