#include<iostream>

using namespace std;

long long n,atk;
long long Sum = 0,low,high,ans;
typedef struct{
    int t;
    long long a,h;
}state;
state room[123456];

int main(){
    cin >> n >> atk;
    for(int i = 0; i < n; i++){
        cin >> room[i].t >> room[i].a >> room[i].h;
    }
    low = 1;
    high = 1e18;
    long long middle;
    while(low <= high){
        middle = (low + high)/2;
        long long curA = atk;
        long long curH = middle;
        bool check = true;
        for(int i = 0; i < n; i++){
            if(room[i].t == 1){
                long long monsterA = room[i].a;
                long long monsterH = room[i].h;
                long long Time;
                if(monsterH%curA == 0)
                    Time = monsterH/curA - 1;
                else
                    Time = monsterH/curA;
                
                curH = curH - monsterA*Time;
                if(curH <= 0){
                    check = false;
                    break;
                }
            }
            else{
                curA += room[i].a;
                curH = min(middle,curH + room[i].h);
            }
        }
        if(check){
            high = middle - 1;
            ans = middle;
        }
        else{
            low = middle + 1;
        }
    }
    cout << ans;
    return 0;
}