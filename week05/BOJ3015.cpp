#include<iostream>
#include<stack>

using namespace std;

int n;
stack<pair<int,int> > s;

int main(){
    cin >> n;
    long long cnt = 0;
    int cur,cn;
    for(int i = 0; i < n; i++){
        cin >> cur;
        cn = 1;
        while(!s.empty() && s.top().first < cur){
            cnt += s.top().second;
            s.pop();
        }
        if(!s.empty()){
            if(s.top().first == cur){
                cnt += s.top().second;
                cn = (s.top().second +1 );
                if(s.size() >1)
                    cnt++;
                s.pop();
            }
            else{
                cnt++;
            }  
        }
          
        s.push(make_pair(cur,cn));
    }
    cout << cnt;
    return 0;
}