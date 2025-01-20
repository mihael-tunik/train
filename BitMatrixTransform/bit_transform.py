def extract_bit_component(M, k):
    n, mask = len(M), 2 ** k
    Mb = []
    
    for i in range(n):
        row = []
        
        for j in range(n):
            bit = 1 if (M[i][j] & mask) > 0 else 0 
            row.append(bit)
            print(bit, end='')
            
        print('')
        Mb.append(row)    
    return Mb    

color, cycle = [], False

def dfs(G, v):
    global cycle        
    color[v] = 1
    
    for u in G[v]:
        if color[u] == 1: # path to grey vertice 
            print('There is a cycle.')
            cycle = True
        else:
            dfs(G, u)
    color[v] = 2
    
A = [[0, 1, 0], [0, 1, 1], [1, 1, 1]]
B = [[1, 1, 0], [0, 0, 0], [1, 1, 1]]

no_cycles = True
n = len(A)

for b in range(0, 5):
    Ab = extract_bit_component(A, b)
    Bb = extract_bit_component(B, b)
    
    print(f'for {b} bit matrices will be: ')
    
    print('\n', Ab, '\n', Bb, '\n')
    
    G_ops = [[] for i in range(2*n)]
    # n vertices be like     : change row 1 to 0's , ..., change row n to 0's
    # then n vertices be like: change col 1 to 1's , ..., change col n to 1's
    need_to_visit = []
    
    # fill G
    for i in range(n):
        for j in range(n):
            if Bb[i][j] == 0: # logic is ~ you need to set i'th row to 0's after setting j'th col to 1's
                G_ops[n + j].append(i)
            if Bb[i][j] == 1: # logic is ~ you need to set j'th col to 1's after setting i'th row to 0's
                G_ops[i].append(n + j)
                
            if Ab[i][j] == 0 and Bb[i][j] == 1:
                need_to_visit.append(n + j)
                
            if Ab[i][j] == 1 and Bb[i][j] == 0:
                need_to_visit.append(i)
                
    
    # reduce duplicates
    for i in range(len(G_ops)):
        G_ops[i] = list(set(G_ops[i])) 
    need_to_visit = list(set(need_to_visit))
    #
    
    print('G is: ', G_ops)
    print('need to visit: ', need_to_visit)
    
    cycle = False
    
    for v in need_to_visit:
        color = [0 for i in range(2*n)]
        dfs(G_ops, v)
        
        if cycle is True:
            break
    
    if cycle is True:
        no_cycles = False
        break
        
        
if no_cycles is True:
    print('Yes')
else:
    print('No')
    
