import time
import random
import numpy as np

from collections import defaultdict
import matplotlib.pyplot as plt

#from MedianTwoSorted import median_two_sorted_log, median_two_sorted_linear
from KOrderTwoSorted import median_two_sorted_log, median_two_sorted_linear

random.seed(23451)

n_tests = 10000

time_data = defaultdict(list)
sizes = [30, 50, 100, 150, 200]

for size in sizes:
    for test in range(0, n_tests):
        n1, n2 = size, size
     
        x = sorted(list(np.random.randint(1000000, size=n1)) ) #random.sample(range(0,100000), n1))
        y = sorted(list(np.random.randint(1000000, size=n1)) ) #random.sample(range(0,100000), n2))
    
        print(f'Test {test + 1}/{n_tests}')

        start = time.time()
        m1 = median_two_sorted_log(x, y)
        end   = time.time()
    
        time_data[ ('my_log', size) ].append( end-start )    
    
        start = time.time()
        m2 = median_two_sorted_linear(x, y)
        end   = time.time()
        
        time_data[ ('linear', size) ].append( end-start )   
        
    
y_my_log = []
y_linear = []

for size in sizes:
    y_my_log.append(np.mean(time_data[ ('my_log', size) ]))
    y_linear.append(np.mean(time_data[ ('linear', size) ]))
    
plt.plot(sizes, y_my_log, 'o-', color='green', label='my_log')
plt.plot(sizes, y_linear, 'o-', color='blue', label='linear')

plt.legend()
plt.grid(True) 
plt.xlabel('Size n of each sorted array')
plt.ylabel('Time [s]')
plt.tight_layout()

plt.savefig('performance.svg')


