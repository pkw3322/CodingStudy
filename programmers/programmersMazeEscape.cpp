#include <string>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

int dfs(vector<string> maps,int x,int y,int eX,int eY){
    int ret = 19999999;
    queue<pair<pair<int,int>,int > >q;
    vector<vector<bool> >Visit(maps.size(),vector<bool>(maps[0].length(),false));
    q.push(make_pair(make_pair(x,y),0));
    Visit[x][y] = true;
    while(!q.empty()){
        int cX = q.front().first.first;
        int cY = q.front().first.second;
        int cnt = q.front().second;
        q.pop();
        if(cX == eX && cY == eY){
            ret = min(ret, cnt);
            continue;
        }
        for(int i = 0; i < 4; i++){
            int nX = cX + dx[i];
            int nY = cY + dy[i];
            if(nX >= 0 && nX < maps.size() && nY >= 0 && nY < maps[0].length() && !Visit[nX][nY] && maps[nX][nY] != 'X'){
                q.push(make_pair(make_pair(nX,nY),cnt+1));
                Visit[nX][nY] = true;
            }
        }
    }
    if(ret == 19999999)
        return -1;
    return ret;
}

int solution(vector<string> maps) {
    int answer = 0;
    int col = maps.size();
    int row = maps[0].length();
    int sX,sY,lX,lY,eX,eY;
    for(int i = 0; i < col; i++){
        for(int j = 0; j < row; j++){
            if(maps[i][j] == 'S'){
                sX = i;
                sY = j;
            }
            if(maps[i][j] == 'L'){
                lX = i;
                lY = j;
            }
            if(maps[i][j] == 'E'){
                eX = i;
                eY = j;
            }
        }
    }
    
    answer = dfs(maps,sX,sY,lX,lY);
    if(answer == -1)
        return answer;
    int temp = dfs(maps,lX,lY,eX,eY);
    if(temp == -1)
        return temp;
    answer += temp;
    return answer;
}