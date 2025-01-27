from count_coordered_pairs import count_coordered_pairs_with_fenwick, coordered_pairs
    
def count_good_arrays(a):
    n, cnt = len(a), 0

    for i in range(0, n):
        for j in range(i, n):
            sub_a = a[i: j+1]
            sub_a = sorted(sub_a)
            m = len(sub_a)
            
            if sub_a[(m-1)//2] == sub_a[m//2]:
                cnt += 1

    return cnt
    

def count_good_arrays_fast(a):
    ans = 0
    M = max(a)
    
    a_mod = [2*M] + a
    a = a_mod # :(
    
    n = len(a)
    S = n
        
    for x in range(0, M+1):
        #print('x is ', x)
        p, q = [], []
        cnt_leq, cnt_geq = 0, 0
        
        for i in range(0, n):
            if a[i] <= x:
                cnt_leq += 1
            if a[i] >= x:
                cnt_geq += 1                
            p.append( 2 * cnt_leq - i + S )
            q.append( 2 * cnt_geq - i + S )
        
        #print(p)
        #print(q)
        
        arrays_with_x = count_coordered_pairs_with_fenwick(p, q)
        #print('new subarrays', arrays_with_x)
        ans += arrays_with_x
        
    return ans
    
a = [0,1,2,3,5,4,6,7,8,8,5,3,4,4,2,1]

print('res_1: ', count_good_arrays(a))
print('res_2: ', count_good_arrays_fast(a))
print('')
