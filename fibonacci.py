def fib(n): 
    if n > 0:
        if n == 1 or n == 2: 
            return n 
        else: 
            return(fib(n-1) + fib(n-2))

def factorial(n):
    if n== 1:
        return 1
        
    return n * factorial(n-1)   

    

