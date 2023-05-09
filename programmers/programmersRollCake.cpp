#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    int type = 0,old,young;
    vector<int> eachTopping(1000001,0);
    vector<int> checking(1000001,0);
    vector<int> olderHave(1000001,0);
    for(int i = 0; i < topping.size(); i++){
        eachTopping[topping[i]]++;
        if(!checking[topping[i]]){
            type++;
            checking[topping[i]] = 1;
            
        }
    }
    old = 0;
    young = type;
    
    for(int i = 0; i < topping.size(); i++){
        if(old > young)
            break;
        if(old == young)
            answer++;
        if(!olderHave[topping[i]])
            old++;
        olderHave[topping[i]]++;
        if(olderHave[topping[i]] == eachTopping[topping[i]])
            young--;
    }
    
    return answer;
}