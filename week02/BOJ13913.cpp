#include<iostream>
#include<algorithm>
#include<queue>
#include<cstring>
#include<vector>

using namespace std;

uint n,k;
int ret = 999999,cnt;
int pre[100001];
bool visited[100001];
queue<pair<int,int> >q;

vector<int> result;

void func(){
    q.push(make_pair(n,0));
    visited[n] = true;
    while(!q.empty()){
        int cur = q.front().first;
        int count = q.front().second;
        q.pop();
        
        if(cur == k){
            if(ret > count){
                ret = count;

                int idx = cur;
                while(idx != n){
                    result.push_back(idx);
                    idx = pre[idx];
                }
                result.push_back(n);

                return ;
            }
        }

        if(!visited[cur+1] && cur >= 0 && cur < 100000){
            q.push(make_pair(cur+1, count+1));
            visited[cur+1] = true;
            pre[cur+1] = cur;
        }
        if(!visited[cur-1] && cur > 0 && cur <= 100000){
            q.push(make_pair(cur-1, count+1));
            visited[cur-1] = true;
            pre[cur-1] = cur;
        }
        if(!visited[2*cur] && cur >= 0 && cur <= 50000){
            q.push(make_pair(2*cur, count+1));
            visited[2*cur] = true;
            pre[2*cur] = cur;
        }
    }
}
int main(){
    cin >> n >> k;
    memset(visited,false,sizeof(visited));
    memset(pre,-1,sizeof(pre));

    func();

    cout << ret << '\n';

    for(int i = result.size()-1; i > -1; i--){
        cout << result[i] << ' ';
    }
    
    return 0;
}