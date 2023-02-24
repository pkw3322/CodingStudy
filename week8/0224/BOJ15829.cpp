#include<iostream>
#include<cstring>
#include<cmath>

#define mod 1234567891
using namespace std;

int l;
long long hashed = 0;
int a[51];
char c;

int main(){
    cin >> l;
    for(int i = 0; i < l; i++){
        cin >> c;
        a[i] = (int)(c-'a'+1);
    }
    long long r = 1;

    for(int i = 0; i < l; i++){
        hashed = (hashed + a[i]*r)%mod;
        r = (r*31)%mod;
    }
    cout << hashed;
    return 0;
}