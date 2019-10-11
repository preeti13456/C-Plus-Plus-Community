def fib(n):
    if(n<=1):          #check for positive no. and base value is done
        return n
    return fib(n-1)+fib(n-2)
#Drive code
n = 4
print("nth the fibonacci no. is",fib(4))
