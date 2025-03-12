This function generates combinations in reverse lex. order.
```
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
```

And so does this function:
```
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
```
Read the code _min\_subseq\_rec.cpp_ to see how to derive this code from dp table backward walk.
