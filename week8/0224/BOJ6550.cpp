#include<iostream>
#include<string>

using namespace std;

void checking(string s,string t){
    int idxA = 0;
    bool isTrue = false;
    for(int i = 0; i < t.length(); i++){
        if(s[idxA] == t[i]){
            idxA++;
        }
        if(idxA == s.length()){
            isTrue = true;
            break;
        }
    }
    if(isTrue)
        cout << "Yes\n";
    else
        cout << "No\n";
    return ;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

    string s,t;
    while(cin >> s >> t){
        checking(s,t);
    }
    return 0;
}