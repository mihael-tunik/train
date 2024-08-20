from copy import deepcopy
from itertools import permutations, product

def mult(*p_chain):
    res = []
    for i in range(0, len(p_chain[0])):
        image = i
        # x o y = x(y(S)), rightmost first
        for p in reversed(p_chain): 
            image = p[image] - 1 
        res.append(image + 1)
    return tuple(res)
        
def inv(x):
    res = list(deepcopy(x))
    for i in range(0, len(x)):
        res[x[i] - 1] = i + 1
    return tuple(res)
    

