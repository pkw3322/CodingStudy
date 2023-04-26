#include<iostream>
#include<algorithm>

using namespace std;

int n,k;
pair<int,int> thing[101];
int dp[101][100001] = {0, };

int func(int maximum){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= maximum; j++){
            if(j-thing[i].first >= 0)
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-thing[i].first] + thing[i].second);
            else
                dp[i][j] = dp[i-1][j];
        }
    }
    return dp[n][maximum];
}

int main(){
    cin >> n >> k;
    for(int i = 1; i <= n; i++){
        cin >> thing[i].first >> thing[i].second;
    }
    cout << func(k);
    return 0;
}