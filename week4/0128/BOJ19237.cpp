#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int N,M,K;
typedef struct{
    int x;
    int y;
    int cur;
    int eachDirect[5][5];
    bool isDead;
}Shark;

Shark shark[401];

pair<int,int> smell [21][21];
int sea[21][21];
int dy[4] = {-1,1,0,0};
int dx[4] = {0,0,-1,1};

bool valid(int y, int x) {
	if (y < 0 || x < 0 || y >= N || x >= N)
		return false;
	return true;
}

void remove_smell() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (sea[i][j] == 0 && smell[i][j].second > 0) {
				smell[i][j].second -= 1;

				if (smell[i][j].second == 0) {
					smell[i][j].first = 0;
				}
			}
		}
	}
}

void moving() {

	for (int i = 1; i <= M; i++) {
		int cur = shark[i].cur;
		int y = shark[i].y;
		int x = shark[i].x;

		bool isFind = false;

		if (shark[i].isDead == false) {
			for (int j = 0; j < 4; j++) {
				int f_dir = shark[i].eachDirect[cur][j];
				int ty = y + dy[f_dir-1];
				int tx = x + dx[f_dir-1];

				if (valid(ty, tx) && smell[ty][tx].second == 0) {

					if (sea[ty][tx] != 0) {
					    sea[y][x] = 0;
						shark[i].isDead = true;
						isFind = true;
						break;
					}

					else {
						sea[y][x] = 0;
						sea[ty][tx] = i;
						shark[i].y = ty;
						shark[i].x = tx;
						isFind = true;

						shark[i].cur = f_dir;
					}

					break; 
				}
			}


			if (!isFind) {
				for (int j = 0; j < 4; j++) {
					int f_dir = shark[i].eachDirect[cur][j]; 
					int ty = y + dy[f_dir-1];
					int tx = x + dx[f_dir-1];

					if (valid(ty, tx) && smell[ty][tx].first == i) {
						sea[y][x] = 0; 
						sea[ty][tx] = i;
						shark[i].y = ty;
						shark[i].x = tx;

						shark[i].cur = f_dir;
						break;
					}
				}
			}
		}
	}

	for (int i = 1; i <= M; i++) {
		if (shark[i].isDead == false) {
			int y = shark[i].y;
			int x = shark[i].x;

			smell[y][x].first = i;
			smell[y][x].second = K;
		}
	}
}


int main() {

	cin >> N >> M >> K;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> sea[i][j];
			if (sea[i][j] != 0) {
				shark[sea[i][j]].y = i;
				shark[sea[i][j]].x = j;
			}
		}
	}

	for (int i = 1; i <= M; i++) {
		cin >> shark[i].cur;
	}

	for (int i = 1; i <= M; i++) {
		for (int k = 1; k <= 4; k++) {
			for (int j = 0; j < 4; j++) {
				cin >> shark[i].eachDirect[k][j];
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (sea[i][j] != 0) {
				smell[i][j] = make_pair(sea[i][j], K);
			}
		}
	}
    int time = 0;

	while (time <= 1000) {
		bool flag = false;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (sea[i][j] != 0 && sea[i][j] != 1) {
					flag = true;
					break;
				}
			}
		}
		if (!flag) break;

		moving();

		remove_smell();

		time += 1;
	}

	if (time > 1000)
		cout << -1;
    else cout << time;

	return 0;
}