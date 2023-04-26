#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;

int mtx[1001][1001];

int main(){
    string from,to;
    cin >> from >> to;
    int maxLen = max(from.length(),to.length());
    for(int i = 1; i <= maxLen; i++){
        mtx[0][i] = i;
        mtx[i][0] = i;
    }
    for(int i = 1; i <= to.length(); i++){
        for(int j = 1; j <= from.length(); j++){
            if(from[j-1] == to[i-1])
                mtx[i][j] = mtx[i-1][j-1];
            else
                mtx[i][j] = min(mtx[i-1][j-1],min(mtx[i-1][j],mtx[i][j-1])) + 1;
        }
    }
    cout << mtx[to.length()][from.length()];
    return 0;
}