#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

#define INF 1e15

using namespace std;

int n,m,k;
long long ans = INF;
vector<vector<pair<int,int> > >road(10001);
vector<vector<long long> >costs(10001,vector<long long>(21,INF));
priority_queue<pair<long long,pair<int,int> > >pq;

void dijkstra(){
    pq.push(make_pair(0,make_pair(1,0)));
    costs[1][0] = 0;
    while(!pq.empty()){
        int location = pq.top().second.first;
        int cnt = pq.top().second.second;
        long long cur_cost = -pq.top().first;
        pq.pop();
        
        if(cur_cost > costs[location][cnt])
            continue;
        
        for(int i = 0; i < road[location].size(); i++){
            int next = road[location][i].first;
            long long next_cost = cur_cost + road[location][i].second;
            
            //포장 했을 때
            if(next_cost < costs[next][cnt]){
                costs[next][cnt] = next_cost;
                pq.push(make_pair(-next_cost,make_pair(next,cnt)));
            }

            //포장 하지 않았을 때
            if(cur_cost < costs[next][cnt+1] && cnt < k){
                costs[next][cnt+1] = cur_cost;
                pq.push(make_pair(-cur_cost,make_pair(next,cnt+1)));
            }
        }
    }
}

int main(){
    cin >> n >> m >> k;
    int a,b,c;
    for(int i = 0; i < m; i++){
        cin >> a >> b >> c;
        road[a].push_back(make_pair(b,c));
        road[b].push_back(make_pair(a,c));
    }
    dijkstra();
    for(int i = 0; i <= k; i++){
        ans = min(ans,costs[n][i]);
    }
    cout << ans;
    return 0;
}