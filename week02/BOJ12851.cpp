#include<iostream>
#include<algorithm>
#include<queue>
#include<cstring>

using namespace std;

uint n,k;
int ret = 999999,cnt;
bool visited[100001];
queue<pair<int,int> >q;

void func(){
    q.push(make_pair(n,0));
    while(!q.empty()){
        int cur = q.front().first;
        int count = q.front().second;
        q.pop();

        visited[cur] = true;
        visited[k] = false;
        
        if(cur == k){
            if(ret > count){
                ret = count;
                cnt = 1;
            }
            else if(ret == count){
                cnt++;
            }
            continue;
        }

        if(!visited[cur+1] && cur >= 0 && cur < 100000)
            q.push(make_pair(cur+1, count+1));

        if(!visited[cur-1] && cur > 0 && cur <= 100000)
            q.push(make_pair(cur-1, count+1));

        if(!visited[2*cur] && cur >= 0 && cur <= 50000)
            q.push(make_pair(2*cur, count+1));
    }
}
int main(){
    cin >> n >> k;
    memset(visited,false,sizeof(visited));
    
    func();
    cout << ret << '\n' << cnt;
    return 0;
}