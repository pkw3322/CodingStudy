#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n,ans = 0;
vector<int> v;

int u[1005];

bool binarySearch(int num){
    int start = 0,end = v.size()-1,mid;
    while(start <= end){
        mid = (start+end)/2;
        if(v[mid] == num){
            return true;
        }
        else if(v[mid] > num){
            end = mid - 1;
        }
        else{
            start = mid + 1;
        }
    }
    return false;
}

void solution(){
    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++){
            v.push_back(u[i] + u[j]);
        }
    }
    sort(v.begin(),v.end());

    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(binarySearch(u[j]-u[i]))
                ans = max(ans,u[j]);
        }
    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> u[i];
    }
    sort(u,u+n);

    solution();

    cout << ans;
    return 0;
}