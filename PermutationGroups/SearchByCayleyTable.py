from copy import deepcopy
from itertools import permutations, product
from tqdm import tqdm

from SchreierSims import SchreierSims
from Utils import mult, inv

import sys

sys.setrecursionlimit(12000)

def BuildGroupDfs(p, S, group):
    for g in S:
        h = mult(g, p)
        if h not in group:
            group.add(h)
            BuildGroupDfs(h, S, group)
            
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
            g = mult(u, v)            
            if not g in G:
                tmp.add(g)      
        
        for u, v in product(new_elements, G):
            g = mult(u, v)            
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
   
def FindStabilizer(G, i):
    g_stab = set()
    for g in G:
        if g[i-1] == i:
            g_stab.add(g)
    return g_stab
    
def FindOrbit(G, i):
    orbit = set()
    for g in G:
        orbit.add(g[i-1])
    return sorted(list(orbit))
    
def GenerateCosets(H, G, coset_type):
    cosets = []
    print(f'Computing {coset_type} cosets')
    
    for g in tqdm(G):
        h_test, new_coset = min(H), True
        
        if coset_type == 'right':
            m_test = mult(h_test, g)
        elif coset_type == 'left':
            m_test = mult(g, h_test)
           
        for gc in cosets:
            if m_test in gc:
                new_coset = False
                break
    
        if new_coset: 
            H_coset = set()
        
            for h in H:
                if coset_type == 'right':
                    m = mult(h, g)
                elif coset_type == 'left':
                    m = mult(g, h)
            
                H_coset.add(m)

            cosets.append(H_coset)
        
    print(f'Number of {coset_type} cosets (H, G): {len(cosets)}')
    #print([len(item) for item in cosets])
    return cosets

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
            m = mult(u, v)
            p_number = backward_hash_table[m]
            print(f'{p_number:3d}', end=' ')
        print()
        
# tests
def SchreierGeneratorsTest():
    S     = [(3,2,1,4,5,6,7,8,9,10), (1,3,4,2,5,6,8,7,10,9), (1,3,2,6,5,4,7,9,10,8)]
    sub_S = [(3,2,1,4,5,6,7,8,9,10), (1,3,4,2,5,6,8,7,10,9)]

    G = SearchByCayleyTable(S)
    H = SearchByCayleyTable(sub_S)

    n = len(S[0])
    identity = tuple(range(1, n + 1))

    G_H = GenerateCosets(H, G, coset_type = 'right')
    R = set()

    for coset in G_H:
        # same as min
        # if identity in coset:
        #     R.add(identity)    
        R.add(min(coset))

    schreier_generators = set()

    for s in S:
        for r in R:
            rs = mult(r, s)
            _rs_ = None
            #cnt = 0
        
            for coset in G_H:
                if rs in coset:
                    _rs_ = min(coset)
                    break
                #cnt += 1
                
            #print('rs_cnt: ', cnt)
            schreier_generators.add(mult(rs,  inv(_rs_) ))
        
    print('Schreier generators for H > G: ')
    print(schreier_generators)

    H_ = SearchByCayleyTable(schreier_generators)
    if H == H_:
        print('H and H_ coincide!')

    
generators = [(1, 13,  9,  3,  23,  6,  7, 14, 10,  4, 24, 12,
              11,  5, 15, 16,  17, 18, 19, 20, 21, 22,  8,  2 ),
             (1 ,  2,  3, 14,  11,  5,  7,  8,  9, 16, 12,  6, 
              13, 18, 15, 20,  17, 22, 19, 24, 21,  4, 23, 10 ), 
             (22,  2,  3,  4,   5, 16, 21,  8,  9, 10, 11, 15,
              13, 14,  1,  7,  19, 17, 20, 18,  6, 12, 23, 24 )]

# test groups
# [(1,2,3,5,4), (1,4,5,3,2)]                                               # 8 
# [(3,2,1,7,5,4,6,8), (1,4,2,3,5,6,7,8)]                                   # 720
# [(3,2,1,4,5,6,7,8,9,10), (1,3,2,4,5,6,7,8,10,9), (10,5,6,8,3,1,7,4,9,2)] # 10080

n = len(generators[0])
#print(generators)

identity = tuple(range(1, n + 1))

R, group_order = SchreierSims(generators)
print(group_order)
