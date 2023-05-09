#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

int r,c,cnt = 0,firstR = -1,firstC = -1;
char lake[1500][1500];
bool visitd[1500][1500];
int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};

bool checking(){
    return true;
}
void func(){
    while(true){
        if(checking()){
            cout << cnt;
            return ;
        }

        cnt++;
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
            if(char_array[j] == 'L' && firstR == -1){
                firstR = i;
                firstC = j;
            }
            lake[i][j] = char_array[j];
        }
    }
    func();
    return 0;
}