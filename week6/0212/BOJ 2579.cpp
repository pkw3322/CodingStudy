#include<iostream>
#include<algorithm>

using namespace std;

int n;
pair<int,int> dp[301];

void solution(){
    dp[1].second = dp[1].first;
    dp[2].second = dp[1].first + dp[2].first;
    dp[3].second = max(dp[1].first + dp[3].first,dp[2].first + dp[3].first);
    for(int i = 4; i <= n; i++){
        dp[i].second = max(dp[i-2].second + dp[i].first,dp[i-3].second + dp[i-1].first + dp[i].first);
    }
}

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> dp[i].first;
        dp[i].second = 0;
    }
    solution();
    cout << dp[n].second;
}