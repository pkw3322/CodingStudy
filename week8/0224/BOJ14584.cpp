#include<iostream>
#include<string>

using namespace std;

int n;
string str;
string words[20];

void func(){
    for(int i = 0; i < 25; i++){
        for(int j = 0; j < n; j++){
            if(str.find(words[j]) != string::npos){
                cout << str << '\n';
                return ;
            }
        }
        for(int j = 0; j < str.length(); j++){
            str[j] = (str[j] - 'a' + 1)%26 + 'a';
        }
    }
}

int main(){
    cin >> str;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> words[i];
    }

    func();
    
    return 0;
}