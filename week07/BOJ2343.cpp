#include<iostream>
#include<algorithm>

using namespace std;

long long n,m;
long long Sum = 0,low = -1, high;
long long arr[100000];


int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
        Sum += arr[i];
        low = max(low,arr[i]);
    }
    high = Sum;
    while(low <= high){
        long long cnt = 0,temp = 0;
        long long middle = (low + high)/2;

        for(int i = 0; i < n; i++){
            if(temp + arr[i] > middle){
                temp = 0;
                cnt += 1;
            }
            temp = temp + arr[i];
        }
        if(temp != 0) cnt += 1;

        if(cnt <= m) high = middle - 1;
        else low = middle + 1;
    }

    cout << low;
    return 0;
}