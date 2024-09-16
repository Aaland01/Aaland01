

# Regularly using loop
def fibonacci(n):
    if n>20 or n<0:
        print("nope, too large a number")
        return
    fibo = [0,1]
    for i in range(n):
        a = fibo[-2]
        print(f"{i}\na: {a}")
        b = fibo[-1]
        print(f" + {b}")
        fibo.append(a+b)
        print(" ------------------------------------------")
    print(f"Final sequence: {fibo}")
    
def fibonacciRecursive(n, numbers=[0,1]):
    if(not isinstance(numbers,list) or not numbers):
        print(f"Unsatisfying list:{numbers}")
        return
    elif (n<0 or n>25):
        print("Counter error.")
        return
    if n==0:
        print(f"Final list: {numbers}")
        return
    a = numbers[-2]
    print(f"   {a}")
    b = numbers[-1]
    print(f" + {b}")
    numbers.append(a+b)
    print(f"{n}: ------------------------------------------")
    return fibonacciRecursive(n-1, numbers)

fibonacciRecursive(20)
    
    
    
    
    