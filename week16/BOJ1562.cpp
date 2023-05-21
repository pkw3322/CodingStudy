#include<iostream>

#define MOD 1000000000
#define FULL 1023
using namespace std;

int n;
int ans = 0;
int dp[101][10][1<<10];

int check(int dig,int cur,int bit){
    if(dp[dig][cur][bit] != 0)
        return dp[dig][cur][bit];
    if(dig == n){
        if(bit == FULL)
            return 1;
        else
            return 0;
    }
    int & tmp = dp[dig][cur][bit];
    tmp = 0;

    if(cur > 0){
        int next = cur-1;
        tmp += check(dig+1,next,(bit|1<<(next)));
    }
    if(cur < 9){
        int next = cur+1;
        tmp += check(dig+1,next,(bit|1<<(next)));
    }
    tmp %= MOD;
    return tmp;
}

void solution(){
    for(int i = 1; i < 10; i++){
        ans += check(1,i,1<<i);
        ans %= MOD;
    }
}

int main(){
    cin >> n;
    solution();
    cout << ans;
    return 0;
}