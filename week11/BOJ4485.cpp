#include<iostream>
#include<cstring>
#include<vector>
#include<queue>

#define INF 19999999

using namespace std;

int n;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
vector<vector<int> >map(126,vector<int>(126,0));
vector<int> ans;
queue<pair<int, pair<int,int> > >q;


void solution(){
    q.push(make_pair(map[0][0], make_pair(0,0)));
    vector<vector<int> >rupees(126,vector<int>(126,INF));
    while(!q.empty()){
        int cnt = q.front().first;
        int cx = q.front().second.first;
        int cy = q.front().second.second;
        q.pop();
        if(cx == n-1 && cy == n-1)
            continue;
        for(int i = 0; i < 4; i++){
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if(nx >= 0 && nx < n && ny >= 0 && ny < n){
                if(rupees[nx][ny] > map[nx][ny] + cnt){
                    rupees[nx][ny] = map[nx][ny] + cnt;
                    q.push(make_pair(rupees[nx][ny],make_pair(nx,ny)));
                }
            }
        }
    }
    ans.push_back(rupees[n-1][n-1]);
}

int main(){
    while(true){
        cin >> n;
        if(n == 0)
            break;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> map[i][j];
            }
        }
        solution();
    }

    for(int i = 0; i < ans.size(); i++){
        cout << "Problem " << i+1 << ": "<< ans[i] << '\n';
    }

    return 0;
}