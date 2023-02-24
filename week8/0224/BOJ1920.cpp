#include<iostream>
#include<algorithm>

using namespace std;

int n,m,k;
int a[100010];

void Search(int temp){
    int start = 0,end = n-1,mid,ans = 0;
    while(end >= start){
        mid = (start+end)/2;
        if(a[mid] == temp){
            cout << 1 << '\n';
            return ;
        }
        else if(a[mid] > temp){
            end = mid-1;
        }
        else{
            start = mid+1;
        }
    }
    cout << 0 << '\n';
}

int main(){
	cin.tie(NULL); 
    cout.tie(NULL); 
    ios_base::sync_with_stdio(false);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a,a+n);
    cin >> m;
    for(int i = 0; i < m; i++){
        cin >> k;
        Search(k);
    }
    return 0;
}