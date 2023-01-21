#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<deque>

using namespace std;

int n,m,k,cnt = 0;
int A[11][11];
int food[11][11];

deque<int> trees[11][11];

int dx[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};

void springSummer(){
    for(int r = 1; r <= n; r++){
        for(int c = 1; c <= n; c++){
            for(int k = 0; k < trees[r][c].size(); k++){
                if(food[r][c] >= trees[r][c][k]){
                    food[r][c] = food[r][c] - trees[r][c][k];
                    trees[r][c][k] += 1;
                }
                else{
                    for(int l = trees[r][c].size() - 1; l >= k; l--){
                        food[r][c] += (trees[r][c][l]/2);
                        trees[r][c].pop_back();
                    }
                    break;
                }
            }
        }
    }
}

void autumnWinter(){
    for(int r = 1; r <= n; r++){
        for(int c = 1; c <= n; c++){
            if(trees[r][c].size() > 0){
                for(int k = 0; k < trees[r][c].size(); k++){
                    if(trees[r][c][k] % 5 == 0){
                        for(int p = 0; p < 8; p++){
                            int nx = r + dx[p];
                            int ny = c + dy[p];
                            if(nx >= 1 && nx <= n && ny >= 1 && ny <= n)
                                trees[nx][ny].push_front(1);
                        }
                    }
                }
            }

            food[r][c] += A[r][c];
        }
    }
}

int main(){
    int x,y,z;
    cin >> n >> m >> k;
    memset(A,0,sizeof(A));
    for(int r = 1; r <= n; r++){
        for(int c = 1; c <= n; c++){
            food[r][c] = 5;
            cin >> A[r][c];
        }
    }
    for(int i = 0; i < m; i++){
        cin >> x >> y >> z;
        trees[x][y].push_back(z);
    }
    for(int i = 0; i < k; i++){
        springSummer();
        autumnWinter();
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if(trees[i][j].size() > 0)
                cnt += trees[i][j].size();
        }
    }
    cout << cnt;
    return 0;
}