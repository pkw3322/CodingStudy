#include<iostream>

using namespace std;

long long dp[101] = {0, };
int cnt;

void set(){
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 2;
    dp[5] = 2;
    dp[6] = 3;
    dp[7] = 4;
    dp[8] = 5;
    dp[9] = 7;
    dp[10] = 9;
}

long long func(int now){
    if(now < 3)
        return dp[now];
    if(dp[now] == 0)
        dp[now] = func(now-2) + func(now-3);
    return dp[now];
}

int main(){
    cin >> cnt;
    set();
    while(cnt > 0){
        int n;
        cin >> n;
        cout << func(n) << '\n';
        cnt--;
    }
    return 0;
}