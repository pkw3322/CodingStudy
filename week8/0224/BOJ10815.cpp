#include<iostream>
#include<algorithm>

using namespace std;

int n,m,k;
int arr[500010];

void binarySearch(int ke){
    int start = 0,end = n-1,mid;
    while(start <= end){
        mid = (start+end)/2;
        if(arr[mid] == ke){
            cout << 1 << " ";
            return ;
        }
        else if(arr[mid] > ke){
            end = mid-1;
        }
        else{
            start = mid+1;
        }
    }
    cout << 0 << " ";
}

int main(){
	cin.tie(NULL); 
    cout.tie(NULL); 
    ios_base::sync_with_stdio(false);
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr,arr+n);
    cin >> m;
    for(int i = 0; i < m; i++){
        cin >> k;
        binarySearch(k);
    }
    return 0;
}