#include<iostream>
#include<vector>

using namespace std;

vector<int> v;

int gcd(int a, int b) {
    return a % b ? gcd(b, a%b) : b;
}
int calc(int a, int b) {
    int i = 1, g;
    while (a != 1) {
        i = (b%a == 0) ? (b / a) : (b / a + 1);
        a = a * i - b;
        b = b * i;
        g = gcd(a, b); 
        a /= g; 
        b /= g;
    }
    return b;
}

int main(){
    int time;
    int denomin,numer;
    cin >> time;
    for(int i = 0; i < time; i++){
        cin >> numer >> denomin;
        v.push_back(calc(numer,denomin));
    }
    for(vector<int>::size_type i = 0; i < v.size(); i++) {
        cout<< v[i] << '\n';
    }
    return 0;
}