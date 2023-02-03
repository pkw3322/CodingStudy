#include<iostream>
#include<queue>
#include<cstring>
#include<vector>

using namespace std;

int n,m,fst = 0,snd,thr = -1,maxRoom = -1;
vector<int> mtx[51][51];
bool visited[51][51];
int di[4] = {0,-1,0,1};
int dj[4] = {-1,0,1,0};
queue<pair<int, pair<int,int> > > Q;

void func(){
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(visited[i][j])
                continue;
            queue<pair<int,int> >q;
            q.push(make_pair(i,j));
            visited[i][j] = true;
            int curRoom = 0;
            while(!q.empty()){
                int ci = q.front().first;
                int cj = q.front().second;
                q.pop();
                for(int k = 0; k <4; k++){
                    int ni = ci + di[k];
                    int nj = cj + dj[k];
                    if(ni >= 0 && ni < m && nj >= 0 && nj < n){
                        if(!visited[ni][nj]){
                            if(mtx[ci][cj][k] == 0){
                                visited[ni][nj] = true;
                                q.push(make_pair(ni,nj));
                            }
                            if(mtx[ci][cj][k] == 1){
                                Q.push(make_pair(k,make_pair(ci,cj)));
                            }
                        }
                    }
                }
                curRoom++;
            }
            maxRoom = maxRoom > curRoom ? maxRoom : curRoom;
            fst++;
        }
    }
    snd = maxRoom;
    while(!Q.empty()){
        int ci = Q.front().second.first;
        int cj = Q.front().second.second;
        int ck = Q.front().first;
        Q.pop();
        mtx[ci][cj][ck] = 0;
        memset(visited,false,sizeof(visited));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(visited[i][j])
                    continue;
                queue<pair<int,int> >q;
                q.push(make_pair(i,j));
                visited[i][j] = true;
                int curRoom = 0;
                while(!q.empty()){
                    int ci = q.front().first;
                    int cj = q.front().second;
                    q.pop();
                    for(int k = 0; k <4; k++){
                        int ni = ci + di[k];
                        int nj = cj + dj[k];
                        if(ni >= 0 && ni < m && nj >= 0 && nj < n){
                            if(!visited[ni][nj]){
                                if(mtx[ci][cj][k] == 0){
                                    visited[ni][nj] = true;
                                    q.push(make_pair(ni,nj));
                                }
                            }
                        }
                    }
                    curRoom++;
                }
                maxRoom = maxRoom > curRoom ? maxRoom : curRoom;
            }
        }
        thr = thr > maxRoom ? thr : maxRoom;
        mtx[ci][cj][ck] = 1;
    }
}

int main(){
    cin >> n >> m;

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            int k;
            int arr[4];
            memset(arr,0,sizeof(arr));
            cin >> k;
            if(k >= 8){
                arr[3] = 1;
                k -= 8;
            }
            if(k >= 4){
                arr[2] = 1;
                k -= 4;
            }
            if(k >= 2){
                arr[1] = 1;
                k -= 2;
            }
            if(k >= 1){
                arr[0] = 1;
                k -= 1;
            }
            for(int l = 0; l < 4; l++){
                mtx[i][j].push_back(arr[l]);
            }
        }
    }
    memset(visited,false,sizeof(visited));

    func();

    cout << fst << '\n' << snd << '\n' << thr;
    return 0;
}