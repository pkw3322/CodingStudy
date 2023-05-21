#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int sudoku[9][9];

bool check(int x,int y){
    for(int i = 0; i < 9; i++){
        if(sudoku[x][y] == sudoku[x][i] && i != y)
            return false;
        if(sudoku[x][y] == sudoku[i][y] && i != x)
            return false;
    }
    int bx = (x/3)*3;
    int by = (y/3)*3;
    for(int i = bx; i < bx+3; i++){
        for(int j = by; j < by+3; j++){
            if(i == x && j == y)
                continue;
            if(sudoku[i][j] == sudoku[x][y])
                return false;
        }
    }
    return true;
}

void solution(int x,int y){
    if(x == 9){
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                cout << sudoku[i][j];
            }
            cout << '\n';
        }
        exit(0);
    }
    if(y == 9){
        solution(x+1,0);
        return ;
    }
    if(sudoku[x][y] == 0){
        for(int i = 1; i <= 9; i++){
            sudoku[x][y] = i;
            if(check(x,y))
                solution(x,y+1);
        }
        sudoku[x][y] = 0;
    }
    else
        solution(x,y+1);
}

int main(){
    char temp;

    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            cin >> temp;
            sudoku[i][j] = temp - '0';
        }
    }
    solution(0,0);
    return 0;
}