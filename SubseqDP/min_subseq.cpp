#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

/* Let dp[i][j] be the minimum cost for prefixes (t_0..{j-1}, s_0..{i-1})

 - 1) you can always extract empty prefix with zero cost from any s_1..j:
      - dp[i][0] == 0
 - 2) initialize first row dp[0][j] by INFs for convenience
      - dp[0][j] == INF for j from 1 to m
 - 3) dp[i+1][j+1] can be 
      - minimal answer from smaller prefix dp[i][j+1]
      - if s[i] == t[j] we can try to include s[i] with cost[i]

 - Answer: dp[n][m] */
int min_subseq(vector <int> &s, vector <int> &t, vector <int> &cost, vector <int> &res){
    int n = s.size(), m = t.size(), INF = 1e9;
    vector <vector <int>> dp(n + 1);
    
    for(int i = 0; i < n + 1; ++i)
        dp[i].resize(m + 1);
    
    dp[0].assign(m + 1, INF);  
    for(int i = 0; i < n + 1; ++i)
        dp[i][0] = 0;
    
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < m; ++j)
            if(s[i] == t[j])
                dp[i+1][j+1] = min(dp[i][j+1], dp[i][j] + cost[i]);
            else
                dp[i+1][j+1] = dp[i][j+1];

    if(dp[n][m] >= INF)
        return INF;

    int x = n, y = m; // starting dp state
    // dp backward walk
    while(x > 0 && y > 0)
        if(s[--x] == t[y-1] && dp[x][y] >= dp[x][y-1] + cost[x])
            res.push_back(x), --y;
    reverse(res.begin(), res.end());
    
    /*
    while(x > 0 && y > 0){ // educational dp backward walk
        if(s[x-1] == t[y-1]){
            if(dp[x-1][y] < dp[x-1][y-1] + cost[x-1]){
               x = x - 1, y = y;
            }
            else{
               res.push_back(x-1);
               x = x - 1, y = y - 1;
            }
        }
        else{
            x = x - 1, y = y;
        }
    }*/
    return dp[n][m];
}

int min_subseq_naive(vector <int> &s, vector <int> &t, vector <int> &cost, vector <int> &res){
    int n = s.size(), m = t.size(), best = 1e9;
    vector <int> chosen(n, 0), argmin(0);
    fill(chosen.begin(), chosen.begin() + m, 1);

    do {
        int flag = 1, sum = 0;
        for (int i = 0, j = 0; i < n; ++i)
            if (chosen[i]){
                sum += cost[i];
                if(s[i] != t[j++])
                    flag = 0;
            }
           
        if(flag && sum < best)
            best = sum, argmin = chosen;
    } while(prev_permutation(chosen.begin(), chosen.end()));

    for(int i = 0; i < argmin.size(); ++i)
       if(argmin[i])
           res.push_back(i);
    return best;
}

void print_array(vector <int> v){
    int vs = v.size();
    for(int i = 0; i < vs; ++i)
        printf("%i ", v[i]);
    printf("\n");
}

int main(void){
    int n = 12, m = 5, tests = 200;
    vector <int> s(n), t(m), cost(n);
    
    for(int k = 0; k < tests; ++k){
        for(int i = 0; i < n; ++i)
             s[i] = rand() % 2, cost[i] = rand() % 10;

        for(int j = 0; j < m; ++j)
             t[j] = rand() % 2;
        
        cout << "s: ";
        print_array(s);
        cout << "t: ";
        print_array(t);
        cout << "cost: ";
        print_array(cost);

        vector <int> argmin_1(0), argmin_2(0);
        int mincost_1 = min_subseq(s, t, cost, argmin_1);
        int mincost_2 = min_subseq_naive(s, t, cost, argmin_2);
        
        cout << "opt: ";
        print_array(argmin_1);
        cout << "opt: ";
        print_array(argmin_2);

        printf("dp result: %i, check: %i\n", mincost_1, mincost_2);
        
        if(mincost_1 != mincost_2){
            printf("Test failed.\n");
            return -1;
        }
    }
    return 0;
}
