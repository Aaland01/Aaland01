def perfectShuffle(list):
    listSize = len(list)
    newList = []
    for i in range(listSize//2):
        newList.append(list[i])
        newList.append(list[listSize//2 + i])
        repeat -= 1
    return newList

def defaultParam(check=True):
    print("True" if check else "False")
    
def tupleTest(tuple):
    variable1=0
    variable2=1
    variable1, variable2 = tuple
    print(f"{variable1}, and {variable2}")


def australianToNOK(amount):
    perMonth = (amount * 52) / 12
    NOK = perMonth * 7.1
    print(NOK)
    
    
australianToNOK(575/2)


def timeConverterNOK(nokTime):
    """ Noktime format: nnnn, i.e. 1400 means 2pm"""
    australianAhead = 9
    hour = str(nokTime)[:2]
    mins = str(nokTime)[2:4]
    print(f"Hour: {hour}")
    print(f"Minutes: {mins}")
    australianTime = int(hour) + australianAhead
    print(f"Time: {australianTime}")
    if (australianTime - 24 >= 0):
        australianTime = australianTime - 24
    print(str(australianTime) + mins)
    
timeConverterNOK(1630)

def timeConverterAUS(ausTime):
    """ Noktime format: nnnn, i.e. 1400 means 2pm"""
    norBehind = -9
    hour = str(ausTime)[:2]
    mins = str(ausTime)[2:4]
    print(f"Hour: {hour}")
    print(f"Minutes: {mins}")
    norTime = int(hour) + norBehind
    print(f"Time: {norTime}")
    if (norTime - 24 >= 0):
        norTime = norTime - 24
    print(str(norTime) + mins)
    
timeConverterAUS(1100)
    