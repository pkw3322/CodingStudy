#include<iostream>
#include<algorithm>

using namespace std;

int subsum(int arr[],int idx,int k){
    int sum = 0;
    for(int i = idx; i < idx + k; i++)
        sum += arr[i];
    return sum;
}
int main(){
    int n,k;
    cin >> n >> k;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    int sum = -10000000;
    for(int i = 0; i <= n-k; i++){
        sum = max(sum,subsum(arr,i,k));
    }
    cout << sum;
    return 0;
}