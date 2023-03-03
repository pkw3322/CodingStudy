#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int findMax(vector<int> array,vector<int> list){
    int ret = 0;
    bool flag = false;
    for(int i = 0; i < list.size(); i++){
        flag = true;
        for(int j = 0; j < array.size(); j++){
            if(array[j]%list[i] == 0 && flag){
                flag = false;
                break;
            }
        }
        if(flag){
            ret = max(ret,list[i]);
        }
    }
    return ret;
}

int solution(vector<int> arrayA, vector<int> arrayB) {
    int answer = 0;
    vector<int> listA,listB;
    
    sort(arrayA.begin(),arrayA.end());
    sort(arrayB.begin(),arrayB.end());
    
    bool flag = false;
    for(int i = 2; i <= arrayA[0]; i++){
        flag = true;
        for(int j = 0; j < arrayA.size(); j++){
            if(arrayA[j]%i != 0 && flag){
                flag = false;
                break;
            }
        }
        if(flag){
            listA.push_back(i);
        }
    }
    flag = false;
    for(int i = 2; i <= arrayB[0]; i++){
        flag = true;
        for(int j = 0; j < arrayB.size(); j++){
            if(arrayB[j]%i != 0 && flag){
                flag = false;
                break;
            }
        }
        if(flag){
            listB.push_back(i);
        }
    }
    answer = findMax(arrayA,listB);
    answer = max(answer,findMax(arrayB,listA));
    
    return answer;
}