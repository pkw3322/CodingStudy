#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>

#define MOD 1000000007LL
using namespace std;

long long d;
vector<vector<long long> > ans(8,vector<long long>(8,0));

vector<vector<long long> >multiple(const vector<vector<long long> >& m1,const vector<vector<long long> >& m2){
    vector<vector<long long> > ret(8,vector<long long>(8,0));
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            long long element = 0;
            for(int k = 0; k < 8; k++){
                element += (m1[i][k]*m2[k][j]);
                element %= MOD;
            }
            ret[i][j] = element % MOD;
        }
    }
    return ret;
}

void solution(){
    for(int i = 0; i < 8; i++){
        ans[i][i] = 1;
    }

    vector<vector<long long> >f(8,vector<long long>(8,0));

    f[0][1] = 1;
    f[0][2] = 1;
    f[1][0] = 1;
    f[1][2] = 1;
    f[1][3] = 1;
    f[2][0] = 1;
    f[2][1] = 1;
    f[2][3] = 1;
    f[2][4] = 1;
    f[3][1] = 1;
    f[3][2] = 1;
    f[3][4] = 1;
    f[3][5] = 1;
    f[4][2] = 1;
    f[4][3] = 1;
    f[4][5] = 1;
    f[4][7] = 1;
    f[5][3] = 1;
    f[5][4] = 1;
    f[5][6] = 1;
    f[6][5] = 1;
    f[6][7] = 1;
    f[7][4] = 1;
    f[7][6] = 1;

    while(d > 0){
        if(d & 1){
            ans = multiple(ans,f);
        }
        f = multiple(f,f);
        d = d >> 1;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    cin >> d;
    solution();
    cout << ans[0][0];
    return 0;
}
