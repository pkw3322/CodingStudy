#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n;

int func(vector<unsigned int>& coins,int row){
    if(row == n){
        int total = 0;
        for(int i = 0; i < n; i++){
            int column = 0;
            for (int j = 0; j < n; j++){
				if (coins[j] & (1 << i)){
					column++;
				}
			}
			total += min(column, n - column);
        }
        return total;
    }
    int unfliped = func(coins,row + 1);
    coins[row] = ~coins[row];

    int fliped = func(coins,row + 1);

    int minBack = fliped > unfliped ? unfliped : fliped;
    return minBack;
}

int main(){
    cin >> n;
    vector<unsigned int> coins(n);
    for(int i = 0; i < n; i++){
        string a;
        cin >> a;
        for(int j = 0; j < n; j++){
            if(a[j] == 'T')
                coins[i] |= (1 << j);   
        }
    }
    cout << func(coins,0);
    return 0;
}