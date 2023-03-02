#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int ans;
string str;
int dp[2500];
int palind[2501][2501];

void func(){
    for(int i = 0; i < str.length(); i++){
        palind[i+1][i+1] = true;
    }
    for(int i = 0; i < str.length()-1; i++){
        if(str[i] == str[i+1])
            palind[i+1][i+2] = true;
    }
    for(int len = 3; len <= str.length(); len++){
        for(int start = 1; start <= str.length() - len + 1; start++){
            int end = start+len-1;
            if(str[start-1] == str[end-1])
                palind[start][end] = palind[start+1][end-1];
        }
    }
    for(int end = 1; end <= str.length(); end++){
        dp[end] = 2000000000;
        for(int start = 1; start <= end; start++){
            if(palind[start][end] == true){
                dp[end] = min(dp[end],dp[start-1]+1);
            }
        }
    }
}

int main(){
    cin >> str;

    func();
    cout << dp[str.length()];
    return 0;
}