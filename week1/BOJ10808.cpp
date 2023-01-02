#include<iostream>
#include<cstring>

using namespace std;

int main(){
    string input;
    cin >> input;
    int len = input.length();
    char* char_array = new char[len + 1];
    strcpy(char_array, input.c_str());

    int result[26];
    for(int i = 0; i < sizeof(result)/sizeof(int); i ++){
        result[i] = 0;
    }

    for(int i = 0; i < input.length(); i++){
        result[char_array[i] - 97]++;
    }
    for(int i = 0; i < sizeof(result)/sizeof(int); i ++){
        cout << result[i] << " ";
    }
    return 0;
}