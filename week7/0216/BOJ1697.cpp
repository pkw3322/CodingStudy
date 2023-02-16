#include<iostream>
#include<queue>
#include<cstring>

using namespace std;

int n,k,ans = 999999;
bool Visit[100001];
queue<pair<int,int> > q;

void func(){
    q.push(make_pair(n,0));
    Visit[n] = true;

    while(!q.empty()){
        int now = q.front().first;
        int cnt = q.front().second;
        q.pop();

        Visit[now] = true;
        Visit[k] = false;

        if(now == k){
            ans = min(cnt,ans);
            continue;
        }
        
        if(now > 0 && now <= 100000){
            if(!Visit[now-1]){
                q.push(make_pair(now-1,cnt+1));
            }
        }
        if(now < 100000 && now >= 0){
            if(!Visit[now+1]){
                q.push(make_pair(now+1,cnt+1));
            }
        }
        if(now <= 50000 && now >= 0){
            if(!Visit[2*now]){
                q.push(make_pair(2*now,cnt+1));
            }
        }
    }
}

int main(){
    cin >> n >> k;
    memset(Visit,false,sizeof(Visit));
    func();
    cout << ans;
    return 0;
}