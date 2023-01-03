#include<iostream>
#include<cstring>

#define YES "DA"
#define NO "NE"

using namespace std;

int main(){
    int len;
    string pattern;
    cin >> len;
    cin >> pattern;
    int idx = pattern.find('*');
    string front = pattern.substr(0,idx);
    string back = pattern.substr(idx+1);
    string list[len];
    for(int i = 0; i < len; i++){
        cin >> list[i];
    }
    for(int i = 0; i < len; i++){
        if(pattern.length() - 1 > list[i].length())
            cout << NO << '\n';
        else if(list[i].find(front) == 0 && list[i].rfind(back)+back.length() == list[i].length())
            cout << YES << '\n';
        else
            cout << NO << '\n';
    }
    return 0;
}