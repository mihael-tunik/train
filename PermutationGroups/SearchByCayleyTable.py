from copy import deepcopy
from itertools import permutations, product
from tqdm import tqdm

from SchreierSims import SchreierSims
from Utils import mult, inv

# the most bruteforce solution ever
# stored for history and checks
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
        # [    G    ]
        #     [ new ]
        # . . . x x
        # . . . x x
        # . . . x x
        # x x x x x
        # x x x x x
        for u, v in product(G, new_elements):
            g = mult(u, v)            
            if not g in G:
                tmp.add(g)      
        
        for u, v in product(new_elements, G):
            #if v not in new_elements: this code is slow anyway
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

    

