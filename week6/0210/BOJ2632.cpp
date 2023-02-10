#include<iostream>
#include<cstring>

using namespace std;

int want,n,m,result = 0,sumA = 0,sumB = 0;
int pizzaA[1000];
int pizzaB[1000];
int pieceA[1000001];
int pieceB[1000001];

int main(){
    cin >> want;
    cin >> m >> n;
    for(int i = 0; i < m; i++){
        cin >> pizzaA[i];
    }
    for(int i = 0; i < n; i++){
        cin >> pizzaB[i];
    }
    memset(pieceA,0,sizeof(pieceA));
    memset(pieceB,0,sizeof(pieceB));
    for(int i = 0; i < m; i++){
        sumA += pizzaA[i];
    }
    for(int i = 0; i < n; i++){
        sumB += pizzaB[i];
    }
    pieceA[sumA] = 1;
    pieceA[0] = 1;
    pieceB[sumB] = 1;
    pieceB[0] = 1;

    for(int i = 0; i < m; i++){
        int Sum = 0;
        for(int j = 0; j < m - 1; j++){
            Sum += pizzaA[(i + j) % m];
            pieceA[Sum]++;
        }
    }
    for(int i = 0; i < n; i++){
        int Sum = 0;
        for(int j = 0; j < n - 1; j++){
            Sum += pizzaB[(i + j) % n];
            pieceB[Sum]++;
        }
    }
    for(int i = 0; i <= want; i++){
        result += pieceA[i]*pieceB[want - i];
    }
    cout << result;
    return 0;
}