#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>

#define INF 3000000001

using namespace std;

int n;
vector<long long> arr;
long long res = INF;
long long ans[2];

void solution(){
    int start = 0,end = n-1;
    while(start < end){
        int temp = arr[start] + arr[end];
        if(abs(temp) < res){
            res = abs(temp);
            ans[0] = arr[start];
            ans[1] = arr[end];
        }
        if(temp < 0)
            start++;
        else
            end--;
    }
}

int main(){
    cin >> n;
    arr.resize(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    solution();
    cout << ans[0] << " " << ans[1] <<'\n';
    return 0;
}