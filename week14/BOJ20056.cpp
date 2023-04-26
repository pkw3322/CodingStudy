#include <iostream>
#include <vector>

using namespace std;
 
struct FIREBALL{
    int x;
    int y;
    int M;
    int S;
    int D;
};
 
int dx[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dy[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int Dir1[4] = { 0, 2, 4, 6 };
int Dir2[4] = { 1, 3, 5 ,7 };
 
int N, M, K,ans = 0;
vector<FIREBALL> MAP[55][55];
vector<FIREBALL> FireBall;

 
void Move(){
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            MAP[i][j].clear();
        }
    }
    
    for (int i = 0; i < FireBall.size(); i++){
        int x = FireBall[i].x;
        int y = FireBall[i].y;
        int M = FireBall[i].M;
        int S = FireBall[i].S;
        int D = FireBall[i].D;
 
        int Move = S % N;
        int nx = x + dx[D] * Move;
        int ny = y + dy[D] * Move;

        if (nx > N) nx -= N;
        if (ny > N) ny -= N;
        if (nx < 1) nx += N;
        if (ny < 1) ny += N;
        FIREBALL f = {nx,ny,M,S,D};
        MAP[nx][ny].push_back(f);
        FireBall[i].x = nx;
        FireBall[i].y = ny;
    }
}
 
void SumBall(){
    vector<FIREBALL> Temp;
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            if (MAP[i][j].size() == 0)continue;
            if (MAP[i][j].size() == 1){
                Temp.push_back(MAP[i][j][0]);
                continue;
            }
            
            int mSum = 0;
            int sSum = 0;
            int Cnt = MAP[i][j].size();
 
            bool isEven = true;
            bool isOdd = true;
            for (int k = 0; k < MAP[i][j].size(); k++)
            {
                mSum += MAP[i][j][k].M;
                sSum += MAP[i][j][k].S;
                if (MAP[i][j][k].D % 2 == 0) isOdd = false;
                else isEven = false;
            }
            
            int curM = mSum / 5;
            int curS = sSum / Cnt;
            if (curM == 0) continue;
            if (isEven == true || isOdd == true){
                for (int k = 0; k < 4; k++){
                    FIREBALL f = {i,j,curM,curS,Dir1[k]};
                    Temp.push_back(f);
                }
            }
            else{
                for (int k = 0; k < 4; k++){
                    FIREBALL f = {i,j,curM,curS,Dir2[k]};
                    Temp.push_back(f);
                }
            }
        }
    }
    FireBall = Temp;
}
 
void Solution(){
    for (int i = 0; i < K; i++){
        Move();
        SumBall();
    }
}

 
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M >> K;
    for (int i = 0; i < M; i++){
        int r, c, m, s, d;
        cin >> r >> c >> m >> s >> d;
        FIREBALL f = {r,c,m,s,d};
        FireBall.push_back(f);
        MAP[r][c].push_back(f);
    }
    Solution();
    
    for(int i = 0 ; i< FireBall.size(); i++) 
        ans += FireBall[i].M;
    
    cout << ans << endl;
    return 0;
}
