#include <string>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

bool error[10];

bool check(int now){
    string str = to_string(now);
    for(int i = 0; i <str.length();i++){
        if(error[str[i]-48]){
            return false;
        }
    }
    return true;
}

int main(){
    int n,m;
    cin>>n>>m;
    int tmp;
    memset(error,false,sizeof(error));

    for(int i = 0; i < m; i++){
        cin>>tmp;
        error[tmp] = true;
    }

    string st = to_string(n);

    int mins = abs(n-100);
    for(int i = 0; i <= 1000000; i++){
        if(check(i)){
            int tmp = abs(n-i) + to_string(i).length();
            mins = min(mins,tmp);
        }
    }
    cout<<mins;
    return 0;
}