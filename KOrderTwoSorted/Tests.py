import time
import numpy as np

from KOrderTwoSorted import median_two_sorted_log, median_two_sorted_linear

np.random.seed(12345)

n_tests = 100000
passed, failed  = 0, 0
verbose = True

for test in range(0, n_tests):

    n1, n2 = list(np.random.randint(1, 8, size=2))
    x = sorted(list(np.random.randint(100, size=n1)+1))
    y = sorted(list(np.random.randint(100, size=n2)+1))
    
    m1 = median_two_sorted_log(x, y)   
    m2 = median_two_sorted_linear(x, y)
    
    if verbose:
        print(f'Test {test + 1}/{n_tests}')    
        
        print(x)
        print(y)
        
        if m1 == m2:
            print(f'OK. Get {m1}, answer was {m2}')
        else:
            print(f'Failed! Get {m1}, answer was {m2}')
    
    if m1 != m2:
        failed += 1
    else:
        passed += 1

print(f'Passed: {passed}, failed: {failed}')
