#include<iostream>
#include<vector>
#include<algorithm>

#define INF 1000000000
using namespace std;

int n;
pair<int,int> matrixs[501];
int dp[501][501] = {0, };

void solution(){
    
    for(int len = 1; len < n; len++){
        for(int i = 0; i < n; i++){
            int j = i+len;
            if(j >= n)
                break;
            int res = INF;

            for(int k = i; k < j; k++){
                res = min(res,dp[i][k] + dp[k+1][j] + matrixs[i].first*matrixs[k].second*matrixs[j].second);
            }
            dp[i][j] = res;
        }
    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> matrixs[i].first >> matrixs[i].second;
    }
    solution();
    cout << dp[0][n-1];
}