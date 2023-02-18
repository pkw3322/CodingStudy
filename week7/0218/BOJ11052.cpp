#include<iostream>
#include<algorithm>

using namespace std;

int n;
int dp[1001];

void func(){
    for(int i = 2; i <= n; i++){
        for(int j = 1; j < i; j++){
            dp[i] = max(dp[i],dp[j] + dp[i-j]);
        }
    }
}

int main(){
    cin >> n;

    for(int i = 1; i <= n; i++){
        cin >> dp[i];
    }
    
    func();

    cout << dp[n];
}