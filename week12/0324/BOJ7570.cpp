#include<iostream>
#include<vector>

using namespace std;

int n,ans,x;
int dp[1000001] = {0, };

int main(){
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> x;
        dp[x] = dp[x-1] + 1;
        ans = max(ans,dp[x]);
    }

    cout << n-ans;
    return 0;
}