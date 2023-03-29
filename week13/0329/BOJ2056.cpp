#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n,ans;
vector<int> arr[1000001];
int work[10001];

int main(){
    cin >> n;
    int a,b,c,minWork = -1;
    for(int i = 1; i <= n; i++){
        cin >> a >> b;
        
        for(int j = 0; j < b; j++){
            cin >> c;
            minWork = max(work[c],minWork);
        }
        if(minWork != -1)
            work[i] = minWork + a;
        else
            work[i] = a;
        minWork = -1;
    }
    ans = work[1];
    for(int i = 1; i <= n; i++){
        ans = max(work[i],ans);
    }
    cout << ans;
    return 0;
}