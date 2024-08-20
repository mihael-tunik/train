from SchreierSims import SchreierSims
from Utils import mult, inv

# pocket cube group
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
