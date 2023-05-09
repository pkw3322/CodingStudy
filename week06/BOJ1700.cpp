#include<iostream>
#include<queue>
#include<cstring>

using namespace std;

int n,k,result = 0;
int schedule[101];
int multiTap[101];

int main(){
    cin >> n >> k;
    
    for(int i = 0; i < k; i++){
        cin >> schedule[i];
    }
    memset(multiTap,0,sizeof(multiTap));
    for(int i = 0; i < k; i++){
        int now = schedule[i];
        int checking = -1;
        for(int j = 0; j < n; j++){
            if(now == multiTap[j]){
                checking = 0;
                break;
            }
        }
        if(checking != 0){
            for(int j = 0; j < n; j++){
                if(multiTap[j] == 0){
                    checking = 1;
                    multiTap[j] = now;
                    break;
                }
            }
            if(checking != 1){
                int last = -1; 
                int index = -1; 
                for (int j = 0; j < n; j++){
                    int tmp = 0;
                    for (int t = i+1;t < k; t++){
                        if (schedule[t] == multiTap[j]){
                            break;
                        }
                        tmp++;
                    }

                    if (tmp > last){
                        last = tmp;
                        index = j;
                    }
                }
                multiTap[index] = schedule[i];
                result++;
            }
        }
    }
    cout << result;
    return 0;
}