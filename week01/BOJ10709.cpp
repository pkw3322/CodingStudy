#include<iostream>

using namespace std;

int main(){
    int h,w,temp;
    cin >> h >> w;
    char input[h][w];
    for(int i = 0; i < h; i++)
        for(int j = 0; j < w; j++)
            cin >> input[i][j];
            
    for(int i = 0; i < h; i++){
        temp = -1;
        for(int j = 0; j < w; j++){
            if(input[i][j] == 'c'){
                temp = 0;
            }
            else if(temp > -1){
                temp += 1;
            }
            cout << temp << ' ';
        }
        cout << '\n';
    }
    return 0;
}