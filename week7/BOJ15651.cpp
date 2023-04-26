#include<iostream>

using namespace std;

int n,m;
int arr[8];
void func(int cnt){
    if(cnt == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return ;
    }
    for(int i = 1; i <= n; i++){
        arr[cnt] = i;
        func(cnt+1);
    }
}

int main(){
    cin >> n >> m;

    func(0);

    return 0;
}