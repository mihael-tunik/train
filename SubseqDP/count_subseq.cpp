#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

/* Let dp[i][j] be the number of ways to extract t_0..{j-1} from s_0..{i-1}

 - 1) you can always extract empty prefix the only way from any s_1..j:
      - dp[i][0] == 1
 - 2) initialize first row dp[0][j] by zeros for convenience
      - dp[0][j] == 0 for j from 1 to m
 - 3) dp[i+1][j+1] is 
      - number of ways to extract t_0..j from smaller prefix dp[i][j+1]
      - if s[i] == t[j] we can add number of t_0..{j-1} (that is dp[i][j])

 - Answer: dp[n][m] */
int count_subseq(vector <int> &s, vector <int> &t){
    int n = s.size(), m = t.size();
    vector <vector <int>> dp(n + 1);
    
    for(int i = 0; i < n + 1; ++i)
        dp[i].resize(m + 1);
    
    dp[0].assign(m + 1, 0);  
    for(int i = 0; i < n + 1; ++i)
        dp[i][0] = 1;
    
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            dp[i+1][j+1] = dp[i][j+1] + (s[i] == t[j]) * dp[i][j];
            /*if(s[i] == t[j])
                dp[i+1][j+1] = dp[i][j+1] + dp[i][j];
            else
                dp[i+1][j+1] = dp[i][j+1];*/
    return dp[n][m];
}

int count_subseq_naive(vector <int> &s, vector <int> &t){
    int n = s.size(), m = t.size(), count = 0;

    vector <int> chosen(n, 0);
    fill(chosen.begin(), chosen.begin() + m, 1);
    
    do {
       int flag = 1;
       for (int i = 0, j = 0; i < n; ++i)
           if (chosen[i] && s[i] != t[j++])
               flag = 0;
       count += flag;
    } while(prev_permutation(chosen.begin(), chosen.end()));

    return count;
}

void print_array(vector <int> v){
    int vs = v.size();
    for(int i = 0; i < vs; ++i)
        printf("%i%c", v[i], (i < vs-1) ? ' ' : '\n');
}

int main(void){
    int n = 12, m = 5, tests = 200;
    vector <int> s(n), t(m);
    
    for(int k = 0; k < tests; ++k){
        for(int i = 0; i < n; ++i)
             s[i] = rand() % 2;

        for(int j = 0; j < m; ++j)
             t[j] = rand() % 2;
        
        print_array(s);
        print_array(t);

        int r1 = count_subseq(s, t), r2 = count_subseq_naive(s, t);
        printf("dp result: %i, check: %i\n", r1, r2);
        
        if(r1 != r2){
            printf("Test failed.\n");
            return -1;
        }
    }
    return 0;
}
