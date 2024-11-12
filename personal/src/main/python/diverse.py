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
    

testvariable = (300,"stairs")
tupleTest(testvariable)