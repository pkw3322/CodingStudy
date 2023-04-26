#include<iostream>
#include<map>

#define Up 0
#define Down 1
#define Left 2
#define Right 3

using namespace std;

int n,m,ans = 0;
char arr[1001][1001];
map<char,int> direct;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

bool checking(int i,int j){
    if(arr[i][j] == 0)
        return true;
    else if(arr[i][j] == 1)
        return false;
    
    char dir = arr[i][j];
    arr[i][j] = 0;
    bool ret = checking(i+dx[direct[dir]],j + dy[direct[dir]]);
    arr[i][j] = 1;
    return ret;
}

void Solution(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(checking(i,j))
                ans++;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    direct.insert(make_pair('U',Up));
    direct.insert(make_pair('D',Down));
    direct.insert(make_pair('L',Left));
    direct.insert(make_pair('R',Right));

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> arr[i][j];
        }
    }
    Solution();
    cout << ans;
    return 0;
    
}