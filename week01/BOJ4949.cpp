#include<iostream>
#include<stack>
#include<cstring>
#include<vector>

using namespace std;


int main(){

    vector<string> result;
    while(true){
        string c,temp;
        stack<char> s;
        getline(cin, c);

        if(c[0] == '.' && c.length() == 1){
            break;
        }
        temp = "yes";
        for(int i = 0; i < c.length(); i++){
            if(c[i] == '(' || c[i] == '['){
                s.push(c[i]);
            }
            else if(c[i] == ')'){
                if(s.empty() || s.top() == '['){
                    temp = "no";
                    break;
                }
                else 
                    s.pop();
            }
            else if(c[i] == ']'){
                if(s.empty() || s.top() == '('){
                    temp = "no";
                    break;
                }
                else 
                    s.pop();
            }
        }
        if(!s.empty()) temp = "no";
        result.push_back(temp);
    }
    for(vector<string>::size_type i = 0; i < result.size(); i++) {
        cout<< result[i] <<endl;
    }
    return 0;
}