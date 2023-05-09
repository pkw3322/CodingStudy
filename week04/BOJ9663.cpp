#include<iostream>

using namespace std;

int n,cnt=0;
int posible[15];

bool checkposible(int idx){
    for(int i = 0; i < idx; i++){
        if(posible[idx] == posible[i] || idx-i == abs(posible[idx] - posible[i]))
            return false;
    }
    return true;
}
void func(int idx){
    if(idx == n){
        cnt++;
        return ;
    }
    for(int i = 0; i < n; i++){
        posible[idx] = i;
        if(checkposible(idx))
            func(idx+1);
    }
}

int main(){
    cin >> n;
    func(0);
    cout << cnt;
    return 0;
}