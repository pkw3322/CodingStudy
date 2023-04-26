#include<iostream>
#include<vector>

using namespace std;

int n,m,tmp;
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
vector<vector<int> >map(500,vector<int>(500,0));
vector<vector<int> >dp(500,vector<int>(500,-1));



int func(int x,int y){
    if(dp[x][y] != -1)
        return dp[x][y];
    int &ret = dp[x][y];
    ret = 0;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 0 && nx < n && ny >= 0 && ny < m && (map[x][y] < map[nx][ny])){
            ret += func(nx,ny);
        }
    }
    return ret;
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> tmp;
            map[i][j] = tmp;
        }
    }
    dp[0][0] = 1;
    cout << func(n-1,m-1);
}