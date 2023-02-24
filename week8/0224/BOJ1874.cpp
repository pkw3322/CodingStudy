#include<iostream>
#include<stack>
#include<vector>

using namespace std;

int n,x,cnt = 0;
stack<int> s;
vector<char> v;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    s.push(cnt);
    cnt++;
    bool check = false;

    for(int i = 0; i < n; i++){
        cin >> x;
        while(s.top() < x){
            s.push(cnt);
            cnt++;
            v.push_back('+'); 
        }
        if(s.top() == x){
            s.pop();
            v.push_back('-');
        }   
        else{
            check = true;
        }
    }
    if(check)
        cout << "NO";
    else{
        for(int i = 0; i < v.size(); i++){
            cout << v[i] << '\n';
        }
    }
    return 0;
}