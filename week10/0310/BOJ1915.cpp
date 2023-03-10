#include<iostream>
#include<algorithm>

using namespace std;

string str;
int n,m,maxLen = 0;
int map[1001][1001];


int func(){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            if(map[i][j] == 0) continue;
            map[i][j] = min(map[i-1][j-1],min(map[i-1][j],map[i][j-1]))+1;
            maxLen = max(maxLen,map[i][j]);
        }
    }

    return maxLen*maxLen;
}

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> str;
        for(int j = 0; j < str.length(); j++){
            map[i][j+1] = str[j] - '0';
        }
    }

    cout << func();
    return 0;
}