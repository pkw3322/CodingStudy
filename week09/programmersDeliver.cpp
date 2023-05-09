#include <string>
#include <vector>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups) {
    long long answer = 0;
    int sD = n-1,sP = n-1,tmp = cap;
    bool flag = true;
    int cmp1 = -1, cmp2 = -1;
    while(flag){
        tmp = cap;
        for(int i = sD; i >= 0; i--){
            int box = deliveries[i];
            if(tmp >= box){
                deliveries[i] -= tmp;
                tmp -= box;
                sD = i;
                if(cmp1 < 0 && box > 0)
                    cmp1 = i;
            }
            else if(deliveries[i] > 0 && deliveries[i] > tmp){
                sD = i;
                deliveries[i] -= tmp;
                if(cmp1 < 0 && box > 0)
                    cmp1 = i;
                break;
            }
        }
        tmp = cap;
        for(int i = sP; i >= 0; i--){
            int box = pickups[i];
            if(tmp >= box){
                pickups[i] -= tmp;
                tmp -= box;
                sP = i;
                if(cmp2 < 0 && box > 0)
                    cmp2 = i;
            }
            else if(pickups[i] > 0 && pickups[i] > tmp){
                sP = i;
                pickups[i] -= tmp;
                if(cmp2 < 0 && box > 0)
                    cmp2 = i;
                break;
            }
        }
        answer += cmp1 > cmp2 ? (long long)(2*(cmp1 + 1)) : (long long)(2*(cmp2 +1));
        if(sD == 0 && sP == 0 && deliveries[0] <= 0 && pickups[0] <= 0)
            flag = false;
        cmp1 = -1;
        cmp2 = -1;
    }
    return answer;
}