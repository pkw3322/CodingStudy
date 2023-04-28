#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

int N, M;
int A[50][50];

vector<int> v;

int d, s;
int sx, sy;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int rdx[4] = {-1, 0, 1, 0};
int rdy[4] = {0, 1, 0, -1};

int score = 0;

void move(){
  v.clear();

  int dist = 1;
  int nx = sx; int ny = sy;
  d = 0;
  int cnt = 0; 
  int maxCnt = N * N - 1;

  while(1){
    for(int i = 0; i < 2; i++){
      for(int j = 0; j < dist; j++){
        nx += rdx[d];
        ny += rdy[d];

        cnt++;

        if(nx < 0 || ny < 0 || nx >= N || ny >= N){
          continue;
        }

        if(A[ny][nx] > 0){
          v.push_back(A[ny][nx]);
        }
      }
      if(cnt >= maxCnt){
        break;
      }
      d = (d + 1) % 4;
    }
    if(cnt >= maxCnt){
      break;
    }
    dist++;
  }
}

void explore(){
  bool flag = true;

  while(flag){
    flag = false;
    vector<int> tmp;

    if(v.size() == 0){
      return;
    }
    
    for(int i = 0; i < v.size(); i++){
      int next = i;

      if(v[i] != v[next]){
        tmp.push_back(v[i]);
      } else {
        while(v[i] == v[next] && next < v.size()){
          next++;
        }

        if(next - i < 4){
          for(int j = i; j < next; j++){
            tmp.push_back(v[j]);
          }
        } else {
          score += v[i] * (next - i);
          flag = true;
        }
      }
      i = --next;
    }
    v = tmp;
  }
}

void change(){
  vector<int> tmp;

  if(v.size() == 0){
    return;
  }

  for(int i = 0; i < v.size(); i++){
    int next = i;

    while(v[i] == v[next] && next < v.size()){
      next++;
    }
    tmp.push_back(next - i);
    tmp.push_back(v[i]);

    if(tmp.size() >= N * N){
      while(tmp.size() >= N * N){
        tmp.pop_back();
      }
    }
    i = --next;
  }
  v = tmp;
}

void mapSet(){
  memset(A, 0, sizeof(A));
  int nx = sx; int ny = sy;
  int d = 0;
  int dist = 1;
  int idx = 0;

  if(v.size() == 0){
    return;
  }

  while(1){
    for(int i = 0; i < 2; i++){
      for(int j = 0; j < dist; j++){
        nx += rdx[d];
        ny += rdy[d];

        if(nx < 0 || ny < 0 || nx >= N || ny > N){
          continue;
        }

        A[ny][nx] = v[idx];
        idx++;

        if(idx == v.size()){
          return;
        }
      }
      d = (d + 1) % 4;
    }
    dist++;
  }
}

int main(){
  cin >> N >> M;

  for(int i = 0; i < N; i++){
    for(int j = 0; j < N; j++){
      cin >> A[i][j];
    }
  }

  sx = N / 2; 
  sy = N / 2;

  for(int i = 0; i < M; i++){
    cin >> d >> s;
    d--;

    int nx = sx; int ny = sy;
    for(int j = 0; j < s; j++){
      nx += dx[d];
      ny += dy[d];
      if(nx < 0 || ny < 0 || nx >= N || ny >= N){
        continue;
      }
      A[ny][nx] = 0;
    }

    move();
    explore();
    change();
    mapSet();
  }

  cout << score;

  return 0;
}