#include<iostream>
#include<queue>

using namespace std;

int r,c,ret = -1;
char mtx[1000][1000];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

queue<pair<int,int> >person;
queue<pair<int,int> >fire;

int main(){
    cin >> r >> c;
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            cin >> mtx[i][j];
            if(mtx[i][j] == 'J'){
                if(i == 0 || i == r-1 || j == 0 || j == c-1)
                    ret = 1;
                person.push(make_pair(i,j));
            }
            else if(mtx[i][j] == 'F'){
                fire.push(make_pair(i,j));
            }
        }
    }
    
    if(ret > -1)
        cout << ret;
    else{
        int cnt = 0;
        while(true){
            int len = fire.size();
            for(int i = 0; i < len; i++){
                int cy = fire.front().first;
                int cx = fire.front().second;
                fire.pop();
                for(int j = 0; j < 4; j++){
                    int nx = cx + dx[j];
                    int ny = cy + dy[j];
                    if(nx >= 0 && nx < c && ny >= 0 && ny < r && (mtx[ny][nx] == '.' || mtx[ny][nx] == 'J')){
                        mtx[ny][nx] = 'F';
                        fire.push(make_pair(ny,nx));
                    }
                }
            }
            len = person.size();
            for(int i = 0; i < len; i++){
                int cy = person.front().first;
                int cx = person.front().second;
                person.pop();
                for(int j = 0; j < 4; j++){
                    int nx = cx + dx[j];
                    int ny = cy + dy[j];
                    if(nx >= 0 && nx < c && ny >= 0 && ny < r && mtx[ny][nx] == '.'){
                        mtx[ny][nx] = 'J';
                        person.push(make_pair(ny,nx));
                    }
                    else if(nx < 0 || ny < 0 || nx == c || ny == r){
                        ret = cnt + 1;
                        break;
                    }
                }
                if(ret > -1) 
                    break;
            }
            if(person.empty())
                break;
            if(ret > -1) 
                break;
            cnt += 1;
        }
        if (ret == -1) 
            cout << "IMPOSSIBLE";
        else 
            cout << ret;
    }
    
    return 0;
}