#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

int n;
double m,price;
pair<int,int> candy[5001];
int dp[10001] = {0, };

int func(int money){
    for(int i = 0; i < n; i++){
        for(int j = candy[i].second; j <= money; j++){
            dp[j] = max(dp[j],dp[j-candy[i].second] + candy[i].first);
        }
    }
    return dp[money];
}

int main(){
    while(true){
        memset(candy,0,sizeof(candy));
        memset(dp,0,sizeof(dp));
        cin >> n >> m;
        if(n == 0 && m == 0.00)
            break;
        for(int i = 0; i < n; i++){
            cin >> candy[i].first >> price;
            candy[i].second = (int)(price*100 + 0.5);
        }
        cout << func((int)(m*100+0.5)) << '\n';
    }

    return 0;
}