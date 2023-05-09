#include<iostream>
#include<cmath>

using namespace std;

long long powmod(long long a,long long b,long long c){
    if(b == 0) return 1;
    else if (b == 1) return a%c;
    long long temp = powmod(a,b/2,c)%c;
    if(b%2 == 0){
        return temp*temp%c;
    }
    else{
        return temp*temp%c*a%c;
    }
}
int main(){
    long long a,b,c;
    cin >> a >> b >> c;

    cout << powmod(a,b,c);
    return 0;
}