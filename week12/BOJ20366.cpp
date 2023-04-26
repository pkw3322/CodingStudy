#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef struct{
    int idx1,idx2,total;
}SnowMan;

int n,ans = 1e9;
vector<int> arr;
vector<SnowMan> snows;

bool cmp(const SnowMan &a,const SnowMan &b){
    return a.total < b.total;
}

void solution(){
    for(int i = 0; i < n-1; i++){
        for(int j = i+1; j < n; j++){
            SnowMan temp;
            temp.idx1 = i;
            temp.idx2 = j;
            temp.total = arr[i] + arr[j];
            snows.push_back(temp);
        }
    }
    sort(snows.begin(),snows.end(),cmp);

    for(int i = 0; i < snows.size()-1; i++){
        SnowMan anna = snows[i];
        for(int j = i+1; j < snows.size(); j++){
            SnowMan elsa = snows[j];
            if(elsa.idx1 != anna.idx1 && elsa.idx1 != anna.idx2 && elsa.idx2 != anna.idx1 && elsa.idx2 != anna.idx2){
                ans = min(ans,elsa.total - anna.total);
                break;
            }
        }
    }
}

int main(){
    cin >> n;
    arr.resize(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    solution();
    cout << ans;
    return 0;
}