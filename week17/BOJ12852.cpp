#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

#define INF 10000000
using namespace std;

int n;
int dp[1000001];
int pre[1000001];
vector<int> ans;
queue<int> q;

void solution(){
    for(int i = 1 ; i < n; i++){
        dp[i] = INF;
    }
    dp[n] = 0;
    pre[n] = INF;
    q.push(n);
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        if(cur > 1){
            if(cur%3 == 0){
                if(dp[cur/3] > (dp[cur]+1)){
                    dp[cur/3] = dp[cur]+1;
                    pre[cur/3] = cur;
                    q.push(cur/3);
                }
            }
            if(cur%2 == 0){
                if(dp[cur/2] > (dp[cur]+1)){
                    dp[cur/2] = dp[cur]+1;
                    pre[cur/2] = cur;
                    q.push(cur/2);
                }
            }
            if(dp[cur-1] > (dp[cur]+1)){
                dp[cur-1] = dp[cur]+1;
                pre[cur-1] = cur;
                q.push(cur-1);
            }
        }
    }
    cout << dp[1]<<'\n';
    int temp = pre[1];
    ans.push_back(1);
    while(temp != INF){
        ans.push_back(temp);
        temp = pre[temp];
    }
    for(int i = ans.size()-1; i >= 0; i--){
        cout << ans[i] << ' ';
    }
    
}

int main(){
    cin >> n;
    solution();

    return 0;
}