#include<iostream>
#include<cmath>

using namespace std;

double x,y;

int main(){
    cin >> x >> y;
    double z = floor(100*y/x);
    if(z >= (double)99) cout << -1;
    else{
        int ans = (int)ceil((x*z+x-100*y)/(99-z));
        cout << ans;
    }
    return 0;
}