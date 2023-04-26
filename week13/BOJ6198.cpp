#include<iostream>
#include<algorithm>
#include<stack>

using namespace std;

int n;
int h[80001];
int dp[80001];
stack<int> s;
long long ans = 0;

void solution(){
    for(int i = 1; i <= n; i++){
        while(!s.empty()){
            if(s.top() > h[i])
                break;
            s.pop();
        }
        ans += (long long)s.size();
        s.push(h[i]);
    }
}

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> h[i];
    }
    solution();
    cout << ans;
    return 0;
}