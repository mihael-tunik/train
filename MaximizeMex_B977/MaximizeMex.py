a = [0, 1, 0, 0, 3, 3, 2]
b = 2
 
a_sorted_bins = [[] for i in range(b)]

for i in range(len(a)):
    a_sorted_bins[a[i] % b].append(a[i])

for j in range(b):
    a_sorted_bins[j] = sorted(a_sorted_bins[j], reverse=True)


cnt, included = 0, True

while(included):    
    #print('trying to include: ', cnt)
    #print('state: ', a_sorted_bins)
    
    included = False
    
    c = cnt + 1
    
    if len(a_sorted_bins[cnt % b]) > 0:
        c = a_sorted_bins[cnt % b][-1]
        
    #print('>>', c)
    
    if c <= cnt:
        included = True
        #print(f'{cnt} included!')
        a_sorted_bins[cnt % b].pop()        
        cnt += 1                
    

print(cnt)

