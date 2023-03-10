#include<iostream>
#include<cstring>

#define mod 1000000

using namespace std;

string str;
int arr[5001],len;
int dp[5001];

int func(){
    if(str[0] == '0'){
        return 0;
    }
    dp[0] = 1;
    for(int i = 1; i <= len; i++){
        if(arr[i] >= 1 && arr[i] <= 9){
            dp[i] = (dp[i-1] + dp[i]) % mod;
        }
        if(i == 1 || arr[i-1] == 0)
            continue;
        int Num = arr[i] + arr[i-1]*10;
        if(Num >= 10 && Num <= 26){
            dp[i] = (dp[i-2] + dp[i]) % mod;
        }
    }
    return dp[len]%mod;
}

int main(){
    cin >> str;
    memset(dp,0,sizeof(dp));
    for(int i = 1; i <= str.length(); i++){
        arr[i] = str[i-1] - '0';
    }
    len = str.length();
    
    cout << func();
    return 0;
}