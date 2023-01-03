#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

int n,m,maxNum = -100,cnt;
vector<int> tmp[10001];
bool visited[10001];

void makeResult(int k){
    cnt++;
	visited[k] = true;
	for (int i = 0; i < tmp[k].size(); i++) {
		if (!visited[tmp[k][i]]) {
			makeResult(tmp[k][i]);
		}
	}
}

int main(){
    cin >> n >> m;
    int result[10001];

    for(int i = 0; i <= n; i++){
        result[i] = 0;
    }
    for(int i = 0; i < m; i++){
        int to,from;
        cin >> to >> from;
        tmp[from].push_back(to);
    }
    for(int i = 1; i <= n; i++){
        makeResult(i);
        result[i] = cnt;
        cnt = 0;
        maxNum = maxNum > result[i]?maxNum:result[i];
        memset(visited,false,sizeof(visited));
    }
    
    for(int i = 1; i <= n; i++)
        if(maxNum == result[i])
            cout << i << ' ';
    
    return 0;
}