#include<iostream>

using namespace std;

int n,k;
int dp[201][201];

void func(){
    for(int i = 0; i <= k; i++){
        dp[1][i] = i;
    }

    for(int i = 2; i <= n; i++){
        for(int j = 1; j <= k; j++){
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000;
        }
    }
}

int main(){
    cin >> n >> k;

    func();

    cout << dp[n][k];
    return 0;
}