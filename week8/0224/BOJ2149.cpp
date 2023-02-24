#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int r;
string k,encrypt;
vector<pair<char,int> >key;
string decrypt[102][102];

void decryption(string encrypt){
    for(int i = 0; i < k.length(); i++){
        for(int j = 0; j < r; j++){
            decrypt[key[i].second][j] = encrypt[i*r + j];
        }
    }
}

int main(){
    cin >> k >> encrypt;
    for(int i = 0; i < k.length(); i++){
        key.push_back(make_pair(k[i],i));
    }
    sort(key.begin(),key.end());
    r = encrypt.length()/k.length();
    decryption(encrypt);
    for(int j = 0; j < r; j++){
        for(int i = 0; i < k.length(); i++){
            cout << decrypt[i][j];
        }
    }
    return 0;
}