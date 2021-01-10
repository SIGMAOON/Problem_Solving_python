def fibo(n):
    fn = 0
    if n == 0:
        fn = 0
    elif n == 1:
        fn = 1
    else:
        fn = fibo(n-1) + fibo(n-2) 
    return fn

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2) 


