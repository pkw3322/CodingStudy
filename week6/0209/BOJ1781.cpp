#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

int n;
long long maxCupNoodle = 0;
pair<int, int> problem[200001];
priority_queue<int,vector<int>,greater<int> >pq;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> problem[i].first >> problem[i].second;
    }
    sort(problem,problem+n);
    for(int i = 0; i < n; i++){
        if(pq.size() < problem[i].first){
            pq.push(problem[i].second);
        }
        else if(pq.top() < problem[i].second){
            pq.pop();
            pq.push(problem[i].second);
        }
    }
    while(!pq.empty()){
        maxCupNoodle += pq.top();
        pq.pop();
    }
    cout << maxCupNoodle;
    return 0;
}