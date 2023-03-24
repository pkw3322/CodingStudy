#include<iostream>
#include<vector>

using namespace std;

int n,ans;
vector<bool> arr(4000001,true);
vector<int> primes;

void makeArr(){
    for (int i = 2; i*i <= n; i++){
        if(!arr[i])
            continue;
        for(int j = i+i; j <= n; j += i){
            arr[j] = false;
        }
    }
    for(int i = 2; i <= n; i++){
        if(arr[i])
            primes.push_back(i);
    }
}

void solution(){
    int start = 0,end = 0;
    int sum = 0;
    while(true){
        if(sum > n){
            sum -= primes[start];
            start++;
        }
        else if(sum < n){
            if(end >= primes.size()) break;
            sum += primes[end];
            end++;
        }
        else{
            ans++;
            if(end >= primes.size()) break;
            sum += primes[end];
            end++;
        }
    }
}

int main(){
    cin >> n;
    makeArr();
    solution();
    cout << ans;
    return 0;
}