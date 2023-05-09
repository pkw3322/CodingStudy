#include<iostream>
#include<algorithm>
#include<queue>
#include<cstring>
#include<vector>

using namespace std;

int r,c,ret = -1;
char arr[20][20];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
bool alpha[26] = {false};


void func(int cx, int cy,int cnt){
    ret = ret > cnt ? ret : cnt;
    for(int i = 0; i < 4; i++){
        int nx = cx + dx[i];
        int ny = cy + dy[i];
        if(!alpha[(int)arr[nx][ny] - 65] && nx >= 0 && nx < r && ny >= 0 && ny < c){
            alpha[(int)arr[nx][ny] - 65] = true;
            func(nx,ny,cnt+1);
            alpha[(int)arr[nx][ny] - 65] = false;
        }
    }
}

int main(){
    cin >> r >> c;
    string tmp;
    for(int i = 0; i < r; i++){
        cin >> tmp;
        int len = tmp.length();
        char* char_array = new char[len + 1];
        strcpy(char_array, tmp.c_str());
        for(int j = c-1; j >= 0; j--){
            arr[i][j] = char_array[j];
        }
    }
    alpha[(int)arr[0][0] - 65] = true;
    func(0,0,1);
    cout << ret;

    return 0;
}