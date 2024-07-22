import numpy as np

def k_order_two_sorted_binsearch(x, y, n, n1, n2, h):
    l, r, prev_state, state = 0, n1-1, (0, n1-1), (-1, -1)
    while prev_state != state: # is there (l, r) update?    
        m = (l + r)//2        
        pivot, f_m = x[ m ], h-m              
        if f_m > n2: # check boarder cases for f_m values 
            l = m        
        elif f_m == n2:        
            if x[ m ] >= y[ n2 - 1 ]:
                return x[ m ]
            else: 
                l = m if l != r-1 else r                
        elif f_m < 0:
            r = m                   
        elif f_m == 0:
            if x[ m ] <= y[ 0 ]:
                return x[ m ]
            else:
                r = m                     
        else: # main part
            if x[ m ] >= y[ f_m - 1 ] and x[ m ] <= y[ f_m ]:
                return x[ m ]                
            elif x[ m ] < y[ f_m - 1 ]:                
                l = m if l != r-1 else r # don't repeat this at home                
            elif x[ m ] > y[ f_m ]:    
                r = m                
        prev_state, state = state, (l, r)
    
def find_k_order_two_sorted(x, y, n1, n2, k):
    if r := k_order_two_sorted_binsearch(x, y, n1 + n2, n1, n2, k ):
       return r
    return k_order_two_sorted_binsearch(y, x, n1 + n2, n2, n1, k )

def median_two_sorted_log(x, y):
    n1, n2, n = len(x), len(y), len(x) + len(y)    
    lm = find_k_order_two_sorted(x, y, n1, n2, (n - 1)//2) 
    if (n1 + n2) % 2 == 1:
       return lm
    else:       
       return (lm + find_k_order_two_sorted(x, y, n1, n2, n//2)) / 2

def merge_two_sorted(x, y):
    l, m, result = 0, 0, []
    while l != len(x) and m != len(y):
        if x[l] < y[m]:
            result.append(x[l])
            l += 1
        else:
            result.append(y[m])
            m += 1    
    while l != len(x):
        result.append(x[l])
        l += 1    
    while m != len(y):
        result.append(y[m])
        m += 1
    return result
    
def median_two_sorted_linear(x, y):
    merged = merge_two_sorted(x, y)
    n = len(merged)    
    if n % 2 == 1:
        return merged[(n-1)//2]
    else:
        return (merged[(n-1)//2] + merged[n//2])/2
            
if __name__ == "__main__":
    np.random.seed(12345)
    n1, n2 = list(np.random.randint(1, 8, size=2))
    x = sorted(list(np.random.randint(100, size=n1)+1))
    y = sorted(list(np.random.randint(100, size=n2)+1))
    
    print(x)
    print(y) 
    
    m1 = median_two_sorted_log(x, y)
    m2 = median_two_sorted_linear(x, y)    
    print(f'{m1}=={m2}: {m1 == m2}')
