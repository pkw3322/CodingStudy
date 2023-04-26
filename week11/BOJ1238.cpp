#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

#define INF 19999999
using namespace std;

int n,m,x;
vector<pair<int,int> >vil[1001];
vector<int> dist;
int rDist[1001];
int ans = -1;

void Dijkstra(int start){
    dist.clear();
    dist.resize(n+1,INF);

    dist[start] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int> >,greater<pair<int,int> > >pq;
    pq.push(make_pair(0,start));
    while(!pq.empty()){
        int cost = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if(cost > dist[cur])
            continue;

        for(int i = 0; i < vil[cur].size(); i++){
            int next = vil[cur][i].first;
            int nCost = cost + vil[cur][i].second;

            if(nCost < dist[next]){
                dist[next] = nCost;
                pq.push(make_pair(nCost,next));
            }
        }
    }
}

void solution(){
    for(int i = 1; i <= n; i++){
        Dijkstra(i);
        rDist[i] = dist[x];
    }
    Dijkstra(x);
    for(int i = 1; i <= n; i++){
        rDist[i] += dist[i];
        ans = max(ans,rDist[i]);
    }
}

int main(){
    cin >> n >> m >> x;
    int a,b,c;
    for(int i = 0; i < m; i++){
        cin >> a >> b >> c;
        vil[a].push_back(make_pair(b,c));
    }
    solution();
    cout << ans;
    return 0;
}