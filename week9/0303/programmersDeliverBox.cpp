#include <string>
#include <vector>

using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    vector<int> sub;
    sub.push_back(0);
    int idx = 0;
    for(int i = 1; i <= order.size(); i++){
        if(order[idx] == i){
            idx++;
        }
        else if(order[idx] == sub.back()){
            sub.pop_back();
            idx++;
            i--;
        }
        else{
            sub.push_back(i);
        }
    }
    
    while(sub.size() != 1){
        if(sub.back() == order[idx]){
            idx++;
            sub.pop_back();
        }
        else
            break;
    }
    answer = idx;
    return answer;
}