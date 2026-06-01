from collections import defaultdict

# frequency counters
count_324 = defaultdict(int)
count_5184 = defaultdict(int)

# sets to track unique pairs
pairs_324 = set()
pairs_5184 = set()


def get_first_pair(n):
    even_sum = 0
    odd_sum = 0
    
    while n != 0:
        d = n % 10
        n //= 10
        if d % 2 == 0:
            even_sum += d
        else:
            odd_sum += d
    
    return (even_sum, odd_sum)


def oessp(n):
    seen = set()
    first_pair = get_first_pair(n)
    
    while True:
        if n in seen:
            return # no non-trivial cycles
        
        seen.add(n)
        
        even_sum, odd_sum = get_first_pair(n)
        n = (even_sum * odd_sum) ** 2
        
        if n == 324:
            count_324[first_pair] += 1
            pairs_324.add(first_pair)
            return
        
        elif n == 5184:
            count_5184[first_pair] += 1
            pairs_5184.add(first_pair)
            return
        
        elif n == 0:
            return


# run
for i in range(1, 10000000):
    oessp(i)


# OUTPUTS
print("\n--- Pairs leading to 324 ---")
for pair, cnt in count_324.items():
    print(pair, "->", cnt)

print("\n--- Pairs leading to 5184 ---")
for pair, cnt in count_5184.items():
    print(pair, "->", cnt)


# common pairs
common_pairs = pairs_324 & pairs_5184

print("\n--- Common pairs ---")
print(common_pairs)
