#include<iostream>
#include<cstring>
#include<algorithm>
#include<queue>
#include<vector>

using namespace std;

int n,m,result = -1;
int baduk[20][20];
int dead[20][20];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

vector<pair<int,int> >empties;

int func()
{
	memset(dead, 0, sizeof(dead));
	int ret = 0;
	for(int i=0; i<n; i++){
		for (int j = 0; j < m; j++)
		{
			if (baduk[i][j] == 2 && dead[i][j] == 0) {
				bool isDead = true;
				queue<pair<int, int> > q;
				q.push(make_pair(i,j));
				dead[i][j] = 1;
				int num = 0;
				while (!q.empty())
				{
					num++;
					int y = q.front().first;
					int x = q.front().second;
					q.pop();
					for (int k = 0; k < 4; k++)
					{
						int ny = y + dy[k];
						int nx = x + dx[k];

						if (0 <= ny && ny < n && 0 <= nx && nx < m){
                            if (baduk[ny][nx] == 0)
                                isDead = false;
                            else if (baduk[ny][nx] == 2 && dead[ny][nx] == 0) {
                                dead[ny][nx] = 1;
                                q.push(make_pair(ny,nx));
                            }
                        }
					}
				}
				if (isDead) {
					ret += num;
				}
			}
		}
    }
	return ret;
}


int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> baduk[i][j];
            if(baduk[i][j] == 0)
                empties.push_back(make_pair(i,j));
        }
    }
    for(int i = 0; i < empties.size(); i++){
        for(int j = 0; j < empties.size(); j++){
            if(i == j) continue;
            int y1 = empties[i].first;
            int x1 = empties[i].second;

            int y2 = empties[j].first;
            int x2 = empties[j].second;

            baduk[y1][x1] = 1;
            baduk[y2][x2] = 1;

            int cur = func();
            result = result > cur ? result : cur;
            baduk[y1][x1] = 0;
            baduk[y2][x2] = 0;
            
        }
    }
    cout << result;
    return 0;
}