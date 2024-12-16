#Happy number or not
def HappyNum():
    num=int(input("enter a number:"))
    sum=0
    while(num!=0):
        ld=num%10
        sq=ld**2
        sum+=sq
        num//=10
        if(num==0):
            if(sum==1 or sum==4):
                if(sum==1):
                    print("happy number")
                else:
                    print("unhappy number")
            else:
                num=sum
                sum=0
HappyNum()
