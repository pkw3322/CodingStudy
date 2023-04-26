#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

int t,End,n,k;
int times[1001];
int relation[1001][1001];
int dp[1001];
vector<int> ans;

int func(int now){
    if(dp[now] != -1)
        return dp[now];
    int &ret = dp[now];
    ret = 0;
    for(int i = 1; i <= n; i++){
        if(relation[i][now] == 0)
            continue;
        ret = max(ret,func(i));
    }
    ret += times[now];
    return ret;
}

int main(){
    cin >> t;
    int from,to;
    while(t > 0){
        memset(times,0,sizeof(times));
        memset(relation,0,sizeof(relation));
        memset(dp,-1,sizeof(dp));
        cin >> n >> k;
        for(int i = 1; i <= n; i++){
            cin >> times[i];
        }
        for(int i = 0; i < k; i++){
            cin >> from >> to;
            relation[from][to] = 1;
        }
        cin >> End;
        ans.push_back(func(End));
        t--;
    }
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << '\n';
    }
    return 0;
}