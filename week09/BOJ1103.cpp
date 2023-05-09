#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int n,m;
int coins[51][51];
int dp[51][51];
bool Visit[51][51];
int ans = 0;
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
string str;

int func(int x,int y){
    if(x < 0 || x >= n || y < 0 || y >= m || coins[x][y] == -1){
        return 0;
    }
    if(Visit[x][y]){
        cout << -1;
        exit(0);
    }
    if(dp[x][y] != -1) return dp[x][y];
    Visit[x][y] = true;

    dp[x][y] = 0;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i]*(coins[x][y]);
        int ny = y + dy[i]*(coins[x][y]);
        dp[x][y] = max(dp[x][y],func(nx,ny)+1);
    }
    Visit[x][y] = false;
    return dp[x][y];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    memset(dp,-1,sizeof(dp));
    memset(Visit,false,sizeof(Visit));
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> str;
        for(int j = 0; j < str.length(); j++){
            if(str[j] == 'H'){
                coins[i][j] = -1;
            }
            else{
                coins[i][j] = str[j] - '1' + 1;
            }
        }
    }
    ans = func(0,0);
    cout << ans;
    return 0;
}