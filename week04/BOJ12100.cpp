#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int n;
long long result = -1;

vector<vector<long long> > move_up(vector<vector<long long> >mtx){
    vector<vector<bool> >checking(n,vector<bool>(n,false));
    for(int i = 0; i < n; i++){
        for(int j = 1; j < n; j++){
            if(mtx[j][i] == 0)
                continue;
            for(int l = j-1; l >= 0; l--){
                if(mtx[l][i] == mtx[l+1][i] && !checking[l][i]){
                    mtx[l][i] *= 2;
                    checking[l][i] = true;
                    mtx[l+1][i] = 0;
                    break;
                }
                else if(mtx[l][i] == 0){
                    mtx[l][i] = mtx[l+1][i];
                    mtx[l+1][i] = 0;
                }
                else{
                    break;
                }
            }
        }
    }
    return mtx;
}


vector<vector<long long> > move_down(vector<vector<long long> >mtx){
    vector<vector<bool> >checking(n,vector<bool>(n,false));
    for(int i = 0; i < n; i++){
        for(int j = n-2; j >= 0; j--){
            if(mtx[j][i] == 0)
                continue;
            for(int l = j+1; l < n; l++){
                if(mtx[l][i] == mtx[l-1][i] && !checking[l][i]){
                    mtx[l][i] *= 2;
                    mtx[l-1][i] = 0;
                    checking[l][i] = true;
                    break;
                }
                else if(mtx[l][i] == 0){
                    mtx[l][i] = mtx[l-1][i];
                    mtx[l-1][i] = 0;
                }
                else{
                    break;
                }
            }
        }
    }
    return mtx;
}

vector<vector<long long> > move_left(vector<vector<long long> >mtx){
    vector<vector<bool> >checking(n,vector<bool>(n,false));
    for(int i = 0; i < n; i++){
        for(int j = 1; j < n; j++){
            if(mtx[i][j] == 0)
                continue;
            for(int l = j-1; l >= 0; l--){
                if(mtx[i][l] == mtx[i][l+1] && !checking[i][l]){
                    mtx[i][l] *= 2;
                    checking[i][l] = true;
                    mtx[i][l+1] = 0;
                    break;
                }
                else if(mtx[i][l] == 0){
                    mtx[i][l] = mtx[i][l+1];
                    mtx[i][l+1] = 0;
                }
                else{
                    break;
                }
            }
        }
    }
    return mtx;
}
    
vector<vector<long long> > move_right(vector<vector<long long> >mtx){
    vector<vector<bool> >checking(n,vector<bool>(n,false));
    for(int i = 0; i < n; i++){
        for(int j = n-2; j >= 0; j--){
            if(mtx[i][j] == 0)
                continue;
            for(int l = j+1; l < n; l++){
                if(mtx[i][l] == mtx[i][l-1] && !checking[i][l]){
                    mtx[i][l] *= 2;
                    mtx[i][l-1] = 0;
                    checking[i][l] = true;
                    break;
                }
                else if(mtx[i][l] == 0){
                    mtx[i][l] = mtx[i][l-1];
                    mtx[i][l-1] = 0;
                }
                else{
                    break;
                }
            }
        }
    }
    return mtx;
}

void func(int level,vector<vector<long long> > mtx){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            result = result > mtx[i][j] ? result : mtx[i][j];
        }
    }
    if(level == 5)
        return;
    func(level+1,move_up(mtx));
    func(level+1,move_down(mtx));
    func(level+1,move_left(mtx));
    func(level+1,move_right(mtx));
}

int main(){
    cin >> n;
    vector<vector <long long> >mtx(n,vector<long long>(n));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> mtx[i][j];
        }
    }
    func(0,mtx);
    cout << result;
    return 0;
}
