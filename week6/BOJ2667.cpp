#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
#include<cstring>

using namespace std;

int n;
int map[25][25];
bool Visit[25][25];
vector<int> ans;
int di[4] = {-1,1,0,0};
int dj[4] = {0,0,-1,1};
queue<pair<int,int> > q;

void solution(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(Visit[i][j]) continue;
            if(map[i][j] == 1){
                int cnt = 1;
                Visit[i][j] = true;
                q.push(make_pair(i,j));
                while(!q.empty()){
                    int ci = q.front().first;
                    int cj = q.front().second;
                    q.pop();
                    for(int k = 0; k < 4; k++){
                        int ni = ci + di[k];
                        int nj = cj + dj[k];
                        if(ni >= 0 && ni < n && nj >= 0 && nj < n){
                            if(!Visit[ni][nj] && map[ni][nj] == 1){
                                q.push(make_pair(ni,nj));
                                Visit[ni][nj] = true;
                                cnt++;
                            }
                        }
                    }
                }
                ans.push_back(cnt);
            }
        }
    }
}

int main(){
    cin >> n;
    char input;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> input;
            map[i][j] = int(input-'0');
        }
    }
    memset(Visit,false,sizeof(Visit));
    solution();
    sort(ans.begin(),ans.end());
    cout << ans.size() << '\n';
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << '\n';
    }
    return 0;
}