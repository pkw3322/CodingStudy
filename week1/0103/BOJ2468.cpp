#include<iostream>
#include<cmath>

using namespace std;

int len;
bool visited[100][100];

void change(int tmp[][100],int i,int j){
    visited[i][j] = true;
    tmp[i][j] = 0;
    if(i < 100 && j < 100){
        if(i<99)
            if(!visited[i+1][j] && tmp[i+1][j])
                change(tmp,i+1,j);
        if(j<99)
            if(!visited[i][j+1] && tmp[i][j+1])
                change(tmp,i,j+1);
        if(i>0)
            if(!visited[i-1][j] && tmp[i-1][j])
                change(tmp,i-1,j);
        if(j>0)
            if(!visited[i][j-1] && tmp[i][j-1])
                change(tmp,i,j-1);   
    }
}
int main(){
    cin >> len;
    int input[len][len];
    int maxHeight = -1;
    int tmp[100][100];
    for(int i = 0; i < 100; i++)
            for(int j = 0; j < 100; j++)
                tmp[i][j] = 0;

    for(int i = 0; i < len; i++)
        for(int j = 0; j < len; j++){
            cin >> input[i][j];
            maxHeight = maxHeight>input[i][j]?maxHeight:input[i][j];
        }

    int area[101];
    for(int l = 1; l <= maxHeight; l++){
        area[l] = 0;

        for(int i = 0; i < 100; i++)
            for(int j = 0; j < 100; j++)
                visited[i][j] = false;
        
        for(int i = 0; i < len; i++)
            for(int j = 0; j < len; j++){
                if(input[i][j] < l) tmp[i][j] = 0;
                else tmp[i][j] = 1;
            }

        for(int i = 0; i < len; i++)
            for(int j = 0; j < len; j++){
                if(!visited[i][j] && tmp[i][j] == 1){
                    area[l] += 1;
                    change(tmp, i, j);
                }
            }
    }
    
    int num = -1;
    for(int l = 1; l <= maxHeight; l++)
        num = num>area[l]?num:area[l];

    cout << num;
    return 0;
}