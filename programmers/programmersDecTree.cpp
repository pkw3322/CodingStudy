#include <string>
#include <vector>

using namespace std;


bool func(int64_t len,vector<bool>& numDec,int32_t level){
    if(len%2 == 1){
        return true;
    }
    
    long long p = 1 << level;
    int left = len - p/2;
    int right = len + p/2;
    if(!(func(left,numDec,level-1) && func(right,numDec,level-1)))
        return false;
    
    if(!numDec[len-1]){
        return !(numDec[left-1]||numDec[right-1]);
    }
    return true;
}

vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    for(int i = 0; i < numbers.size(); i++){
        long long root = 1;
        long long p = 1;
        int lev = 0;
        int len = 0;
        while(numbers[i] >= p){
            p *= 2;
            len++;
        }
        while(len >= root*2){
            root *= 2;
            lev++;
        }
        vector<bool> numDec(root*2,false);
        for(int j = 0; j <= len; j++){
            numDec[j] = numbers[i]%2;
            numbers[i] /= 2;
        }
        answer.push_back(func(root,numDec,lev));
    }
    return answer;
}
