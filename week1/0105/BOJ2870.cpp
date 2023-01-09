#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

bool cmp(string a, string b) {
	if (a.size() == b.size()) {
		return a < b;
	}
	return a.size() < b.size();
}

int main(){
    vector<string> ret;
    int n;
    string k;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> k;
        string tem = "";
        for(int j = 0; j < k.length(); j++){
            if (isdigit(k[j])) {
				if (tem.length() == 1 && tem == "0") {
					tem = "";
				}
				tem += k[j];
				if (j == k.length() - 1) {
					ret.push_back(tem);
					tem = "";
				}
			}
			else {
				if (tem != "") {
					ret.push_back(tem); 
				}
				tem = "";
			}
        }
    }
    sort(ret.begin(),ret.end(),cmp);
    for(vector<string>::size_type i = 0; i < ret.size(); i++) {
        cout<< ret[i] << '\n';
    }

    return 0;
}