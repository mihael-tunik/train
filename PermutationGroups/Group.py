from Utils import mult, inv 
import sys

sys.setrecursionlimit(12000)

def BuildGroupDfs(p, S, group):
    for g in S:
        h = mult(g, p)
        if h not in group:
            group.add(h)
            BuildGroupDfs(h, S, group)

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
