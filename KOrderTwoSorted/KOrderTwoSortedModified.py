import numpy as np

def k_order_and_next_two_sorted_binsearch(x, y, n, n1, n2, h):
    l, r, prev_state, state = 0, n1-1, (0, n1-1), (-1, -1)
    while prev_state != state: # is there (l, r) update?    
        m = (l + r)//2        
        pivot, f_m = x[ m ], h-m              
        if f_m > n2: # check boarder cases for f_m values 
            l = m        
        elif f_m == n2:        
            if x[ m ] >= y[ n2 - 1 ]:
                return x[ m ], x[ m + 1 ] # this fail only if h == n1 + n2 - 1
            else: 
                l = m if l != r-1 else r                
        elif f_m < 0:
            r = m                   
        elif f_m == 0:
            if x[ m ] <= y[ 0 ]:
                tmp = y[0] if m >= n1-1 else x[ m + 1 ]                    
                return x[ m ], min(tmp, y[ 0 ])
            else:
                r = m                     
        else: # main part
            if x[ m ] >= y[ f_m - 1 ] and x[ m ] <= y[ f_m ]:                
                tmp = y[ f_m ] if m >= n1-1 else x[ m + 1 ]                
                return x[ m ], min(tmp, y[ f_m ])                
            elif x[ m ] < y[ f_m - 1 ]:                
                l = m if l != r-1 else r # don't repeat this at home                
            elif x[ m ] > y[ f_m ]:    
                r = m                
        prev_state, state = state, (l, r)
        
def find_k_order_two_sorted_modified(x, y, n1, n2, k):
    if r := k_order_and_next_two_sorted_binsearch(x, y, n1 + n2, n1, n2, k ): 
       return r
    return k_order_and_next_two_sorted_binsearch(y, x, n1 + n2, n2, n1, k ) 

def median_two_sorted_log_modified(x, y):
    n1, n2, n = len(x), len(y), len(x) + len(y)    
    lm, rm = find_k_order_two_sorted_modified(x, y, n1, n2, (n - 1)//2) 
    if (n1 + n2) % 2 == 1:
       return lm
    else:       
       return (lm + rm) / 2
