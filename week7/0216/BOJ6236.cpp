#include<iostream>
#include<algorithm>

using namespace std;

long long n,m;
long long Sum = 0,low = -1,high,result = 0,total;
long long arr[100000];

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >>arr[i];
        Sum += arr[i];
    }
    high = Sum;
    low = 1;
    while(low <= high){
        long long middle = (low + high)/2;
        total = middle;
        bool check = true;
        long long cnt = 1;
        for(int i = 0; i < n; i++){
            int now = arr[i];
            if(now > middle){
                check = false;
                break;
            }
            if(now > total){
                total = middle;
                cnt++;
            }
            total = total - now;
        }
        if(!check || cnt > m) low = middle + 1;
        else{
            result = middle;
            high = middle - 1;
        }
    }
    cout << result;
    return 0;
}