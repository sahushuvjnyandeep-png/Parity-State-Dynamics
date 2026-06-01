#program file 1
#This the plain implementation and the root program-

pro=1
sum1=0#for accumalating even digits
sum2=0#for accumalating odd digits
#checking all finite values between 1 and 10^10
for i in range(0,100000000):
    a=i;
    while(a!=0):#extracting digits
        b=a%10;
        a=a//10;
        if (b%2==0):
            sum1+=b
        else:
            sum2+=b
    p=sum1*sum1#taking square of the sum of even digits in variable p
    q=sum2*sum2#taking square of the sum of odd digits in variable q
    pro=p*q#product of the squares of the sum of odd digits and sum of even digits
    if (pro==i):
        print(i)#display
    pro=1
    sum1=0#re-intialization
    sum2=0
