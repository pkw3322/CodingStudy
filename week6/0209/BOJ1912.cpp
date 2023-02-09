#include<iostream>
#include<algorithm>

using namespace std;

int n;
int arr[200000];
int dp[200000];
long long result;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
        dp[i] = arr[i];
    }    
    result = arr[0];
    for(int i = 0; i < n; i++){
        dp[i] = max(dp[i],dp[i-1] + arr[i]);
        if(dp[i] > result){
            result = dp[i];
        }
    }
    cout << result;
    return 0;
}