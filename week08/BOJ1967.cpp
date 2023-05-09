#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

int n,parent,child,weight,r = 0,endPoint = 0;
vector<pair<int,int> > trees[10002];
bool Visit[10002] = {false, };

void func(int point,int length){
    if(Visit[point]) return;

    Visit[point] = true;

    if(r < length){
        r = length;
        endPoint = point;
    }
    for(int i = 0; i < trees[point].size(); i++){
        func(trees[point][i].first,length + trees[point][i].second);
    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n-1; i++){
        cin >> parent >> child >> weight;
        trees[parent].push_back(make_pair(child,weight));
        trees[child].push_back(make_pair(parent,weight));
    }
    
    func(1,0);
    r = 0;
    memset(Visit,false,sizeof(Visit));
    func(endPoint,0);
    cout << r;
    return 0;
}