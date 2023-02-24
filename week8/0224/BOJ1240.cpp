#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
#include<algorithm>

using namespace std;

int n,m,x,y,z;
int dist[1001];
vector<pair<int,int> >v[1002];
queue<int>q;

int func(int start,int end){
    int sum = 0;
    memset(dist,-1,sizeof(dist));
    q.push(start);
    dist[start] = 0;
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for(int i = 0; i < v[cur].size(); i++){
            if(dist[v[cur][i].first] != -1) continue;
            dist[v[cur][i].first] = dist[cur] + v[cur][i].second;
            q.push(v[cur][i].first);
         }
    }
    return dist[end];
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n-1; i++){
        cin >> x >> y >> z;
        v[x].push_back(make_pair(y,z));
        v[y].push_back(make_pair(x,z));
    }
    for(int i = 0; i < m; i++){
        cin >> x >> y;
        cout << func(x,y) << '\n';
    }
    return 0;
}