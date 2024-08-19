from copy import deepcopy
from itertools import permutations, product

from Utils import mult, inv

# computes every possible pair
# (orbit element j for initial index i, pij)
# where pij permutation which can be expressed in terms of s1, s2, ..., sl in S
# and maps position i-th position to j-th
# pij form transversal for cosets of stabilizer of i
def BuildSchreierTree(i, S, orbit):
    for g in S:
        if g[i-1] not in orbit:
            orbit[g[i-1]] = mult(g, orbit[i])
            BuildSchreierTree(g[i-1], S, orbit)
            
def BuildSchreierGenerators(S, orbit):
    S_gen = set()
    for g in S:
        for u in orbit:
            schreier_generator = mult(inv(orbit[g[u-1]]), g, orbit[u])
            S_gen.add(schreier_generator) 
    return S_gen

def SimsFilter(S, n):    
    u = [[-1]*n] * n # only for j > i

    for g in S:
        h = g        
        for i in range(1, n+1):
            j = h[i-1]
            if j > i:
                if u[i-1][j-1] == -1:
                    u[i-1][j-1] = h
                    break
                else:
                    h = mult(inv(u[i-1][j-1]), h)
    
    S_reduced = set()
    
    for i in range(0, n):
        for j in range(0, n):
            if u[i][j] != -1:
                S_reduced.add(u[i][j])

    return S_reduced
    
def SchreierSims(S):
    n = len(S[0])    
    ans, group_order, i = [], 1, 1
    
    while len(S) != 0 and i <= n:
        orbit = {i : tuple(range(1, n+1))}
        BuildSchreierTree(i, S, orbit)
       
        R = [orbit[j] for j in orbit]
        S = SimsFilter(BuildSchreierGenerators(S, orbit), n)
        
        ans += [R] # that is right transversals for G{i} in G{i-1}
        group_order, i = group_order * len(R), i + 1 
        
    return ans, group_order
