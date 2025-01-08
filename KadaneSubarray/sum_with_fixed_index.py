import random

random.seed(12345)

# O(n ^ 2)
def sum_variety_subarray_bruteforce(numbers):    
    variety = set()
    
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            s = sum(numbers[i: j+1])
            variety.add(s)
                
    return variety
    
def sum_variety_subarray_linear(numbers, idx):
    # every call for O(n):
    l1,_,_ = opt_subarray_kadane(numbers[:idx], mode='min')
    l2,_,_ = opt_subarray_kadane(numbers[:idx], mode='max')

    r1,_,_ = opt_subarray_kadane(numbers[idx+1:], mode='min')
    r2,_,_ = opt_subarray_kadane(numbers[idx+1:], mode='max')

    m1,_,_ = opt_subarray_pinned(numbers, idx, mode='min')
    m2,_,_ = opt_subarray_pinned(numbers, idx, mode='max')
    #
    
    L = set(range(l1, l2+1))
    R = set(range(r1, r2+1))
    M = set(range(m1, m2+1))
    
    return (L.union(R)).union(M)
    
def opt_subarray_bruteforce(numbers, fixed_index, mode='max'):
    best_l, best_r = -1, -1
    sgn = {'max': 1, 'min': -1}
    best_sum = sgn[mode] * float('-inf')
    #print(best_sum)
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            s = sum(numbers[i: j+1])
            
            if sgn[mode] * (best_sum - s) <= 0 and (i <= fixed_index and j >= fixed_index):
                best_sum = s
                best_l, best_r = i, j
                
    return best_sum, best_l, best_r
    
def opt_subarray_kadane(numbers, mode='max'):
    current_sum, sgn = 0, {'max': 1, 'min': -1}
    l, r, best_l, best_r = -1, -1, -1, -1
    best_sum = sgn[mode] * float('-inf')
        
    for i in range(0, len(numbers)):
        x, r = numbers[i], i
        
        if sgn[mode] * (x - (current_sum + x)) >= 0:
            current_sum, l, r = x, i, i
        else:
            current_sum, r = current_sum + x, i
            
        if sgn[mode] * (best_sum - current_sum) < 0:
            best_sum = current_sum
            best_l, best_r = l, r
            
    return best_sum, best_l, best_r
    
# answer the question what is the best subarray sum,
# including numbers[fixed_index] for O(n)
def opt_subarray_pinned(numbers, fixed_index, mode='max'):  
    prefix_sums, s, best_l, best_r = [0], 0, -1, -1
    sgn = {'max': 1, 'min': -1}
    
    for i in range(0, len(numbers)):
        if i == fixed_index:
           s += 0
        else:
           s += numbers[i]
        prefix_sums.append(s)
    
    best_sum_l = sgn[mode] * float('-inf')
    
    for i in range(0, fixed_index):   
        candidate = prefix_sums[fixed_index] - prefix_sums[i]
        if sgn[mode] * (candidate - best_sum_l) > 0:
            best_sum_l = candidate
            best_l     = i
        
    best_sum_r = sgn[mode] * float('-inf')
    
    for i in range(fixed_index+1, len(numbers)):
        candidate = prefix_sums[i+1] - prefix_sums[fixed_index]    
        if sgn[mode] * (candidate - best_sum_r) > 0:
            best_sum_r = candidate
            best_r     = i
                
    best_sum = numbers[fixed_index]

    if sgn[mode] * best_sum_l > 0:
        best_sum += best_sum_l
    else:
        best_l = fixed_index
        
    if sgn[mode] * best_sum_r > 0:
        best_sum += best_sum_r
    else:
        best_r = fixed_index
        
    return best_sum, best_l, best_r
    
tests = 2001

for t in range(tests):
    n = 150
    a = []

    for i in range(0, n):
        r = random.randint(0, 1)
        a.append(2*r-1)
    
    idx = n // 2
    a[idx] = 1000
    
    print(f'Test {t}')
    print(a)
    
    v1=sum_variety_subarray_bruteforce(a)
    v2=sum_variety_subarray_linear(a, idx)

    print(v1)
    print(v2)
    
    if(v1 != v2):
        print('Fail.')
        break
        
    '''s1, l1, r1 = opt_subarray_bruteforce(a, idx, 'min')
    s2, l2, r2 = opt_subarray_pinned(a, idx, 'min') 
    
    print(s1, l1, r1)
    print(s2, l2, r2)
    
    print('\n')
    
    if(s1 != s2):
        print('Fail.')
        break
        
    '''
