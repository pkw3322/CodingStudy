#include <iostream>
#include <algorithm>

using namespace std;

int n,q, a, b;
int arr[2001];
bool dp[2001][2001] = { false, };

int main()
{
	cin.tie(NULL); 
    cout.tie(NULL); 
    ios_base::sync_with_stdio(false);
	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}

	for (int i = 1; i <= n - 1; i++) {
		if (arr[i] == arr[i + 1])
			dp[i][i + 1] = true;
	}

	for (int i = 1; i <= n; i++) {
		dp[i][i] = true;
	}

	for (int i = n - 1; i >= 1; i--) {
		for (int j = i + 2; j <= n; j++) {
			if (arr[i] == arr[j] && dp[i+1][j-1] == true) {
				dp[i][j] = true;
			}
		}
	}

	cin >> q;

	for (int i = 0; i < q; i++) {
		cin >> a >> b;
		cout << dp[a][b] << '\n';
	}

	return 0;
}