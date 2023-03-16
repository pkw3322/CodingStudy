#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

int n,m;
int arr[1025][1025];
int bit[1025][1025] = {0,};
vector<int> ans;

int getPrefixSum(int row,int column){
    int ret = 0;
    while(row > 0){
        int cc = column;
        while(cc > 0){
            ret += bit[row][cc];
            cc -= cc&-cc;
        }
        row -= row&-row;
    }
    return ret;
}

void update(int row,int column,int dif){
    while(row <= n){
        int cc = column;
        while(cc <= n){
            bit[row][cc] += dif;
            cc += cc&-cc;
        }
        row += row&-row;
    }
}

int getSum(int row1,int column1,int row2,int column2){
    return getPrefixSum(row2,column2) - getPrefixSum(row2,column1-1) - getPrefixSum(row1-1,column2) + getPrefixSum(row1-1,column1-1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m;
    memset(bit,0,sizeof(bit));
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            cin >> arr[i][j];
            update(i,j,arr[i][j]);
        }
    }
    for(int i = 0; i < m; i++){
        int a,b,c,d,e;
        cin >> a >> b >> c;
        if(a == 0){
            cin >> d;
            int dif = d - arr[b][c];
            arr[b][c] = d;
            update(b,c,dif);
        }
        else{
            cin >> d >> e;
            ans.push_back(getSum(b,c,d,e));
        }
    }
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] <<'\n';
    }
    return 0;
}
