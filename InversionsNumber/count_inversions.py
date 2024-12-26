class FenwickTree:
    def __init__(self, n):
        self.t = [0] * n # long empty list 
        self.N = n
        
    def modify(self, i, d):
        while i < self.N:
            self.t[i] += d
            i = i | (i + 1)
            print('m')
    
    def prefix_sum(self, i):
        result = 0
        while i >= 0:
            print(f'{i} -> ', end = '')
            result += self.t[i]
            i = (i & (i + 1)) - 1
        print('.')
        return result

    def query(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

    def print(self):
        print('T: ', end='')
        for j in range(0, self.N):
            print(f' {self.t[j]:02} ', end='')
        print('\n')
        
    def show_indexes(self):
        for i in range(0, self.N): # every row corresponds to index in a[]
            print(f'{i:03} ', end='')
            for j in range(0, self.N): # every column corresponds to index in t[]
                # T[j] corresponds to sum on [j & (j + 1), j]
                if i >= j & (j + 1) and i <= j: # i : [g(j), j]
                    print('x   ', end = '')
                else:
                    print('.   ', end = '')
            print('')
        
        print('T: ', end='')
        for j in range(0, self.N):
            print(f'{j:03} ', end='')
        print('\n')
        
# O(n ^ 2)
def inversions_base(a):
    n, cnt = len(a), 0
    for i in range(0, n):
        for j in range(0, n):
            if a[i] > a[j] and i < j:
                cnt += 1
    return cnt

# O(n ^ 2)
def inversions_flag_array(a):
    n, cnt, M = len(a), 0, max(a) 
    T = [0] * (M + 1)
    for i in range(0, n):
        T[a[i]] = 1
        s = 0
        for j in range(a[i] + 1, M+1):
            s += T[j]     
        print(f's: {s}')
        cnt += s
    return cnt

# O(n log n)
def inversions_fenwick(a):
    n, cnt, M = len(a), 0, 20
    T = FenwickTree(M+1)
    T.show_indexes()
    
    T.print()
    print(a, end='\n\n')
        
    for i in range(0, n):
        print(f'modify {a[i]} (+1)')
        T.modify(a[i], 1)
        T.print()
        q = T.query(a[i] + 1, M)
        print(f'sum is {q}\n')
        cnt += q

    return cnt
    
a = [12, 8, 5, 3, 1, 2, 10, 7, 0]
print(inversions_base(a))
print(inversions_flag_array(a))
print(inversions_fenwick(a))
