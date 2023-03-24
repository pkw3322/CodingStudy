#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

int N,M,K,T,ans;
int cnt[301];
int dp[301][301];
vector<pair<int,int> >v;

int func(int cur,int prev,int num){
    if(cur == v.size())
        return 0;
    if(dp[cur][num] != 0)
        return dp[cur][num];
    int cost = max(0,T-v[cur].second);
    int real = prev >= cost ? 0 : cost;

    int &ret = dp[cur][num];

    if(num >= real){
        ret = max(func(cur+1,cost,num-real)+v[cur].first,func(cur+1,0,num));
    }
    else{
        ret = func(cur+1,0,num);
    }
    return ret;
}

void solution(){
    int now = cnt[1];
    int Count = 1;
    for(int i = 2; i <= N; i++){
        if(now != cnt[i]){
            v.push_back(make_pair(Count,now));
            Count = 0;
            now = cnt[i];
        }
        Count++;
    }
    v.push_back(make_pair(Count,now));
    ans = func(0,0,K);
}

int main(){
    cin >> N >> M >> K >> T;
    int a,b;
    memset(cnt,0,sizeof(cnt));
    for(int i = 0; i < M; i++){
        cin >> a >> b;
        for(int j = a; j < b; j++){
            cnt[j] = min(T,++cnt[j]);
        }
    }

    solution();
    cout << ans;
    return 0;
}