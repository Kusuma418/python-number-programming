#automorphic number
def automorphic():
    num=int(input("enter a number:"))
    sq=num**2
    c=0
    while(num!=0):
        ld=num%10
        sq_ld=sq%10
        if(ld!=sq_ld):
            c+=1
            break
        num//=10
        sq//=10
    if(c>0):
        print("given number is not automorphic number")
    else:
        print("given number is automorphic number")
automorphic()
        
        
