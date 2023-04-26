#include<iostream>
#include<vector>
#include<cstring>
#include<queue>
#include<cmath>

using namespace std;

int n,l,cnt = 0;
int road[101][101];
int roadVer2[101][101];

bool canMake(int arr[][101],int ci,int cj){
    int stand = arr[ci][cj+1];
    for (int j = cj + 1; j < cj + 1 + l; j++){
        if (arr[ci][j] != stand) 
            return false;
    }
    return true;
}

int checking(int arr[][101]){
    int total = 0;
    for (int i = 0; i < n; i++){
        int before = 1;
        bool checkRoad = true;
        for(int j = 0; j < n-1; j++){
            if(arr[i][j] == arr[i][j+1])
                before += 1;
            else if(arr[i][j] == arr[i][j+1] + 1){
                if(canMake(arr,i,j)){
                    j = j + l-1;
                    before = 0;
                }
                else{
                    checkRoad = false;
                    break;
                }
            }
            else if(arr[i][j] + 1 == arr[i][j+1]){
                if(before >= l)
                    before = 1;
                else{
                    checkRoad = false;
                    break;
                }
            }
            else if(abs(arr[i][j] - arr[i][j+1]) >= 2){
                checkRoad = false;
                break;
            }
        }
        if(checkRoad){
            total += 1;
        }
    }
    
    return total;
}


void func(){
    //horizontal
    int hor = checking(road);
    //vertical
    int vertic = checking(roadVer2);

    cnt = hor + vertic;
}

int main(){
    cin >> n >> l;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> road[i][j];
            roadVer2[j][i] = road[i][j];
        }
    }
    func();
    cout << cnt;
    return 0;
}