#include<iostream>

using namespace std;

enum DAYS{
    SUN,MON,TUE,WED,THU,FRI,SAT
};

int month,day;

int getMonth(int mon){
    if(mon == 2)
        return 28;
    
    if(mon == 4 || mon == 6 || mon == 9 || mon == 11)
        return 30;
    
    return 31;
}

void getDay(DAYS d){
    if(d == MON)
        cout << "MON";
    else if(d == TUE)
        cout << "TUE";
    else if(d == WED)
        cout << "WED";
    else if(d == THU)
        cout << "THU";
    else if(d == FRI)
        cout << "FRI";
    else if(d == SAT)
        cout << "SAT";
    else if(d == SUN)
        cout << "SUN";
}
int main(){
    cin >> month >> day;

    if(month == 1){
        getDay(DAYS(day%7));
    }
    else{
        int total = 0;
        for(int i = 1; i < month; i++){
            total += getMonth(i);
        }
        total += day;
        getDay(DAYS(total%7));
    }
    return 0;
}