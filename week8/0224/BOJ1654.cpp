#include<iostream>
#include<algorithm>

using namespace std;

unsigned int n,k,ans,maxL = 0;
unsigned int arr[1000001];

void func(unsigned int left,unsigned int right){
    unsigned int mid;
    while(left <= right){
        mid = (left+right)/2;
        int now = 0;
        for(int i = 0; i < k; i++){
            now += arr[i]/mid;
        }
        if (now >= n){
			left = mid + 1;
			ans = max(ans, mid);
		}
		else{
			right = mid - 1;
		}
    }
}

int main(){
    cin >> k >> n;
    for(int i = 0; i < k; i++){
        cin >> arr[i];
        maxL = max(maxL,arr[i]);
    }

    func(1,maxL);
    cout << ans;
    return 0;
}