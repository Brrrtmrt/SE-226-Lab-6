
import sys
result=lambda x,n:(-1**n)*(x**(2*n+1))/(factorial(2*n+1))
def factorial(x):
    if x<=1:
        return 1
   
    return x*factorial(x-1)



def sine_x(x,n):
    calc=0.0
    rad=x*0.01745329
    for i in range(0,n):
        calc+=result(x,i)
    return calc

x=0
def func(n):
    """calculates sum until 1/n

    Args:
        n (int): 
    """
    global x
    if n==0:
        return
    x+=1/n
    return func(n-1)



