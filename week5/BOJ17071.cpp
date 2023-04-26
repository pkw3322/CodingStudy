#include<iostream>
#include<cstring>
#include<queue>

using namespace std;

uint n,k;
int ret = 999999;
bool visited[500001][2];
queue<pair<int,int> >q;

void func(){
    visited[n][0] = true; 
    q.push(make_pair(n,0));
    while(!q.empty()){
        int cur = q.front().first;
        int ctime = q.front().second;
        int curK = k + ctime*(ctime+1)/2;
        
        q.pop();
        if(curK > 500000){
            ret = -1;
            return;
        }
        if(cur == curK || visited[curK][ctime%2]){
            if(ret > ctime){
                ret = ctime;
            }
            return;
        }
        ctime++;
        if(!visited[cur+1][ctime%2] && cur >= 0 && cur < 500000){
            q.push(make_pair(cur+1, ctime));
            visited[cur+1][ctime%2] = true;
        }

        if(!visited[cur-1][ctime%2] && cur > 0 && cur <= 500000){
            q.push(make_pair(cur-1, ctime));
            visited[cur-1][ctime%2] = true;
        }

        if(!visited[2*cur][ctime%2] && cur >= 0 && cur <= 250000){
            q.push(make_pair(2*cur, ctime));
            visited[2*cur][ctime%2] = true;
        }
    }
}

int main(){
    cin >> n >> k;
    func();
    if(ret == 999999)
        cout << -1;
    else
        cout << ret;
    return 0;
}