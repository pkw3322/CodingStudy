#include<iostream>
#include<vector>

using namespace std;

int n,ans = -1;
int panda[500][500];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
vector<vector<int> >dp(500,vector<int>(500,-1));

int move(int x,int y){
    if(dp[x][y] != -1)
        return dp[x][y];
    int &ret = dp[x][y];
    ret = 1;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 0 && nx < n && ny >= 0 && ny < n && panda[nx][ny] < panda[x][y]){
            ret = max(ret,move(nx,ny)+1);
        }
    }
    return ret;
}

void func(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            dp[i][j] = move(i,j);
            ans = max(dp[i][j],ans);
        }
    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> panda[i][j];
        }
    }
    func();
    cout << ans;
    return 0;
}