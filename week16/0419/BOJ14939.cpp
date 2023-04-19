#include<iostream>
#include<algorithm>
#include<cstring>

#define INF 1000000000
using namespace std;

bool light[10][10];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int cnt = INF;


void change(int x,int y, bool temp[][10]){
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 0 && nx < 10 && ny >= 0 && ny < 10){
            temp[nx][ny] = !temp[nx][ny];
        }
    }
    temp[x][y] = !temp[x][y];
}

bool isOnLight(bool temp[][10]){
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if(temp[i][j])
                return true;
        }
    }
    return false;
}

void solution(int now,int sum,bool arr[][10]){
    if(now == 10){
        bool temp3[10][10] = {0, };
        memcpy(temp3,arr,sizeof(bool)*100);
        
        for(int i = 1; i < 10; i++){
            for(int j = 0; j < 10; j++){
                if(temp3[i-1][j]){
                    change(i,j,temp3);
                    sum++;
                }
            }
        }

        if(!isOnLight(temp3))
            cnt = min(cnt,sum);
        return ;
    }

    bool temp1[10][10] = {0, };
    bool temp2[10][10] = {0, };
    memcpy(temp1,arr,sizeof(bool)*100);
    memcpy(temp2,arr,sizeof(bool)*100);

    solution(now+1,sum,temp1);

    change(0,now,temp2);
    solution(now+1,sum+1,temp2);
}

int main(){
    char temp;
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            cin >> temp;
            if(temp == '#'){
                light[i][j] = false;
            }
            else{
                light[i][j] = true;
            }
        }
    }
    solution(0,0,light);

    if(cnt == INF)
        cout << -1;
    else
        cout << cnt;
    return 0;
}