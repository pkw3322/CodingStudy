#include<iostream>
#include<cmath>

using namespace std;

int main(){
    int n,k,result;
    while(cin >> n){
        k = 1;
        result = 1;
        while(true){
            if(result % n == 0) break;
            else{
                k++;
                result = result*10 + 1;
                result %= n;
            }
        }
        cout << k << '\n';
    }
    return 0;
}