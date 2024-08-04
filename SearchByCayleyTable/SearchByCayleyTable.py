from copy import deepcopy
from itertools import permutations, product
from tqdm import tqdm

def apply(x, y):
    res = []
    for i in range(0, len(y)):
        res.append(y[x[i]-1])
    return tuple(res)

def SearchByCayleyTable(generators):
    G = set()
    new_elements = set()
    
    print('Generators:')

    for g in generators:
        G.add(g)
        new_elements.add(g)
        print(g)
    
    print('\nStart bruteforce:\n')
       
    while len(new_elements) > 0:
        tmp = set()
        
        for u, v in product(G, new_elements):
            g = apply(u, v)            
            if not g in G:
                tmp.add(g)      
        
        for u, v in product(new_elements, G):
            g = apply(u, v)            
            if not g in G:
                tmp.add(g)    
        
        new_elements.clear()
        new_elements = tmp
        
        for w in new_elements:
            G.add(w)
            
        print('New elements in G:', len(new_elements))
        print('G is now size of ', len(G), '\n')
    
    #print('Full G is: ')
    #for g in G:
    #    print(g)
        
    print('Size: ', len(G) )
    return G

def GeneratePermutations(identity):
    symmetry_group = set()
    backward_hash_table = {}

    for i, p in enumerate(permutations(identity)):
        symmetry_group.add(p)
        backward_hash_table[p] = i
    
    return symmetry_group, backward_hash_table
    
def ShowCayleyTable(G):
    for u in G:
        for v in G:
            m = apply(u, v)
            p_number = backward_hash_table[m]
            print(f'{p_number:3d}', end=' ')
        print()
    
def GenerateCosets(G, symm_G, coset_type):
    cosets = []
    print(f'Computing {coset_type} cosets')
    
    for g in tqdm(symm_G):
        h_test, new_coset = min(G), True
        
        if coset_type == 'right':
            m_test = apply(h_test, g)
        elif coset_type == 'left':
            m_test = apply(g, h_test)
           
        for gc in cosets:
            if m_test in gc:
                new_coset = False
                break
    
        if new_coset: 
            G_coset = set()
        
            for h in G:
                if coset_type == 'right':
                    m = apply(h, g)
                elif coset_type == 'left':
                    m = apply(g, h)
            
                G_coset.add(m)

            cosets.append(G_coset)
        
    print(f'Number of {coset_type} cosets (G, symm_G): {len(cosets)}')
    return cosets
    
generators = [(3,2,1,7,5,4,6,8), (1,4,2,3,5,6,7,8)]
# [(1,2,3,5,4), (1,4,5,3,2)]                                               # 8 
# [(3,2,1,7,5,4,6,8), (1,4,2,3,5,6,7,8)]                                   # 720
# [(3,2,1,4,5,6,7,8,9,10), (1,3,2,4,5,6,7,8,10,9), (10,5,6,8,3,1,7,4,9,2)] # 10080, slow

G = SearchByCayleyTable(generators)

identity = tuple(range(1, len(generators[0])+1))
symm_G, backw_ht = GeneratePermutations(identity)

GenerateCosets(G, symm_G, coset_type = 'right')
