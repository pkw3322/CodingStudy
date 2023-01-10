#include<iostream>

using namespace std;
int n,m,h,x,y,ret;
bool line[31][11];

void setting(){
    ret = 999999;
    for(int i = 0; i < 31; i++){
        for(int j = 0; j < 11; j++){
            line[i][j] = false;
        }
    }
}
bool isManipulated(){
    for(int i = 1; i <= n; i++){
        int c = i;
        for(int j = 1; j <= h; j++){
            if(line[j][c]) 
                c += 1;
            else if(line[j][c-1]) 
                c -= 1;
        }
        if(c != i) 
            return false;
    }
    return true;
}

void func(int depth, int cnt){
    if(depth == cnt){
        if(isManipulated())
            ret = cnt;
        return;
    }
    for(int i = 1; i < n; i++){
        for(int j = 1; j <= h; j++){
            if(line[j][i] || line[j][i-1] || line[j][i+1]) 
                continue;
			line[j][i] = 1;
			func(depth,cnt+1);
			line[j][i] = 0;

			while(!line[j][i-1] && !line[j][i+1]) 
                j++; 
        }
    }
}

int main(){
    int a,b;
    cin >> n >> m >> h;
    setting();
    for (int i = 0; i < m; i++){
        cin >> a >> b;
        line[a][b] = true;
    }
    
    for(int i = 0; i < 4; i++){
        if(ret != 999999) break;
        func(i,0);
    }

    if(ret == 999999)
        ret = -1;
    cout << ret;
    return 0;
}
