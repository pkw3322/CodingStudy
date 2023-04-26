#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int n;
long long ans;
vector<pair<int,int> >v;

void solution(){
    sort(v.begin(),v.end());
    int s = v[0].first,e = v[0].second;
    for(int i = 1; i < n; i++){
        int curS = v[i].first,curE = v[i].second;
        if(e > curS){
            if(e < curE){
                e = curE;
            }
        }
        else{
            ans += (e-s);
            s = curS;
            e = curE;
        }
    }
    ans += (e-s);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    int a,b;
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        v.push_back(make_pair(a,b));
    }

    solution();
    cout << ans;
    return 0;
}