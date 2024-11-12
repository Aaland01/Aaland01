
def simpleFibo(n):
    """A short fibo as possible with only using two variables, nothing else

    Args:
        n (int): The requested fibonacci number, indexed at 1. Limited to [1,499] for no particular reason
    """
    if n<=0 or n>500 or not isinstance(n, int):
        print("Insufficient parameter")
        return 0
        
    firstnum = 0
    nextnum = 1
    
    for i in range(n-1):
        firstnum, nextnum = nextnum, firstnum + nextnum
        
    print(f"Fibo number {n}: {firstnum}")
    print(f"  -> next is {nextnum}")
    return firstnum

def matrix_fibonacci(n):
    """Matrix calculating fibonacci generator, O(lgn). Modified to index at 1 instead of 0

    Args:
        n (int): Index of fibonacci number

    Returns:
        int: The requested fibonacci number
    """
    if n <= 0 or n > 500 or not isinstance(n, int):
        print("Insufficient parameters")
        return 0
    if n == 1 : 
        print(f"[MATRIX] Fibonacci number 1: 0")
        return 0
    
    fiboMatrix = [[1, 1], [1, 0]]
    
    def matrix_power(fiboMatrix, n):
        if n == 0 or n == 1:
            return

        helper = [[1, 1], [1, 0]]
        matrix_power(fiboMatrix, n // 2)
        fiboMatrix = multiply(fiboMatrix, fiboMatrix)

        if n % 2 != 0:
            fiboMatrix = multiply(fiboMatrix, helper)

    matrix_power(fiboMatrix, n - 2)
    result = fiboMatrix[0][0]
    print(f"[MATRIX] Fibonacci number {n}: {result}")
    return result

def multiply(mat1, mat2):  
    top_L = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    top_R = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    bot_L = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    bot_R = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    mat1[0][0], mat1[0][1] = top_L, top_R
    mat1[1][0], mat1[1][1] = bot_L, bot_R
    return mat1

# Regularly using loop

def fibonacci(n):
    """Older first attempt. Generates and prints the n'th fibonacci number
    Ask for: 1, 2, 3, 4, 5, 6, ...
    Receive: 0, 1, 1, 2, 3, 5, ...
    
    Args:
        n (int): Fibonacci number to select in sequence
    """
    if n>200 or n<=0:
        print(f"Insufficient argument for Fibonacci number: {n}")
        return
    # initialization
    sequence = [0,1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    print(f"Final sequence: {sequence}")
    print(f"Fibonacci number {n}: {sequence[n-1]}")
    
def recursiveFibonacci(n, sequence=[0,1]):
    """Generates and prints the n'th fibonacci number, recursively.
    Allows initating other fibonacci starter-variants.

    Args:
        n (int): Fibonacci number to select in sequence,
        sequence (list): Default value of [0,1]. Allows initating other fibonacci variants.
        
    """
    if(not isinstance(sequence,list) or not sequence):
        print(f"Insufficient list:{sequence}")
        return
    elif (n<=0 or n>200):
        print(f"Insufficient argument for Fibonacci number: {n}")
        return
    if len(sequence) >= n:
        print(f"Final sequence: {sequence}")
        print(f"Fibonacci number {n}: {sequence[n-1]}")
        return
    sequence.append(sequence[-1] + sequence[-2])
    return recursiveFibonacci(n, sequence)
  
def recursiveFibonacci2(n):
    """ Alternative recursive method with internal recursive method, decreasing redundant checks in recursion.
    Also prevents using default argument for the initial sequence. 

    Args:
        n (int): Fibonacci number to select in sequence,
        
    """
    if (n<=0 or n>200):
            print(f"Insufficient argument for Fibonacci number: {n}")
            return
    sequence=[0,1]
    def fibonacci(sequence,n):
        if len(sequence) >= n:
            print(f"Final sequence: {sequence}")
            print(f"Fibonacci number {n}: {sequence[n-1]}")
            return sequence[n-1]
        sequence.append(sequence[-1] + sequence[-2])
    return fibonacci(n, sequence)    
    
n = 14
matrix_fibonacci(n)
# fibonacci: 
# fibonacci(14)         # Returns --- 233
#recursiveFibonacci(5)  # Returns --- 3
#simpleFibo(n)          # Returns --- 233