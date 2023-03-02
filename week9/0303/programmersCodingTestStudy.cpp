#include <string>
#include <vector>
#include <algorithm>

using namespace std;



int solution(int alp, int cop, vector<vector<int>> problems) {
    int answer = 0;
    int alp_req = -1;
    int cop_req = -1;
    for(int i = 0; i < problems.size(); i++){
        if(alp_req < problems[i][0])
            alp_req = problems[i][0];
        if(cop_req < problems[i][1])
            cop_req = problems[i][1];
    }
    vector<vector<int>> dp(alp_req+1,vector<int>(cop_req+1,1999999999));
    if(alp_req <= alp && cop_req <= cop)
        return 0;
    if(alp_req < alp)
        alp = alp_req;
    if(cop_req < cop)
        cop = cop_req;
    dp[alp][cop] = 0;
    for(int i = alp; i <= alp_req; i++){
        for(int j = cop; j <= cop_req; j++){
            if(j < cop_req)
                dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1);
            if(i < alp_req)
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1);
            for(int l = 0; l < problems.size(); l++){
                if(i >= problems[l][0] && j >= problems[l][1]){
                    dp[min(alp_req,i+problems[l][2])][min(cop_req,j+problems[l][3])] = 
                        min(dp[min(alp_req,i+problems[l][2])][min(cop_req,j+problems[l][3])],dp[i][j]+problems[l][4]);
                }
            }
        }
    }
    answer = dp[alp_req][cop_req];
    return answer;
}