#include<iostream>

using namespace std;

int n,m;
int arr[8];
void func(int cnt,int start){
    if(cnt == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return ;
    }
    for(int i = start; i <= n; i++){
        arr[cnt] = i;
        func(cnt+1,i);
    }
}

int main(){
    cin >> n >> m;

    func(0,1);

    return 0;
}