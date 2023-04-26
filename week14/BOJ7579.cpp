#include<iostream>
#include<algorithm>

using namespace std;

int n,m,total = 0;
pair<int,int> memorys[101];
int dp[101][10001];

void Solution(){
    for(int i = 1; i <= n; i++){
        for(int j = 0; j <= total; j++){
            if(j-memorys[i].first >= 0){
                dp[i][j] = max(dp[i][j],dp[i-1][j-memorys[i].first] + memorys[i].second);
            }
            dp[i][j] = max(dp[i][j],dp[i-1][j]);
        }
    }
}

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> memorys[i].second;
    }
    for(int i = 1; i <= n; i++){
        cin >> memorys[i].first;
        total += memorys[i].first;
    }

    Solution();
    for(int i = 0; i <= total; i++){
        if(dp[n][i] >= m){
            cout << i;
            break;
        }
    }
    return 0;
}