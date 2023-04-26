#include<iostream>
#include<queue>

using namespace std;

int n;
queue<int> q;

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        q.push(i);
    }
    for(int i = 0; i < n; i++){
        int cur = q.front();
        q.pop();
        if(q.empty()){
            cout << cur;
            break;
        }
        else{
            cur = q.front();
            q.pop();
            q.push(cur);
        }
    }
    return 0;
}