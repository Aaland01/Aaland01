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
    
def stringReplace(string, a, b):
    '''Replaces instances of a in string with b'''
    if(isinstance(string, str) and isinstance(a, str) and isinstance(b, str)):
        print(string.replace(a,b))
    else:
        print("Input needs to be string")