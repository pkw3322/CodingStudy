#include<iostream>
#include<algorithm>

using namespace std;

int n,k;
int coins[100];
int dp[100001] = {0, };

int func(int money){
    if(dp[money] != 0)
        return dp[money];
    dp[money] = 100001;
    for (int i = 1; i < money; i++){
        dp[money] = min(dp[money],func(money-i)+func(i));
    }
    if(dp[money] == 100001)
        return -1;
    return dp[money];
}

int main(){
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        cin >> coins[i];
        dp[coins[i]] = 1;
    }
    cout << func(k);
    return 0;
}