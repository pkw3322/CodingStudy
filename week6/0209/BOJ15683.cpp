#include<iostream>

using namespace std;

int n,m,minSpace = 999999,cameraSize = 0;
int arr[8][8];
int rotateType[5] = {4,2,4,4,1};
pair<pair<int,int>, int> cameras[8];

int Count(){
    int c = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(arr[i][j] == 0) c++;
        }
    }
    return c;
}

void copy(int from[8][8],int to[8][8]){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            to[i][j] = from[i][j];
        }
    }
}

void update(int direct,pair<pair<int,int>, int> camera){
    direct %= 4;
    if(direct == 0){
        for(int i = camera.first.second + 1; i < m; i++){
            if(arr[camera.first.first][i] == 6) break;
            if(arr[camera.first.first][i] > 0) continue;
            arr[camera.first.first][i] = -1;
        }
    }
    if(direct == 1){
        for(int i = camera.first.first - 1; i >= 0; i--){
            if(arr[i][camera.first.second] == 6) break;
            if(arr[i][camera.first.second] > 0) continue;
            arr[i][camera.first.second] = -1;
        }
    }
    if(direct == 2){
        for(int i = camera.first.second - 1; i >= 0; i--){
            if(arr[camera.first.first][i] == 6) break;
            if(arr[camera.first.first][i] > 0) continue;
            arr[camera.first.first][i] = -1;
        }
    }
    if(direct == 3){
        for(int i = camera.first.first + 1; i < n; i++){
            if(arr[i][camera.first.second] == 6) break;
            if(arr[i][camera.first.second] > 0) continue;
            arr[i][camera.first.second] = -1;
        }
    }
}

void func(int cnt){
    if(cnt == cameraSize){
        int now = Count();
        minSpace = minSpace > now ? now : minSpace;
        return ;
    }
    int backup[8][8];
    for(int direct = 0; direct < rotateType[cameras[cnt].second]; direct++){
        copy(arr,backup);
        if(cameras[cnt].second == 0){
            update(direct,cameras[cnt]);
        }
        if(cameras[cnt].second == 1){
            update(direct,cameras[cnt]);
            update(direct+2,cameras[cnt]);
        }
        if(cameras[cnt].second == 2){
            update(direct,cameras[cnt]);
            update(direct+1,cameras[cnt]);
        }
        if(cameras[cnt].second == 3){
            update(direct,cameras[cnt]);
            update(direct+1,cameras[cnt]);
            update(direct+2,cameras[cnt]);
        }
        if(cameras[cnt].second == 4){
            update(direct,cameras[cnt]);
            update(direct+1,cameras[cnt]);
            update(direct+2,cameras[cnt]);
            update(direct+3,cameras[cnt]);
        }
        func(cnt+1);
        copy(backup,arr);
    }
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> arr[i][j];
            if(arr[i][j] != 0 && arr[i][j] != 6){
                cameras[cameraSize].first.first = i;
                cameras[cameraSize].first.second = j;
                cameras[cameraSize].second = arr[i][j]-1;
                cameraSize++;
            }
        }
    }
    func(0);
    cout << minSpace;
    return 0;
}