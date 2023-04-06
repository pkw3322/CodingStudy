#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int n;
int wines[10001] = {0,};
int dp[10001];

void Solution(){
    dp[0] = 0;
    dp[1] = wines[1];
    dp[2] = wines[1] + wines[2];
    for(int i = 3; i <= n; i++){
        dp[i] = max(dp[i-3]+wines[i-1]+wines[i],max(dp[i-2]+wines[i],dp[i-1]));
    }
}

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> wines[i];
    }
    Solution();
    cout << dp[n];
    return 0;
}