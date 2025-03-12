#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

void print_array(vector <int> v){
    int vs = v.size();
    for(int i = 0; i < vs; ++i)
        printf("%i ", v[i]);
    printf("\n");
}

void walk(vector <vector <int>> &dp,
    vector <int> &s, 
    vector <int> &t,
    vector <int> &cost, 
    int x, 
    int y,
    vector <int> &path, 
    vector <vector<int>> &combs){

    if(x > 0 and y > 0){
        if(s[x-1] == t[y-1]){
            int min_value = min(dp[x-1][y], dp[x-1][y-1] + cost[x-1]);
        
            if(dp[x-1][y-1] + cost[x-1] == min_value){
                path.push_back(x-1);
                walk(dp, s, t, cost, x-1, y-1, path, combs);
                path.pop_back();
            }
            if(dp[x-1][y] == min_value){
                walk(dp, s, t, cost, x-1, y, path, combs);
            }
        }
        else
            walk(dp, s, t, cost, x-1, y, path, combs);
    }
    else
        combs.push_back(path);
}

int min_subseq_rec(vector <int> &s, vector <int> &t, vector <int> &cost, vector <int> &res){
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

    vector <vector<int>> combs;
    vector <int> path;

    walk(dp, s, t, cost, n, m, path, combs);

    for(auto &c : combs)
        print_array(c);
    printf("\n%lu solution found: \n\n", combs.size());    

    return dp[n][m];
}

int main(void){
    int n = 15, m = 5;
    vector <int> s(n), t(m), cost(n);
    
    for(int i = 0; i < n; ++i)
        s[i] = 1, cost[i] = 1;

    for(int j = 0; j < m; ++j)
        t[j] = 1;
        
    cout << "s: ";
    print_array(s);

    cout << "t: ";
    print_array(t);

    cout << "c: ";
    print_array(cost);

    vector <int> argmin(0);
    int mincost = min_subseq_rec(s, t, cost, argmin);

    return 0;
}
