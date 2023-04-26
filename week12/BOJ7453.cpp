#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n;
long long ans = 0;
int A[4001],B[4001],C[4001],D[4001];
vector<int> AB;
vector<int> CD;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            AB.push_back(A[i]+B[j]);
            CD.push_back(C[i]+D[j]);
        }
    }
    
    sort(AB.begin(),AB.end());
    sort(CD.begin(),CD.end());

    for(int i = 0; i < AB.size(); i++){
        int idx = lower_bound(CD.begin(),CD.end(),-AB[i])-CD.begin();
        int pidx = upper_bound(CD.begin(),CD.end(),-AB[i])-CD.begin();
        
        ans += (pidx - idx);
    }
    cout << ans;
    return 0;
}