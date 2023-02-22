#include<iostream>

using namespace std;

int n;
int dp[101][10] = {0, };

int func(int n){
    int ret = 0;
    for(int i = 2; i <= n; i++){
        for(int j = 0; j < 10; j++){
            if(j == 0)
                dp[i][j] = (dp[i-1][j+1])%1000000000;
            else if(j == 9)
                dp[i][j] = (dp[i-1][j-1])%1000000000;
            else
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%1000000000;   
        }
    }
    for(int i = 0; i < 10; i++){
        ret = (ret + dp[n][i])%1000000000;
    }
    return ret;
}

int main(){
    cin >> n;
    for(int i = 1; i < 10; i++)
        dp[1][i] = 1;
    
    cout << func(n);
    return 0;
}