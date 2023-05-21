#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int t,n,m;
int A[1001];
int B[1001];

int main(){
    cin >> t >> n;
    for(int i = 0; i < n; i++){
        cin >> A[i];
    }
    cin >> m;
    for(int i = 0; i < m; i++){
        cin >> B[i];
    }
    vector<int> aSum, bSum;
	
	for (int i = 0; i < n; i++) {
		int sum = A[i];
		aSum.push_back(sum);
		for (int j = i + 1; j < n; j++) {
			sum += A[j];
			aSum.push_back(sum);
		}
	}

	for (int i = 0; i < m; i++) {
		int sum = B[i];
		bSum.push_back(sum);
		for (int j = i + 1; j < m; j++) {
			sum += B[j];
			bSum.push_back(sum);
		}
	}

	sort(bSum.begin(), bSum.end());

	long long ans = 0;
	for (int i = 0; i < aSum.size(); i++) {
		int target = t - aSum[i];
		int lo = lower_bound(bSum.begin(), bSum.end(), target) - bSum.begin();
		int hi = upper_bound(bSum.begin(), bSum.end(), target) - bSum.begin();
		ans += (hi - lo);
	}
    cout << ans;
    return 0;
}