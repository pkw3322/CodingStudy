#include<iostream>
#include<queue>

using namespace std;

int test,s,num;
bool Visit[10000001];
char c;

void solution(){
    priority_queue<pair<int,int> ,vector<pair<int,int> >, greater<pair<int, int> > > minH;
    priority_queue<pair<int,int> ,vector<pair<int,int> > > maxH;
    int cnt = 0;
    cin >> s;
    for(int i = 0; i < s; i++){
        cin >> c >> num;

        if(c == 'I'){
            maxH.push(make_pair(num,i));
            minH.push(make_pair(num,i));
            Visit[i] = true;
        }
        if(c == 'D'){
            if(cnt != 0) continue;

            if(num == 1){
                while(!maxH.empty() && !Visit[maxH.top().second])
                    maxH.pop();
                if(!maxH.empty()){
                    Visit[maxH.top().second] = false;
                    maxH.pop();
                }
            }
            if(num == -1){
                while(!minH.empty() && !Visit[minH.top().second])
                    minH.pop();
                if(!minH.empty()){
                    Visit[minH.top().second] = false;
                    minH.pop();
                }
            }
        }
    }
    while(!maxH.empty() && !Visit[maxH.top().second])
        maxH.pop();
    while(!minH.empty() && !Visit[minH.top().second])
        minH.pop();
    if(minH.empty() && maxH.empty())
        cout << "EMPTY\n";
    else
        cout << maxH.top().first << " " << minH.top().first << '\n';
}

int main(){
    cin >> test;
    while(test > 0){
        solution();
        test--;
    }
    return 0;
}