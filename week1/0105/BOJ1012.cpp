#include<iostream>
#include<cmath>
#include<cstring>

using namespace std;

int n,m,k;
int matrix[50][50];
bool visits[50][50];

void area(int i, int j){
    visits[i][j] = true;
    matrix[i][j] = 0;
    if(i < 50 && j < 50){
        if(i<49)
            if(!visits[i+1][j] && matrix[i+1][j])
                area(i+1,j);
        if(j<49)
            if(!visits[i][j+1] && matrix[i][j+1])
                area(i,j+1);
        if(i>0)
            if(!visits[i-1][j] && matrix[i-1][j])
                area(i-1,j);
        if(j>0)
            if(!visits[i][j-1] && matrix[i][j-1])
                area(i,j-1);   
    }
}
int main(){
    int t,x,y;
    cin >> t;
    int results[t];
    for(int te = 0; te < t; te++){
        cin >> m >> n >> k;
        memset(visits,false,sizeof(visits));
        memset(matrix,0,sizeof(matrix));
        for(int i = 0; i < k; i++){
            cin >> x >> y;
            matrix[y][x] = 1;
        }
        results[te] = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(!visits[i][j] && matrix[i][j]){
                    results[te]++;
                    area(i,j);
                }
            }
        }
    }
    for(int i = 0; i < t; i++){
        cout << results[i] << '\n';
    }
    return 0;
}