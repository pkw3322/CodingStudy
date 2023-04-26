#include<iostream>
#include<cstring>

using namespace std;

int c;
int score = 0;
int cnt = 0;
int blue[4][6];
int green[6][4];

void checkAndRemove(){
    for(int i = 0; i < 2; i++){
        bool checker = false;
        for(int j = 0; j < 4; j++){
            if(green[i][j] == 1){
                checker = true;
                break;
            }
        }
        if(checker){
            for(int k = 5; k > 0; k--){
                for(int l = 0; l < 4; l++){
                    green[k][l] = green[k-1][l];
                }
            }
            for(int k = 0; k < 4; k++){
                green[0][k] = 0;
            }
        }
    }
    for(int j = 0; j < 2; j++){
        bool checker = false;
        for(int i = 0; i < 4; i++){
            if(blue[i][j] == 1){
                checker = true;
                break;
            }
        }
        if(checker){
            for(int k = 5; k > 0; k--){
                for(int l = 0; l < 4; l++){
                    blue[l][k] = blue[l][k-1];
                }
            }
            for(int k = 0; k < 4; k++){
                blue[k][0] = 0;
            }
        }
    }
}

void isFull(){
    for(int i = 2; i < 6; i++){
        bool checker = true;
        for(int j = 0; j < 4; j++){
            if(green[i][j] == 0){
                checker = false;
                break;
            }
        }
        if(checker){
            score++;
            for(int k = i; k > 0; k--){
                for(int l = 0; l < 4; l++){
                    green[k][l] = green[k-1][l];
                }
            }
            for(int k = 0; k < 4; k++){
                green[0][k] = 0;
            }
        }
    }
    
    for(int j = 2; j < 6; j++){
        bool checker = true;
        for(int i = 0; i < 4; i++){
            if(blue[i][j] == 0){
                checker = false;
                break;
            }
        }
        if(checker){
            score++;
            for(int k = j; k > 0; k--){
                for(int l = 0; l < 4; l++){
                    blue[l][k] = blue[l][k-1];
                }
            }
            for(int k = 0; k < 4; k++){
                blue[k][0] = 0;
            }
        }
    }
}

void move(int t,int x,int y){
    if(t == 1){
        int i = 0;
        for(; i < 6; i++){
            if(green[i][y] == 1){
                break;
            }
        }
        if(i == 5 && green[i][y] == 0){
            green[i][y] = 1;
        }
        else{
            green[i-1][y] = 1;
        }
        i = 0;
        for(; i < 6; i++){
            if(blue[x][i] == 1){
                break;
            }
        }
        if(i == 5 && blue[x][i] == 0){
            blue[x][i] = 1;
        }
        else{
            blue[x][i-1] = 1;
        }
    }
    else if(t == 2){
        int i = 0;
        for(; i < 6; i++){
            if(green[i][y] == 1 || green[i][y+1] == 1){
                break;
            }
        }
        if(i == 5 && green[i][y] == 0 && green[i][y+1] == 0){
            green[i][y] = 1;
            green[i][y+1] = 1;
        }
        else{
            green[i-1][y] = 1;
            green[i-1][y+1] = 1;
        }
        i = 0;
        for(; i < 6; i++){
            if(blue[x][i] == 1){
                break;
            }
        }
        if(i == 5 && blue[x][i] == 0){
            blue[x][i] = 1;
            blue[x][i-1] = 1;
        }
        else{
            blue[x][i-1] = 1;
            blue[x][i-2] = 1;
        }
    }
    else if(t == 3){
        int i = 0; 
        for(; i < 6; i++){
            if(green[i][y] == 1){
                break;
            }
        }
        if(i == 5 && green[i][y] == 0){
            green[i][y] = 1;
            green[i-1][y] = 1;
        }
        else{
            green[i-1][y] = 1;
            green[i-2][y] = 1;
        }
        i = 0;
        for(; i < 6; i++){
            if(blue[x][i] == 1 || blue[x+1][i] == 1){
                break;
            }
        }
        if(i == 5 && blue[x][i] == 0 && blue[x+1][i] == 0){
            blue[x][i] = 1;
            blue[x+1][i] = 1;
        }
        else{
            blue[x][i-1] = 1;
            blue[x+1][i-1] = 1;
        }
    }
    isFull();
    checkAndRemove();
}

int main(){
    cin >> c;
    memset(blue,0,sizeof(blue));
    memset(green,0,sizeof(green));
    int t,x,y;
    while(c > 0){
        cin >> t >> x >> y;
        move(t,x,y);
        c--;
    }
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 6; j++){
            if(blue[i][j] == 1)
                cnt++;
            if(green[j][i] == 1)
                cnt++;
        }
    }
    cout << score << '\n' << cnt << '\n';

}