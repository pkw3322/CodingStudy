#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

#define MOD 1000000003

using namespace std;

int n,k;
int dp[1001][1001] = {0, };

int main(){
    cin >> n >> k;
    
    for(int i = 0; i < n; i++){
        dp[i][0] = 1;
        dp[i][1] = i;
    }

    for(int i = 2; i <= n; i++){
        for(int j = 2; j <= k; j++){
            dp[i][j] = (dp[i-2][j-1] + dp[i-1][j])%MOD;
        }
    }

    cout << (dp[n-1][k]+dp[n-3][k-1])%MOD;
    return 0;
}