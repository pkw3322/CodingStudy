#include<iostream>
#include<algorithm>

using namespace std;

int n,ans;
pair<int,int> aggs[8];

void solution(int idx){
    if(idx == n){
        int cnt = 0;
        for(int i = 0; i < n; i++){
            if(aggs[i].first <= 0)cnt++;
        }
        ans = max(ans,cnt);
        return ;
    }

    if(aggs[idx].first <= 0)
        solution(idx+1);
    else{
        bool flag = false;
        for(int i = 0; i < n; i++){
            if(i == idx || aggs[i].first <= 0)
                continue;
            aggs[i].first -= aggs[idx].second;
            aggs[idx].first -= aggs[i].second;

            flag = true;
            solution(idx+1);

            aggs[i].first += aggs[idx].second;
            aggs[idx].first += aggs[i].second;
        }
        if(!flag)
            solution(n);
    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> aggs[i].first >> aggs[i].second;
    }
    solution(0);
    cout << ans;
    return 0;
}