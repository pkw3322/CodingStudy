#include <string>
#include <vector>

using namespace std;

bool checking(int arr[],int n){
    for(int i = 0; i <= n; i++){
        if(arr[i] == 1)
            return false;
    }
    return true;
}

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    int arr[100001] = {0,};
    for(int i = 0; i < section.size(); i++){
        arr[section[i]] = 1;
    }
    while(!checking(arr,n)){
        int end = section[section.size()-1];
        for(int i = end; i > end - m; i--){
            if(i < 1)
                break;
            if(arr[i] == 1){
                section.pop_back();
                arr[i] = 0;
            }
        }
        answer++;
    }
    return answer;
}