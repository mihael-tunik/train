from collections import defaultdict
import random

def count_zero_subarrays_bruteforce(a):
    n, count = len(a), 0

    for i in range(n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s += a[k]
            if s == 0:
                count += 1
                print(f'Has zero sum ({i}, {j}): ', a[i: j+1])
    return count

def count_zero_subarrays_hashmap(a):
    n, count, s = len(a), 0, 0
    sums_map = defaultdict(int)
    sums_map[0] = 1

    for i in range(n):
        s += a[i]
        count += sums_map[s] 
        # sums_map[s] stores number of prefix subarrays ending before i with sum equal to s 
        # [   ]{....}i each corresponds to subarray with sum s-s = 0
        sums_map[s] += 1 # increase counter

    return count

def count_zero_subarrays_sum_pairs(a):
    n, count, s = len(a), 0, 0
    sums_map = defaultdict(int)

    for i in range(n):
        s += a[i]
        sums_map[s] += 1 # increase counter

    for k, v in sums_map.items():
        x = sums_map[k]
        if x > 1:
            count += x * (x-1) // 2
    
    count += sums_map[0]

    return count


L = 100
random.seed(123)
test = [random.randint(-1,1) for i in range(L)]

print(test)

print(count_zero_subarrays_bruteforce(test))
print(count_zero_subarrays_hashmap(test))
print(count_zero_subarrays_sum_pairs(test))
