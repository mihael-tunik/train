from SearchByCayleyTable import SearchByCayleyTable
from Utils import mult, inv
from Group import BuildGroupDfs

from tqdm import tqdm

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
        
def SchreierGeneratorsTest():
    S     = [(3,2,1,4,5,6,7,8,9,10), (1,3,4,2,5,6,8,7,10,9), (1,3,2,6,5,4,7,9,10,8)]
    sub_S = [(3,2,1,4,5,6,7,8,9,10), (1,3,4,2,5,6,8,7,10,9)]

    n = len(S[0])
    identity = tuple(range(1, n + 1))
    
    G, H = set(), set()
    BuildGroupDfs(identity, S, G)
    BuildGroupDfs(identity, sub_S, H)
    
    #G = SearchByCayleyTable(S)
    #H = SearchByCayleyTable(sub_S)
    left_or_right = 'right'
    G_H = GenerateCosets(H, G, coset_type = left_or_right)
    R = set()

    for coset in G_H:
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
            if left_or_right == 'right':
                schreier_generators.add(mult(rs,  inv(_rs_) ))
            else:
                schreier_generators.add(mult(inv(_rs_), rs)) #?
    print('Schreier generators for H > G: ')
    print(schreier_generators)

    H_ = SearchByCayleyTable(schreier_generators)
    if H == H_:
        print('H and H_ coincide!')

SchreierGeneratorsTest()
