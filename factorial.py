#factorial of a digit
def fact():
    num=int(input("enter a digit:"))
    fact=1
    i=1
    while(i<=num):
        fact=fact*i
        i+=1
    print(fact,"is a factorial of",num)
fact()
    
