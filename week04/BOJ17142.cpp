#include<iostream>
#include<cmath>
#include<queue>
#include<vector>
#include<cstring>

using namespace std;

int n,m,result = 1000000,empties = 0;
int mtx[50][50];
int timeline[50][50];
bool selectingVirus[10];

int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

vector<pair<int,int> > virus;

void func(int idx,int cnt){
    if(cnt == m){
        queue<pair<int,int> >q;
        int infected = 0, total = 0;
        memset(timeline,-1,sizeof(timeline));
        for(int i = 0; i < virus.size(); i++){
            if(selectingVirus[i]){
                q.push(make_pair(virus[i].first,virus[i].second));
                timeline[virus[i].first][virus[i].second] = 0;
            }
        }
        while(!q.empty()){
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx >= 0 && nx < n && ny >= 0 && ny < n){
                    if(mtx[nx][ny] != 1 && timeline[nx][ny] == -1){
                        timeline[nx][ny] = timeline[x][y] + 1;
                        if(mtx[nx][ny] == 0){
                            infected++;
                            total = timeline[nx][ny];
                        }
                        q.push(make_pair(nx,ny));
                    }
                }
            }
        }
        if(infected == empties)
            result = result < total ? result : total;
        return;
    }
    for(int i = idx; i < virus.size(); i++){
        if(selectingVirus[i]) continue;
        selectingVirus[i] = true;
        func(i+1,cnt+1);
        selectingVirus[i] = false;
    }
}
int main(){
    cin >> n >> m;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> mtx[i][j];
            if(mtx[i][j] == 2)
                virus.push_back(make_pair(i,j));
            else if(mtx[i][j] == 0){
                empties++;
            }
        }
    }
    memset(selectingVirus,false,sizeof(selectingVirus));
    func(0,0);
    if(result == 1000000) cout << -1;
    else cout << result;
    return 0;
}