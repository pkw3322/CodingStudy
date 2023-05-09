#include<iostream>
#include<cstring>
#include<queue>
#include<vector>

using namespace std;

int n,result = 1000000;
int persons[11];
bool isConnect[11][11];
bool isSelect[11];
bool visited[11];

bool Check_Connection(vector<int> V, bool T)
{
    memset(visited, false, sizeof(visited));
    queue<int> q;
    q.push(V[0]);        
    visited[V[0]] = true;
    int cnt = 1;
 
    while (q.empty() == 0)
    {
        int x = q.front();
        q.pop();
 
        for (int i = 1; i <= n; i++)
        {
            if (isConnect[x][i]&& isSelect[i] == T && !visited[i])
            {
                visited[i] = true;
                cnt++;
                q.push(i);
            }
        }
    }
    if (V.size() == cnt) 
        return true;
    return false;
}

bool checking(){
    vector<int> tmp1,tmp2;
    for(int i = 1; i<= n; i++){
        if(isSelect[i] == true)
            tmp1.push_back(i);
        else
            tmp2.push_back(i);
    }
    if(tmp1.size() == 0 || tmp2.size() == 0)
        return false;
    if(!Check_Connection(tmp1, true)) 
        return false;
    if(!Check_Connection(tmp2, false)) 
        return false;
    return true;
}

void func(int idx,int cnt){
    if(cnt >= 1 && checking()){
        int a = 0,b = 0,d;
        for (int i = 1; i <= n; i++){
            if(isSelect[i] == true) 
                a = a + persons[i];
            else 
                b = b + persons[i];
        }
        d = abs(a - b);
        result = result < d ? result : d;
    }
    for(int i = idx; i <= n; i++){
        if(isSelect[i]) continue;
        isSelect[i] = true;
        func(i,cnt+1);
        isSelect[i] = false;
    }
}

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> persons[i];
    }
    for(int i = 1; i <= n; i++){
        int k;
        cin >> k;
        for(int j = 0; j < k; j++){
            int l;
            cin >> l;
            isConnect[i][l] = true;
            isConnect[l][i] = true;
        }
    }
    
    func(1,0);

    if(result == 1000000) cout << -1;
    else cout << result;
    return 0;
}