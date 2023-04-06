#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

struct GRAPH{
    int A;
    int B;
    int weight;
};

int V,E,ans;
int parent[10001];
vector<GRAPH> graphs;
bool Visit[10001];

bool cmp(GRAPH &g1,GRAPH &g2){
    return g1.weight < g2.weight;
}

int find(int x){
    if(parent[x] == x)return x;
    else{
        parent[x] = find(parent[x]);
        return parent[x];
    }
}

void Union(int x,int y){
    int xRoot = find(x);
    int yRoot = find(y);

    if(xRoot != yRoot)
        parent[yRoot] = xRoot;
}

bool isSameParent(int x,int y){
    if(find(x) == find(y))
        return true;
    else
        return false;
}

void Solution(){
    for(int i = 1; i <= V; i++){
        parent[i] = i;
    }
    for(int i = 0; i < E; i++){
        if(!isSameParent(graphs[i].A,graphs[i].B)){
            Union(graphs[i].A,graphs[i].B);
            ans += graphs[i].weight;
        }
    }
}

int main(){
    cin >> V >> E;
    int a,b,c;
    memset(Visit,false,sizeof(Visit));
    for(int i = 0; i < E; i++){
        cin >> a >> b >> c;
        GRAPH g = {a,b,c};
        graphs.push_back(g);
    }
    sort(graphs.begin(),graphs.end(),cmp);
    Solution();
    cout << ans;
    return 0;
}