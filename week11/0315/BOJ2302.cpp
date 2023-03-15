#include<iostream>
#include<cstring>

using namespace std;

int n,m;
uint ans = 1;
int dp[41];
int Vip[41];

void solution(){
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    for(int i = 3; i <= n; i++)
        dp[i] = dp[i-1] + dp[i-2];
    int start = 0;
    for(int i = 0; i < m; i++){
        int end = Vip[i];
        ans *= dp[end - start - 1];
        start = end;
    }
    ans *= dp[n-start];
}

int main(){
    cin >> n >> m;
    int idx;

    for(int i = 0; i < m; i++){
        cin >> Vip[i];
    }

    solution();
    cout << ans;
    return 0;
}