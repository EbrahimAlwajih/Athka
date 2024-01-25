
def fact (n):
    if n < 1:
        return 1
    else:
        return n*fact(n-1)

def print_str (s, indx) :
    if indx < len(s):
        print(s[indx])
        print_str(s, indx+1)
        

def countdown(n):
    if n <= 0:
        print("Liftoff!")
    else:
        print(n)
        countdown(n-1)

def sum_natural(n):
    if n <= 0:
        return 0
    else:
        return n+sum_natural(n-1)

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



print (fact(5))