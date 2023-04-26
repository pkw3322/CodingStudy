#include<iostream>
#include<queue>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

int N,L,R,cnt = 0,total = 0;
int country[50][50];
bool visited[50][50];
bool flag = true;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

queue<pair<int,int> >q;
vector<pair<int,int> >v;

bool compare(int a, int b){
    if(a > b){
        if(a-b >= L && a-b <= R)
            return true;
        else return false;
    }
    else{
        if(b-a >= L && b-a <= R)
            return true;
        else return false;
    }
}

void func(int start_x,int start_y){
    q.push(make_pair(start_x,start_y));
    visited[start_x][start_y] = true;
    while(!q.empty()){
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++){
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if(!visited[nx][ny] && nx >= 0 && nx < N && ny >= 0 && ny < N && compare(country[cx][cy],country[nx][ny])){
                q.push(make_pair(nx,ny));
                visited[nx][ny] = true;
                v.push_back(make_pair(nx,ny));
                total += country[nx][ny];
            }
        }
    }
}

int main(){
    cin >> N >> L >> R;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> country[i][j];
        }
    }

    while(flag){
        flag = false;
        memset(visited,false,sizeof(visited));
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(!visited[i][j]){
                    v.clear();
                    v.push_back(make_pair(i,j));
                    total = country[i][j];
                    func(i,j);
                }
                if (v.size() >= 2) {
					flag = true; 
					for (int i = 0; i < v.size(); i++) {
						country[v[i].first][v[i].second] = total / v.size(); 
					}
				}
            }
        }
        if(flag)
            cnt++;  
    }
    cout << cnt;
    return 0;
}