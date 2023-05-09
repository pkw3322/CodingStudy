#include<iostream>

#define MOD 10007;
using namespace std;

int n;

int dp[1001][10] = {0, };

int func(){
    int ans = 0;

    for(int i = 0; i < 10; i++){
        dp[1][i] = 1;
    }

    for(int i = 2; i <= n; i++){
        for(int j = 0; j < 10; j++){
            if(j == 0){
                dp[i][j] = 1;
                continue;
            }
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
            dp[i][j] %= MOD;
        }
    }

    for(int i = 0; i < 10; i++){
        ans += dp[n][i];
    }
    ans %= MOD;
    return ans;
}

int main(){
    cin >> n;

    cout << func();

    return 0;
}