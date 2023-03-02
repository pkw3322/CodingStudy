#include<iostream>

using namespace std;

int n,ans = 0;
int L[21];
int J[21];
int dp[101];

void func(){
    for(int i = 0; i < n; i++){
        for(int j = 100; j >= L[i]; j--){
            dp[j] = max(dp[j],dp[j-L[i]]+J[i]);
        }
    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> L[i];
    }
    for(int i = 0; i < n; i++){
        cin >> J[i];
    }
    func();
    cout << dp[99];
}