#include<iostream>
#include<algorithm>
#include<map>
#include<queue>

using namespace std;

int a,b,c,d,ans;
int nowA,nowB;
map<pair<int,int >,int>Visit;
queue<pair<int,int> >q;

void func(){
    q.push(make_pair(0,0));
    Visit[make_pair(0,0)] = 0;
    while(!q.empty()){
        int ca = q.front().first;
        int cb = q.front().second;
        int cnt = Visit[make_pair(ca,cb)];
        q.pop();
        if(ca == c && cb == d){
            ans = cnt;
            return ;
        }

        if(Visit.count(make_pair(a,cb)) == 0){
            q.push(make_pair(a,cb));
            Visit[make_pair(a,cb)] = cnt+1;
        }
        if(Visit.count(make_pair(ca,b)) == 0){
            q.push(make_pair(ca,b));
            Visit[make_pair(ca,b)] = cnt+1;
        }

        if(Visit.count(make_pair(0,cb)) == 0){
            q.push(make_pair(0,cb));
            Visit[make_pair(0,cb)] = cnt+1;
        }
        if(Visit.count(make_pair(ca,0)) == 0){
            q.push(make_pair(ca,0));
            Visit[make_pair(ca,0)] = cnt+1;
        }

        int nA,nB;
        if(ca > b - cb){
            nA = ca + cb - b;
            nB = b;
        }
        else{
            nA = 0;
            nB = ca + cb;
        }
        if(Visit.count(make_pair(nA,nB)) == 0){
            q.push(make_pair(nA,nB));
            Visit[make_pair(nA,nB)] = cnt+1;
        }
        if(cb > a - ca){
            nA = a;
            nB = cb + ca - a;
        }
        else{
            nA = ca + cb;
            nB = 0;
        }
        if(Visit.count(make_pair(nA,nB)) == 0){
            q.push(make_pair(nA,nB));
            Visit[make_pair(nA,nB)] = cnt+1;
        }
    }
    ans = -1;
}
int main(){
    cin >> a >> b >> c >>d;

    func();
    cout << ans;
    return 0;
}