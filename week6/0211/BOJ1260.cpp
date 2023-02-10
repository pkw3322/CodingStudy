#include<iostream>
#include<vector>
#include<cstring>
#include<queue>

using namespace std;

int n,m,start;
bool arr[1001][10000];
bool visitDFS[1001];
bool visitBFS[1001];


void BFS(int s){
    queue<pair<int,int> >bfsQ;
    cout << s << " ";
    visitBFS[s] = true;
    for(int i = 0; i <= n; i++){
        if(!visitBFS[i] && arr[s][i])
            bfsQ.push(make_pair(s,i));
    }
    while(!bfsQ.empty()){
        int a = bfsQ.front().second;
        if(!visitBFS[a])
            cout << a << " ";
        visitBFS[a] = true;
        bfsQ.pop();
        for(int i = 0; i <= n; i++){
            if(!visitBFS[i] && arr[a][i]){
                bfsQ.push(make_pair(a,i));
            }
        }
    }
}

void DFS(int s){
    cout << s << " ";
    visitDFS[s] = true;
    for(int i = 0; i <= n; i++){
        if(!visitDFS[i] && arr[s][i])
            DFS(i);
    }
}

int main(){
    memset(visitDFS,false,sizeof(visitDFS));
    memset(visitBFS,false,sizeof(visitBFS));
    memset(arr,false,sizeof(arr));
    cin >> n >> m >> start;
    for(int i = 0; i < m; i++){
        int a,b;
        cin >> a >> b;
        arr[a][b] = true;
        arr[b][a] = true;
    }
    DFS(start);
    cout << '\n';
    BFS(start);
    return 0;
}