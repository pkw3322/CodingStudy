#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;



vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    priority_queue<pair<int,int> ,vector<pair<int,int> >,greater<pair<int,int> > >pq;
    vector<pair<int,int> > temp;
    vector<int> answer;
    vector<pair<int,int> > mountains[50001];
    int intens[50001];
    bool isSummits[50001];
    
    memset(mountains,0,sizeof(mountains));
    memset(isSummits,false,sizeof(isSummits));
    memset(intens,-1,sizeof(intens));
    
    for(int i = 0; i < paths.size(); i++){
        mountains[paths[i][0]].push_back(make_pair(paths[i][1],paths[i][2]));
        mountains[paths[i][1]].push_back(make_pair(paths[i][0],paths[i][2]));
    }
    for(int i = 0; i < summits.size(); i++){
        isSummits[summits[i]] = true;
    }
    for(int i = 0; i < gates.size(); i++){
        pq.push(make_pair(0,gates[i]));
        intens[gates[i]] = 0;
    }
    
    while(!pq.empty()){
        int cost = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        
        if(cost > intens[cur])
            continue;
        
        if(isSummits[cur]){
            temp.push_back(make_pair(cost,cur));
            continue;
        }
        for(int i = 0; i < mountains[cur].size(); i++){
            int weight = mountains[cur][i].second;
            int to = mountains[cur][i].first;
            if(intens[to] == -1 || max(cost,weight) < intens[to]){
                intens[to] = max(cost,weight);
                pq.push(make_pair(intens[to],to));
            }
        }
    }
    sort(temp.begin(),temp.end());
    answer.push_back(temp[0].second);
    answer.push_back(temp[0].first);
    return answer;
}