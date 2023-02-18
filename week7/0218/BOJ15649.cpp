#include<iostream>
#include<cstring>

using namespace std;

int n,m;
int arr[9];
bool Visit[9];

void func(int cnt){
    if(cnt == m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return ;
    }
    for(int i = 1; i <= n; i++){
        if(!Visit[i]){
            Visit[i] = true;
            arr[cnt] = i;
            func(cnt+1);
            Visit[i] = false;
        }
    }
}

int main(){
    cin >> n >> m;
    memset(Visit,false,sizeof(Visit));

    func(0);
}