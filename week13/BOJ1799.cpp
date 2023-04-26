#include<iostream>
#include<algorithm>

using namespace std;

int n;
pair<int,int> ans;
int map[11][11];
bool lCross[20],rCross[20];

void solution(int r,int c,int cnt,int col){
    if(c >= n){
        r++;
        if(c%2 == 0)
            c = 1;
        else
            c = 0;
    }
    if(r >= n){
        if(col == 0)
            ans.first = max(ans.first,cnt);
        else
            ans.second = max(ans.second,cnt);
        return ;
    }
    if(map[r][c] != 0 && !lCross[c-r+n-1] && !rCross[r+c]){
        lCross[c-r+n-1] = 1;
        rCross[r+c] = 1;
        solution(r,c+2,cnt+1,col);
        lCross[c-r+n-1] = 0;
        rCross[r+c] = 0;
    }
    solution(r,c+2,cnt,col);
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> map[i][j];
        }
    }

    solution(0,0,0,0);
    solution(0,1,0,1);
    cout << ans.first + ans.second;
    return 0;
}