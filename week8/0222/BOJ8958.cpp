#include<iostream>
#include<cstring>
#include<vector>

using namespace std;

int cnt;
vector<int> ans;

void printAll(){
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << '\n';
    }
}

void cal(string str){
    int ret = 0;
    int coun = 0;
    for(int i = 0; i < str.length(); i++){
        if(str.at(i) == 'X'){
            coun = 0;
        }
        else{
            coun++;
            ret += coun;
        }
    }
    ans.push_back(ret);
}

int main(){
    cin >> cnt;

    while(cnt > 0){
        string str;
        cin >> str;
        cal(str);
        cnt--;
    }

    printAll();
}