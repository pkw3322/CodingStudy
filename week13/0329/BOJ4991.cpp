#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstring>

#define DIRTY 1
#define ROBOT 0
#define WALL -1
#define CLEAN 2
#define INF 2147483647
using namespace std;

int w,h;
vector<int> v;
int map[20][20];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

int bfs(pair<int,int> start,pair<int,int> dirty,int board[20][20]){
    int v[20][20];
    queue<pair<int,int> >q;
    memset(v,0,sizeof(v));
    q.push(start);
    v[start.first][start.second] = 1;

    while(!q.empty()){
        int curX = q.front().first;
        int curY = q.front().second;
        q.pop();
        
        for(int i = 0; i < 4; i++){
            int nx = curX + dx[i];
            int ny = curY + dy[i];
            if(nx >= 0 && nx < h && ny >= 0 && ny < w){
                if(board[nx][ny] != WALL && v[nx][ny] == 0){
                    q.push(make_pair(nx,ny));
                    v[nx][ny] = v[curX][curY] + 1;
                }
            }
        }
    }
    if(v[dirty.first][dirty.second] != 0)
        return v[dirty.first][dirty.second] - 1;
    else
        return -1;
}

int main(){
    while(true){
        cin >> w >> h;
        char c;
        if(w == 0 && h == 0)
            break;
        int answer = INF;
        memset(map,0,sizeof(map));
        pair<int,int> robot;
        vector<pair<int,int> >dirtys;
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                cin >> c;
                if(c == '.')
                    map[i][j] = CLEAN;
                else if(c == 'o'){
                    map[i][j] = ROBOT;
                    robot.first = i;
                    robot.second = j;
                }
                else if(c == '*'){
                    map[i][j] = DIRTY;
                    dirtys.push_back(make_pair(i,j));
                }
                else if(c == 'x'){
                    map[i][j] = WALL;
                }
            }
        }
        int memo[20][20][20][20];
        memset(memo,0,sizeof(memo));
        do{ 
            pair<int, int> tempRobot = robot;  
            int temp[20][20];
            memcpy(temp, map, sizeof(temp));
            int cnt = 0; 
 
            for(int i = 0; i < dirtys.size(); i++){  
                temp[dirtys[i].first][dirtys[i].second] = ROBOT; 
                temp[tempRobot.first][tempRobot.second] = CLEAN; 
 
                if(memo[tempRobot.first][tempRobot.second][dirtys[i].first][dirtys[i].second] == 0){ 
                    int dist = bfs(tempRobot, dirtys[i],temp); 
                    memo[tempRobot.first][tempRobot.second][dirtys[i].first][dirtys[i].second] = dist;  
 
                    if(dist == -1){
                        cnt = INF; 
                        break;
                    }
                    else{
                        cnt += dist;
                    }   
                }
                else{ 
                    if(memo[tempRobot.first][tempRobot.second][dirtys[i].first][dirtys[i].second] == -1){
                        cnt = INF; 
                        break;
                    }
                    else{
                        cnt += memo[tempRobot.first][tempRobot.second][dirtys[i].first][dirtys[i].second];
                    }
                }
                tempRobot = dirtys[i];
            }
            answer = min(answer, cnt);
        }while(next_permutation(dirtys.begin(), dirtys.end()));

        v.push_back((answer == INF) ? -1 : answer);
    }
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << '\n';
    }
    return 0;
}