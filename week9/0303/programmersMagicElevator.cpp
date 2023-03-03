#include <string>
#include <vector>

using namespace std;



int solution(int storey) {
    int answer = 0;
    while(storey != 0){
        int nex = (storey/10) % 10;
        int cur = storey % 10;
        if(cur > 5){
            storey += 10;
            answer += (10 - cur);
        }
        else if(cur == 5){
            answer += 5;
            storey += nex >= 5 ? 10 : 0;
        }
        else{
            answer += cur;
        }
        storey /= 10;
    }
    return answer;
}