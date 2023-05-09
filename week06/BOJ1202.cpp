#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

int n,k;
long long maxPrice;
pair<int,int> jewelInfo[300001];
int bag[300001];
priority_queue<int, vector<int>, less<int> > pq;

int main(){
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        int weight,price;
        cin >> jewelInfo[i].first >> jewelInfo[i].second;
    }
    for(int i = 0; i < k; i++){
        cin >> bag[i];
    }
    sort(jewelInfo,jewelInfo + n);
    sort(bag,bag+k);
    int index = 0;
    for(int i = 0; i < k; i++){
        while(index < n && jewelInfo[index].first <= bag[i]){
            pq.push(jewelInfo[index].second);
            index++;
        }
        if(!pq.empty()){
            maxPrice += pq.top();
            pq.pop();
        }
    }
    cout << maxPrice;
    return 0;
}