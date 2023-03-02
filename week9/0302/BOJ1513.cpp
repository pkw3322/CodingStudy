#include<iostream>
#include<cstring>

#define mod 1000007;
using namespace std;

int n,m,c;
int C[51][51] = {0, };

int dp[51][51][51][51];

int func(int x, int y, int cnt, int prev){
    if(x > n || y > m) return 0;
    if(x == n && y == m){
        if(cnt == 0 && C[x][y] == 0) return 1;
        if(cnt == 1 && C[x][y] > prev) return 1;
        return 0;
    }
	int &ret = dp[x][y][cnt][prev];
	if(ret != -1) return ret;
    ret = 0;
    if(C[x][y] == 0){
        ret = (func(x + 1, y, cnt, prev) + func(x, y + 1, cnt, prev)) % mod;
    }else if(C[x][y] > prev){
        ret = (func(x + 1, y, cnt - 1, C[x][y]) + func(x, y + 1, cnt - 1, C[x][y])) % mod;
    }
	return ret;
}

int main(){
    memset(dp,-1,sizeof(dp));
    cin >> n >> m >> c;
    int x,y;
    for(int i = 1; i <= c; i++){
        cin >> x >> y;
        C[x][y] = i;
    }
    for(int i = 0; i <= c; i++){
        cout << func(1,1,i,0) << " ";
    }
    return 0;
}
