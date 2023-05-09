#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;
int n,m,result = -1;
int arr[500][500];
bool visits[500][500];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

void getMax(int x,int y,int count, int sum){
    if(count == 4){
        result = result > sum ? result : sum;
        return ;
    }
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 0 && ny >= 0 && nx < n && ny < m && !visits[nx][ny]) {
            visits[nx][ny] = 1;
            getMax(nx, ny, count+1, sum + arr[nx][ny]);
            visits[nx][ny] = 0;
        }
    }
    if(x-1 >= 0 && y-1 >= 0 && x+1 < n) { 
        result = max(result, (arr[x-1][y] + arr[x][y-1] + arr[x][y] + arr[x+1][y]));
    }
    if(x-1 >= 0 && y+1 < m && x+1 < n) { 
        result = max(result, (arr[x-1][y] + arr[x][y+1] + arr[x][y] + arr[x+1][y]));
    }
    if(y-1 >= 0 && y+1 < m && x+1 < n) {
        result = max(result, (arr[x][y] + arr[x+1][y] + arr[x+1][y-1] + arr[x+1][y+1]));
    }
    if(y-1 >= 0 && y+1 < m && x+1 < n) { 
        result = max(result, (arr[x][y-1] + arr[x][y] + arr[x][y+1] + arr[x+1][y]));
    }
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> arr[i][j];
        }
    }
    memset(visits,false,sizeof(visits));

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            visits[i][j] = true;
            getMax(i,j,1,arr[i][j]);
            visits[i][j] = false;
        }
    }
    cout << result;
    return 0;
}