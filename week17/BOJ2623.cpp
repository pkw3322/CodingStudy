#include <iostream>
#include <vector>
#include <queue>

using namespace std;
 
int N, M;
int inDeg[1002] = { 0, };
vector<int> graph[1002];
vector<int> ans;             
 
void solution(){
    queue<int> q;
 
    for (int i = 1; i <= N; i++) {
        if (inDeg[i] == 0) {
            q.push(i);
        }
    }
 
    while (!q.empty()) {
        int from = q.front();
        q.pop();
        ans.push_back(from);
 
        for (int i = 0; i < graph[from].size(); i++) {
            int to = graph[from][i];
            inDeg[to]--;
            if (inDeg[to] == 0) {
                q.push(to);
            }
        }
    }
 
    if (ans.size() != N) {
        cout << 0 << endl;
        return ;
    }
    else {
        for (int i = 0; i < N; i++) {
            cout << ans[i] << endl;
        }
    }
}

int main() {
    cin >> N >> M;
 
    while (M--) {
        int sNum;
        int s1, s2;
        cin >> sNum;
        if (sNum == 0) continue;
        cin >> s1;
        if (sNum == 1) continue;
 
        for (int i = 0; i < sNum-1; i++) {
            cin >> s2;
            graph[s1].push_back(s2);
            inDeg[s2]++;
            s1 = s2;
        }
    }
 
    solution();
 
    return 0;
}
