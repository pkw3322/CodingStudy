#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

#define INF 3000000001
using namespace std;

int n;
vector<long long> v;
long long res = INF;
long long ans[3];

int main(){
    cin >> n;
    v.resize(n);
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    sort(v.begin(),v.end());
    for(int i = 0; i < n-2; i++){
        int left = i+1,right = n-1;
        while(left < right){
            long long tem = v[i] + v[left] + v[right];
            if(abs(tem) < res){
                res = abs(tem);
                ans[0] = v[i];
                ans[1] = v[left];
                ans[2] = v[right];
            }
            if(tem < 0) left++;
            else right--;
        }
    }

    for(int i = 0; i < 3; i++)
        cout << ans[i] << " ";
    return 0;
}