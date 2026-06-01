from collections import defaultdict
count_324=defaultdict(int)
count_5184=defaultdict(int)
count_0=defaultdict(int)
pairs_324=set()
pairs_5184=set()
pairs_0=set()
def oessp_stats(a):
    seen=set()
    first_pair=None
    while True:
        if a==324:
            if first_pair is not None:
                count_324[first_pair]+=1
                pairs_324.add(first_pair)
                return
        if a==5184:
            if first_pair is not None:
                count_5184[first_pair]+=1
                pairs_5184.add(first_pair)
                return
        if a==0:
            if first_pair is not None:
                count_0[first_pair]+=1
                pairs_0.add(first_pair)
            return
        if a in seen:
            return
        seen.add(a)
        sum_even=0
        sum_odd=0
        o=a
        while o!=0:
            d=o%10
            o=o//10
            if d%2==0:
                sum_even+=d
            else:
                sum_odd+=d
        if first_pair is None:
            first_pair=(sum_even,sum_odd)
            a=(sum_even*sum_odd)*(sum_even*sum_odd)
for i in range(88999999,100000000):
    oessp_stats(i)
print("\ntop pairs leading to 324")
for pair, cnt in sorted(count_324.items(), key=lambda x:-x[1]):
    print(pair, "->", cnt)
print("\ntop pairs leading to 5184")
for pair, cnt in sorted(count_5184.items(),key=lambda x:-x[1]):
    print(pair, "->", cnt)
print("\ntop pairs leading to 0")
for pair, cnt in sorted(count_0.items(),key=lambda x:-x[1]):
    print(pair, "->", cnt)
common_pairs = pairs_324 & pairs_5184 & pairs_0
print("common pairs include")
print(common_pairs)
                    
