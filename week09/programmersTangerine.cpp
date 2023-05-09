#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int,int> a, pair<int,int> b){
    return a.first > b.first;
}
int solution(int k, vector<int> tangerine) {
    int answer = 0;
    vector<pair<int,int> >v;
    for(int i = 0; i < tangerine.size(); i++){
        int temp = tangerine[i];
        auto it = find_if(v.begin(),v.end(),
                         [&temp](const pair<int, int>& elem){ return elem.second == temp; });
        if(it == v.end()){
            v.push_back(make_pair(1,tangerine[i]));
        }
        else{
            v[it-v.begin()].first++;
        }
    }
    sort(v.begin(),v.end(),compare);
    int idx = 0;
    while(k > 0){
        k -= v[idx].first;
        answer++;
        idx++;
    }
    return answer;
}