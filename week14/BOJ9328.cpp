#include<iostream>
#include<vector>
#include<cstring>
#include<cctype>
#include<queue>

using namespace std;

int test,h,w,cntDocu;
string temp;
char arr[101][101];
bool Visit[101][101];
vector<pair<int,int> >input;
vector<int> ans;
vector<char> keys;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

bool checking(char c){
    for(int i = 0; i < keys.size(); i++){
        if(keys[i] == c)
            return true;
    }
    return false;
}

bool Solution(){
    bool needUpdate = false;
    queue<pair<int,int> > q;
    memset(Visit,false,sizeof(Visit));

    for(int i = 0; i < input.size(); i++){
        if(arr[input[i].first][input[i].second] >= 'A' && 
            arr[input[i].first][input[i].second] <= 'Z'){
            if(checking(arr[input[i].first][input[i].second]))
                arr[input[i].first][input[i].second] = '.';
            else
                continue;
        }
        if(arr[input[i].first][input[i].second] >= 'a' && 
            arr[input[i].first][input[i].second] <= 'z'){
            keys.push_back(toupper(arr[input[i].first][input[i].second]));
        }

        q.push(input[i]);
        Visit[input[i].first][input[i].second] = true;
        if(arr[input[i].first][input[i].second] == '$'){
            arr[input[i].first][input[i].second] = '.';
            cntDocu++;
        } 
    }
    while(!q.empty()){
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++){
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if(nx >= 0 && nx < h && ny >= 0 && ny < w){
                if(arr[nx][ny] != '*' && !Visit[nx][ny]){
                    if(arr[nx][ny] >= 'A' && arr[nx][ny] <= 'Z'){
                        if(!checking(arr[nx][ny]))
                            continue;
                        needUpdate = true;
                    }
                    if(arr[nx][ny] == '$')
                        cntDocu++;
                    if(arr[nx][ny] >= 'a' && arr[nx][ny] <= 'z'){
                        keys.push_back(toupper(arr[nx][ny]));
                        needUpdate = true;
                    }
                    arr[nx][ny] = '.';
                    Visit[nx][ny] = true;
                    q.push(make_pair(nx,ny));
                }
            }
        }
    }
    return needUpdate;
}

int main(){
    cin >> test;
    while(test > 0){
        cin >> h >> w;
        memset(arr,0,sizeof(arr));
        input.clear();
        keys.clear();
        cntDocu = 0;
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                cin >> arr[i][j];
                if(i == 0 || j == 0 || i == h-1 || j == w-1){
                    if(arr[i][j] != '*')
                        input.push_back(make_pair(i,j));
                }
            }
        }
        cin >> temp;
        if(temp != "0"){
            for(int i = 0; i < temp.length(); i++){
                keys.push_back(toupper(temp[i]));
            }
        }
        while(Solution());

        ans.push_back(cntDocu);
        test--;
    }
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << '\n';
    }
    return 0;
}