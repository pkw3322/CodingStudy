#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

int r,c,t;
int upx[4] = {0,-1,0,1};
int upy[4] = {1,0,-1,0};
int downx[4] = {0,1,0,-1};
int downy[4] = {1,0,-1,0};
int dx[4] = {0,-1,0,1};
int dy[4] = {1,0,-1,0};

pair<int,int> cleaner; 
int arr[51][51];
int temp[51][51];

void diffuse(int x,int y,int value){
    int cnt = 0;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 0 && nx < r && ny >= 0 && ny < c && temp[nx][ny] != -1){
            cnt++;
            temp[nx][ny] += (value/5);
        }
    }
    temp[x][y] += (value - (cnt*(value/5)));
}

void cleaning(){
    int cx = cleaner.first,cy = cleaner.second;
    int curX = cx,curY = cy+1;
    int downX = cx+1,downY = cy+1;
    int upTemp = arr[curX][curY],downTemp = arr[downX][downY],temp;
    arr[curX][curY] = 0;
    arr[downX][downY] = 0;
    for(int i = 0; i < 4; i++){
        while((curX+upx[i]) >= 0 && (curX+upx[i]) < r && (curY+upy[i]) >= 0 && (curY+upy[i]) < c){
            if(arr[curX+upx[i]][curY+upy[i]] == -1)
                break;
            temp = arr[curX+upx[i]][curY+upy[i]];
            arr[curX+upx[i]][curY+upy[i]] = upTemp;
            upTemp = temp;
            curX += upx[i];
            curY += upy[i];    
        }
        while((downX+downx[i]) >= 0 && (downX+downx[i]) < r && (downY+downy[i]) >= 0 && (downY+downy[i]) < c){
            if(arr[downX+downx[i]][downY+downy[i]] == -1)
                break;
            temp = arr[downX+downx[i]][downY+downy[i]];
            arr[downX+downx[i]][downY+downy[i]] = downTemp;
            downTemp = temp;
            downX += downx[i];
            downY += downy[i];
        }
    }
}   

void solution(){
    for(int times = 0; times < t; times++){
        memset(temp,0,sizeof(temp));
        temp[cleaner.first][cleaner.second] = -1;
        temp[cleaner.first+1][cleaner.second] = -1;
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(arr[i][j] > 0)
                    diffuse(i,j,arr[i][j]);
            }
        }
        memcpy(arr,temp,sizeof(arr));
        cleaning();
    }
}

int main(){
    cin >> r >> c >> t;
    bool isFirst = true;
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            cin >> arr[i][j];
            if(arr[i][j] == -1 && isFirst){
                isFirst = false;
                cleaner = make_pair(i,j);
            }
        }
    }
    solution();
    int ans = 0;
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            if(arr[i][j] < 1)
                continue;
            ans += arr[i][j];
        }
    }
    cout << ans << '\n';

    return 0;
}