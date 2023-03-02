#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

long long n,c,ans;
long long things[31];
vector<long long> vL;
vector<long long> vR;

void func(int start,int end,vector<long long>& v,long long total){
    if(start > end){
        v.push_back(total);
        return ;
    }
    else{
        func(start+1,end,v,total+things[start]);
        func(start+1,end,v,total);
    }
}

int main(){
    cin >> n >> c;
    for(int i = 0; i < n; i++){
        cin >> things[i];
    }

    func(0,n/2,vL,0);
    func(n/2+1,n-1,vR,0);
    
    sort(vR.begin(),vR.end());

    for(int i = 0; i < vL.size(); i++){
        ans += upper_bound(vR.begin(),vR.end(),c-vL[i]) - vR.begin();
    }
    cout << ans;
}