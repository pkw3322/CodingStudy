#include<iostream>
#include<vector>
#include<cstring>
#include<queue>

using namespace std;

int n,m,ans = -1;
pair<int,int> red,blue;
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
char map[11][11];
bool Visit[11][11][11][11];
queue<pair<pair< pair<int,int>, pair<int,int> >,int> >q;

void move(int& rx,int& ry,int& dist,int& type){
    while(map[rx+dx[type]][ry+dy[type]] != '#' && map[rx][ry] != 'O'){
        rx += dx[type];
        ry += dy[type];
        dist++;
    }
}

void solution(pair<int,int> r,pair<int,int> b){
    memset(Visit,false,sizeof(Visit));
    q.push(make_pair(make_pair(r,b),0));
    Visit[r.first][r.second][b.first][b.second] = true;
    while(!q.empty()){
        int rx = q.front().first.first.first;
        int ry = q.front().first.first.second;
        int bx = q.front().first.second.first;
        int by = q.front().first.second.second;
        int cnt = q.front().second;
        q.pop();

        if(cnt >= 10)
            break;
        for(int i = 0; i < 4; i++){
            int nrx = rx,nry = ry,nbx = bx,nby = by;
            int rdist = 0,bdist = 0,ncnt = cnt+1;
            move(nrx,nry,rdist,i);
            move(nbx,nby,bdist,i);

            if(map[nbx][nby] == 'O') continue;
            if(map[nrx][nry] == 'O'){
                ans = ncnt;
                return ;
            }
            if(nrx == nbx && nry == nby){
                if(rdist > bdist){
                    nrx -= dx[i];
                    nry -= dy[i];
                }
                else{
                    nbx -= dx[i];
                    nby -= dy[i];
                }
            }
            if(Visit[nrx][nry][nbx][nby])
                continue;
            Visit[nrx][nry][nbx][nby] = true;
            q.push(make_pair(make_pair(make_pair(nrx,nry),make_pair(nbx,nby)),ncnt));
        }
    }
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> map[i][j];
            if(map[i][j] == 'R'){
                red.first = i;
                red.second = j;
            }
            if(map[i][j] == 'B'){
                blue.first = i;
                blue.second = j;
            }
        }
    }
    solution(red,blue);
    cout << ans;
    return 0;
}