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
    
defaultParam(0)
defaultParam("")