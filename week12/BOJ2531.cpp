#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

int n,d,k,c;
int flag,cnt,cFlag,ans = 0;
vector<int> arr;
int checking[3001];

int main(){
    cin >> n >> d >> k >> c;
    arr.resize(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    memset(checking,0,sizeof(checking));
    for(int i = 0; i < n; i++){
        flag = 0;
        cFlag = 1;
        for(int j = i; j < i+k; j++){
            if(checking[arr[j%n]] == 1)
                flag++;
            else
                checking[arr[j%n]] = 1;

            if(arr[j%n] == c)
                cFlag = 0;
        }
        ans = max(ans,k-flag+cFlag);
        memset(checking,0,sizeof(checking));
    }
    cout << ans;
    return 0;
}