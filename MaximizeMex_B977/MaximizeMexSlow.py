a = [0, 1, 0, 0, 3, 3, 2]
b = 2
 
a_sorted = sorted(a)
a_sorted_bins = [[] for i in range(b)]

for i in range(len(a)):
    a_sorted_bins[a[i] % b].append(a[i])

for j in range(b):
    a_sorted_bins[j] = sorted(a_sorted_bins[j], reverse=True)

print(a_sorted_bins)
print(a_sorted)

cnt = 0
used = [False] * len(a)
included = True

while(included):    
    #print('trying to include: ', cnt)
    included = False
    
    #print(used)
    for i in range(len(a_sorted)):
        if used[i] is False:        
            d = cnt - a_sorted[i]
 
            #print('a: ', a_sorted[i], 'delta: ', d)
    
            if d == 0 or (d > 0 and d % b == 0):
                used[i] = True
                included = True
                
                #print(f'{cnt} included!')
                
                cnt += 1                
                break     

print(cnt)

