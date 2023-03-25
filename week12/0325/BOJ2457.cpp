#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstring>

using namespace std;

typedef struct{
    int openDay;
    int closeDay;
}Flower;

int monthToday[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
int n,ans = 1;
vector<Flower> flowers;

int mToD(int month,int day){
    int res = 0;
    for(int i = 1; i < month; i++)
        res += monthToday[i];
    return res+day;
}

bool cmp(Flower f1,Flower f2){
    return f1.openDay < f2.openDay;
}

void solution(){
    int start = mToD(3,0);
    int end = mToD(3,1);
    int res = 0;
    int maxE = 0,maxIdx = 0;
    int last = mToD(12,1);
    sort(flowers.begin(),flowers.end(),cmp);
    
    for(int i = 0; i < n; i++){
        if(flowers[i].openDay > start && flowers[i].openDay <= end){
            if(maxE < flowers[i].closeDay){
                maxE = flowers[i].closeDay;
                maxIdx = i;
            }
            if(flowers[i].closeDay == last){
                res++;
                end = maxE;
                break;
            }
            continue;
        }
        else{
            if(end >= maxE)
                break;
            res++;
            start = end;
            end = maxE;
            i--;
        }
    }
    if(end == last){
        ans = res;
    }
    else{
        ans = 0;
    }
}

int main(){
    cin >> n;
    int oM,oD,cM,cD;
    int mini = mToD(3,1),maxi = mToD(11,30),maxim = mToD(12,1);
    for(int i = 0; i < n; i++){
        cin >> oM >> oD >> cM >> cD;
        Flower temp = {mToD(oM,oD),mToD(cM,cD)};
        if(temp.openDay < mini){
            temp.openDay = mini;
        }
        if(temp.closeDay > maxi){
            temp.closeDay = maxim;
        }
        flowers.push_back(temp);
    }

    solution();
    cout << ans;
    return 0;
}