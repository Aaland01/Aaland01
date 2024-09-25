

# Regularly using loop

def fibonacci(n):
    """Generates and prints the n'th fibonacci number
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
    """Generates and prints the n'th fibonacci number, recursively

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

# fibonacci: 
fibonacci(5)           # Returns --- 3
recursiveFibonacci(5)  # Returns --- 3
    
    
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
    