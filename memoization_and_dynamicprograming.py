#####################factorial
# def fac(n):
#   if n<=0:
#       return (1)

#   else:
#        return (n*fac(n-1))   

# print(fac(4))

#########################fibonacci

def fib(n):
    if n==0 or n==1:
        value=n
    else:
        value=fib(n-1)+fib(n-2)

    return (value)        


print(fib(2))    