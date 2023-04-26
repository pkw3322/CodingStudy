#include<iostream>
#include <algorithm>
#include<cmath>
#include<queue>
#include<cstring>

using namespace std;

int n,m;
bool visited[100][100];
int result[100][100];
int matrix[100][100];
queue<pair<int,int> > q;

void findMin(int i,int j){
    int x,y;
    visited[i][j] = true;
    result[i][j] += 1;
    q.push(make_pair(i,j));
    
    while(!q.empty()){
        x = q.front().first;
        y = q.front().second;
        q.pop();

        if(0 < x && x < 100 && y < 100 && !visited[x-1][y] && matrix[x-1][y]){
            visited[x-1][y] = true;
            q.push(make_pair(x-1,y));
            result[x-1][y] = result[x][y] + 1;
        }

        if(0 < y && x < 100 && y < 100 && !visited[x][y-1] && matrix[x][y-1]){
            visited[x][y-1] = true;
            q.push(make_pair(x,y-1));
            result[x][y-1] = result[x][y] + 1;
        }

        if(0 <= x && x < 99 && y < 100 && !visited[x+1][y] && matrix[x+1][y]){
            visited[x+1][y] = true;
            q.push(make_pair(x+1,y));
            result[x+1][y] = result[x][y] + 1;
        }

        if(0 <= y && x < 100 && y < 99 && !visited[x][y+1] && matrix[x][y+1]){
            visited[x][y+1] = true;
            q.push(make_pair(x,y+1));
            result[x][y+1] = result[x][y] + 1;
        }        
    }
}

int main(){
    cin >> n >> m;
    string tmp;
    char t[m];
    for(int i = 0; i < n; i++){
        cin >> tmp;
        int len = tmp.length();
        char* char_array = new char[len + 1];
        strcpy(char_array, tmp.c_str());
        for(int j = m-1; j >= 0; j--){
            matrix[i][j] = int(char_array[j]-'0');
        }
    }
    for(int i = 0; i < 100; i++)
        for(int j = 0; j < 100; j++){
            visited[i][j] = false;
        }

    findMin(0,0);
    cout << result[n-1][m-1];
    return 0;
}