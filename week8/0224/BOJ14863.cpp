#include<iostream>
#include<algorithm>

using namespace std;

int n,k,ans;
pair<int,int> bike[101];
pair<int,int> walk[101];
int dp[101][100001] = {0,};

int func(int step,int rest){
    if(step == n+1){
        return 0;
    }
    if(dp[step][rest] != 0)
        return dp[step][rest];
    int ans = -1e9;

    if(walk[step].first <= rest){
        ans = max(ans,func(step+1,rest-walk[step].first)+walk[step].second);
    }
    if(bike[step].first <= rest){
        ans = max(ans,func(step+1,rest-bike[step].first)+bike[step].second);
    }
    dp[step][rest] = ans;
    return ans;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL); 
    cin >> n >> k;
    for(int i = 1; i <= n; i++){
        cin >> walk[i].first >> walk[i].second >> bike[i].first >> bike[i].second;

    }
    cout << func(1,k);
    
    return 0;
}