#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>

using namespace std;

int n;
int W[16][16];
int dp[16][1<<16];


int func(int cur,int Visit){
    if(Visit == (1<<n)-1){
        if(W[cur][0] == 0)return 200000000;
        return W[cur][0];
    }
    int &result = dp[cur][Visit];
    if(result != -1){
        return result;
    }
    result = 200000000;
    for(int i = 0; i < n; i++){
        if(W[cur][i] == 0)continue;
        if((Visit & (1 << i)) == (1 << i)) continue;
        result = min(result,W[cur][i] + func(i,Visit|1<<i));
    }
    return result;
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> W[i][j];
        }
    }
    memset(dp,-1,sizeof(dp));
    cout << func(0,1);

}