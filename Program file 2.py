#this the main file unveiling most of the things

global l ,m, counts, indicator, store
indicator=0#checker in which list to store the pair
l=[]
m=[]
num_324=[]#nums which iterates in funtion and ultimately reach 324
num_5184=[]#nums which iterates in funtion and ultimately reach 5184
num_0=[]
st=[]#pairs which form 324
nd=[]#pairs which form 5184
rd=[]
cycle_found=False
count = {0:0, 324:0, 5184:0}
def oessp(a):
    pro=1
    sum1=0
    sum2=0
    store=None
    seen=set()
    while(True):
        if a in seen:
            if a not in [0,324,5184]:
                print("cycle found at:",a)
                return True
            else:
                return False
        seen.add(a)
        o=a
        while(a!=0):#extracting
            b=a%10
            a=a//10
            if (b%2==0):
                sum1+=b
            else:
                sum2+=b
        if store is None:
            store=(sum1, sum2)
        p=sum1*sum1#taking square of the sum of even digits in variable p
        q=sum2*sum2#taking square of the sum of odd digits in variable q
        pro=p*q#product of the squares of the sum of odd digits and sum of even digits
        if (pro==o):
            if o not in m:
                m.append(o)
                if o==324:
                    indicator=1
                    st.append(store)
                elif o==5184:
                    indicator=2
                    nd.append(store)
                elif o==0:
                    indicator=3
                    rd.append(store)
                break
            else:
                count[o] += 1
                if o==324:
                    indicator=1
                    num_324.append(i)
                    st.append(store)
                elif o==5184:
                    indicator=2
                    num_5184.append(i)
                    nd.append(store)
                elif o==0:
                    indicator=3
                    num_0.append(i)
                    rd.append(store)
                break
        a=pro
        pro=1
        sum1=0#re-intialization
        sum2=0
for i in range(9999900,9999999):
    a=i
    if oessp(a):
        cycle_found=True
if not cycle_found:
    print("no non-trivial cycles found")
print("total numbers falling into",count)
print("fixed points",m)
print("pairs of 324\n",st)
print("pairs of 5184\n",nd)
print("pairs of 0\n",rd)
print("numbers ultimately reach to 324\n",num_324)
print("numbers ultimately reach to 5184\n",num_5184)
print("numbers ultimately reach to 0\n",num_0)

