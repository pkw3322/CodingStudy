#include<iostream>
#include<cstring>
#include<queue>
 
using namespace std;
 
int r, c, swanX,swanY;
bool isFind;
char lake[1500][1500];
bool visitd[1500][1500];
 
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
 
queue<pair<int, int> > swanQ, swanN, Q, N;
 
void swanBFS(){
    while (!swanQ.empty() && !isFind){
        int x = swanQ.front().first;
        int y = swanQ.front().second;
        swanQ.pop();
 
        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
 
            if (nx >= 0 && nx < r && ny >= 0  && ny < c){
                if (visitd[nx][ny] == false){
                    if (lake[nx][ny] == '.'){
                        visitd[nx][ny] = true;
                        swanQ.push(make_pair(nx, ny));
                    }
                    else if (lake[nx][ny] == 'L'){
                        visitd[nx][ny] = true;
                        isFind = true;
                        break;
                    }
                    else if (lake[nx][ny] == 'X'){
                        visitd[nx][ny] = true;
                        swanN.push(make_pair(nx, ny));
                    }
                }
            }
        }
    }
}
 
void melting(){
    while (!Q.empty()){
        int x = Q.front().first;
        int y = Q.front().second;
        Q.pop();
 
        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
 
            if (nx >= 0 && nx < r && ny >= 0  && ny < c){
                if (lake[nx][ny] == 'X'){
                    lake[nx][ny] = '.';
                    N.push(make_pair(nx, ny));
                }
            }
        }
    }
}
 
void func(){
    int Day = 0;
    swanQ.push(make_pair(swanX, swanY));
    visitd[swanX][swanY] = true;
 
    while (!isFind){
        swanBFS();
 
        if (isFind == false){
            melting();
            Q = N;
            swanQ = swanN;
 
            while (!N.empty()) 
                N.pop();
            while (!swanN.empty()) 
                swanN.pop();
            Day++;
        }
    }
    cout << Day << endl;
}
 
int main(void)
{   
    isFind = false;
    cin >> r >> c;
    for (int i = 0; i < r; i++){
        for (int j = 0; j < c; j++){
            cin >> lake[i][j];
            if (lake[i][j] != 'X') 
                Q.push(make_pair(i, j));    
            if (lake[i][j] == 'L')
            {
                swanX = i;
                swanY = j;
            }
        }
    }
    func();
    return 0;
}
 
 