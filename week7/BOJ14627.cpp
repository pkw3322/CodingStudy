#include<iostream>
#include<algorithm>

using namespace std;

long long s,c;
long long Sum = 0,low = -1,high,ans = 0;
long long arr[1000000];

int main(){
    cin >> s >> c;
    for(int i = 0; i < s; i++){
        cin >> arr[i];
        Sum += arr[i];
    }
    low = 1;
    high = 1000000000;
    while(low <= high){
        long long middle = (low + high)/2;
        long long cnt = 0;
        for(int i = 0; i < s; i++){
            cnt = cnt + arr[i]/middle;
        }
        if(cnt >= c){
            low = middle + 1;
            ans = middle;
        }
        else{
            high = middle - 1;
        }
    }
    ans = Sum - ans*c;
    cout << ans;
    return 0;
}