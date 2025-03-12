#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

vector <vector <int>> combs;

int dp_func(int i, int j){
    return (i >= j) ? 0 : 1e9;
} 
    
void comb_dp(int x, int y, vector <int> &path){
    if(x > 0 && y > 0){
        int u = dp_func(x-1, y);
        int v = dp_func(x-1, y-1);
        int min_value = min(u, v);

        if(v == min_value){
            path.push_back(x-1);
            comb_dp(x-1, y-1, path);
            path.pop_back();
        }
        if(u == min_value)
            comb_dp(x-1, y, path);
    }
    else
        combs.push_back(path);
}

// x-1 >= y                  -> (u, v) == (0, 0)
// x-1  < y & x - 1 >= y - 1 -> (u, v) == (inf, 0) 
// x-1  < y & x - 1 < y - 1  -> (u, v) == (inf, inf)
void comb(int x, int y, vector <int> &path){
    if(x <= 0 || y <= 0){
        combs.push_back(path);
        return;
    }

    path.push_back(x);
    comb(x-1, y-1, path);
    path.pop_back();

    if(x != y)
        comb(x-1, y, path);
}

void print_array(vector <int> v){
    int vs = v.size();
    for(int i = 0; i < vs; ++i)
        printf("%i ", v[i]);
    printf("\n");
}

int main(void){
    int n = 5, m = 3;

    vector <int> path;

    //comb_dp(n, m, path);
    comb(n, m, path);

    for(auto &c : combs)
        print_array(c);

    return 0;
}
