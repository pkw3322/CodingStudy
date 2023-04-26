#include<iostream>

using namespace std;

int n,m,dist,cnt;
int cx,cy;
int map[51][51];
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int back(int dist){
    return (dist+2)%4;
}

int rightAngle(int dist){
    if(dist == 0)
        return 3;
    else
        return dist-1;
}

bool clean(){
    if(map[cx][cy] == 0){
        cnt++;
        map[cx][cy] = 2;
    }
    bool check = false;
    for(int i = 0; i < 4; i++){
        int nx = cx + dx[i];
        int ny = cy + dy[i];
        if(nx > 0 && nx < n && ny > 0 && ny < m && map[nx][ny] == 0){
            check = true;
            break;
        }
    }
    if(check){
        dist = rightAngle(dist);
        if(map[cx+dx[dist]][cy+dy[dist]] == 0){
            cx = cx+dx[dist];
            cy = cy+dy[dist];
        }
    }
    else{
        if(map[cx+dx[back(dist)]][cy+dy[back(dist)]] != 1){
            cx = cx+dx[back(dist)];
            cy = cy+dy[back(dist)];
        }
        else{
            return false;
        }

    }
    return true;
}

void solution(){
    while(clean()){
    }
}

int main(){
    cin >> n >> m;
    cin >> cx >> cy >> dist;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> map[i][j];
        }
    }
    solution();
    cout << cnt;
    return 0;
}