#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>

using namespace std;

int n,ans;
int home[17][17];
int dp[17][17];
int dx[3] = {0,1,1};
int dy[3] = {1,0,1};
queue<pair<pair<int,int>, int> >q;

bool checking(int x,int y){
    int ax[5] = {0,0,0,-1,1};
    int ay[5] = {0,-1,1,0,0};
    for(int i = 0; i < 5; i++){
        int nx = x + ax[i];
        int ny = y + ay[i];
        if(home[nx][ny] == 1)
            return false;
    }
    return true;
}

void moving(int x,int y,int type,int i){
    int nx = x + dx[i];
    int ny = y + dy[i];
    int ntype = i;
    if(home[nx][ny] == 0 && nx > 0 && nx <= n && ny > 0 && ny <= n){
        if(i == 2){
            if(home[nx-1][ny] == 1 || home[nx][ny-1] == 1)
                return;
        }
        q.push(make_pair(make_pair(nx,ny),ntype));
    }
}

void func(int x,int y,int type){
    q.push(make_pair(make_pair(x,y),type));
    while(!q.empty()){
        int nx = q.front().first.first;
        int ny = q.front().first.second;
        int ntype = q.front().second;
        q.pop();
        if(nx == n && ny == n)
            ans++;
        if(ntype == 0){
            moving(nx,ny,ntype,0);
            moving(nx,ny,ntype,2);
        }
        else if(ntype == 1){
            moving(nx,ny,ntype,1);
            moving(nx,ny,ntype,2);
        }
        else{
            moving(nx,ny,ntype,0);
            moving(nx,ny,ntype,1);
            moving(nx,ny,ntype,2);
        }
    }
}

int main(){
    cin >> n;
    memset(dp,-1,sizeof(dp));
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            cin >> home[i][j];
        }
    }
    func(1,2,0);
    cout << ans;
    return 0;
}