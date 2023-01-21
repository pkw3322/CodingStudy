#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdlib>

using namespace std;

int r,c,m,sumSize = 0;

typedef struct shark{
    int size;
    int dest;
    int speed;
}SHARK;

SHARK sea[101][101];
SHARK aftermove[101][101];

void setAfterMove(){
    for(int i = 1; i <= r; i++){
        for(int j = 1; j <= c; j++){
            aftermove[i][j].dest = 0;
            aftermove[i][j].size = 0;
            aftermove[i][j].speed = 0;
        }
    }
}

void catchshark(int person){
    for(int i = 1; i <= r; i++){
        if(sea[i][person].size != 0){
            sumSize += sea[i][person].size;
            sea[i][person].size = 0;
            sea[i][person].dest = 0;
            sea[i][person].speed = 0;
            break;
        }
    }
}

void sharkmove(){
    setAfterMove();
    for(int i = 1; i <= r; i++){
        for(int j = 1; j <= c; j++){
            if(sea[i][j].size != 0){
                int nx = i,ny = j;
                int speed = sea[i][j].speed;
                while(speed > 0){
                    if(sea[i][j].dest == 1){
                        if(nx == 1){
                            sea[i][j].dest = 2;
                        }
                        else{
                            nx--;
                            speed--;
                        }
                    }
                    else if(sea[i][j].dest == 2){
                        if(nx == r){
                            sea[i][j].dest = 1;
                        }
                        else{
                            nx++;
                            speed--;
                        }
                    }
                    else if(sea[i][j].dest == 3){
                        if(ny == c){
                            sea[i][j].dest = 4;
                        }
                        else{
                            ny++;
                            speed--;
                        }
                    }
                    else if(sea[i][j].dest == 4){
                        if(ny == 1){
                            sea[i][j].dest = 3;
                        }
                        else{
                            ny--;
                            speed--;
                        }
                    }
                }
                if(aftermove[nx][ny].size != 0){
                    if (sea[i][j].size > aftermove[nx][ny].size){
                        aftermove[nx][ny].dest = sea[i][j].dest;
                        aftermove[nx][ny].speed = sea[i][j].speed;
                        aftermove[nx][ny].size = sea[i][j].size;
                    }
                }
                else{
                    aftermove[nx][ny].dest = sea[i][j].dest;
                    aftermove[nx][ny].speed = sea[i][j].speed;
                    aftermove[nx][ny].size = sea[i][j].size;
                }
                sea[i][j].dest = 0;
                sea[i][j].speed = 0;
                sea[i][j].size = 0;
            }
        }
    }
    for(int i = 1; i <= r; i++){
        for(int j = 1; j <= c; j++){
            sea[i][j].dest = 0;
            sea[i][j].size = 0;
            sea[i][j].speed = 0;
            if(aftermove[i][j].size != 0){
                sea[i][j].dest = aftermove[i][j].dest;
                sea[i][j].size = aftermove[i][j].size;
                sea[i][j].speed = aftermove[i][j].speed;
            }
        }
    }
}
int main(){
    cin >> r >> c >> m;
    int sr,sc,s,d,z;
    for(int i = 0; i < m; i++){
        cin >> sr >> sc >> s >> d >> z;
        if (d == 1 || d == 2) s %= ((r - 1) * 2);
		if (d == 3 || d == 4) s %= ((c - 1) * 2);
        sea[sr][sc].speed = s;
        sea[sr][sc].dest = d;
        sea[sr][sc].size = z;
    }
    
    for(int i = 1; i <= c; i++){
        catchshark(i);
        sharkmove();
    }

    cout << sumSize;
    return 0;
}