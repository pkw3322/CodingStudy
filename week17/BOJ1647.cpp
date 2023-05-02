#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n,m,ans = 0;
int parent[100001];
vector<int> v;
vector<pair<int, pair<int,int> > > city;

int findParent(int x){
    if(x == parent[x])
        return x;
    else{
        parent[x] = findParent(parent[x]);
        return parent[x];
    }
}

void Union(int x,int y, int cost){
    int px = findParent(x);
    int py = findParent(y);

    if(px == py)
        return ;
    parent[py] = parent[px];
    n--;
}

bool isSameParent(int x,int y){
    int px = findParent(x);
    int py = findParent(y);

    if(px == py)
        return true;
    return false;
}

void solution(){
    sort(city.begin(),city.end());
    for(int i = 1; i <= n; i++)
        parent[i] = i;
    for(int i = 0; i < city.size(); i++){
        if(!isSameParent(city[i].second.first,city[i].second.second)){
            Union(city[i].second.first,city[i].second.second,city[i].first);
            v.push_back(city[i].first);
        }
    }
    for(int i = 0; i < v.size()-1; i++)
        ans += v[i];
}

int main(){
    int a,b,c;
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        cin >> a >> b >> c;
        city.push_back(make_pair(c,make_pair(a,b)));
    }

    solution();

    cout << ans;

    return 0;
}