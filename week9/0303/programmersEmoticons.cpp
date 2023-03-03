#include <string>
#include <vector>

using namespace std;

int maxPlus = -1,maxEmo = -1;

void func(vector<int> v,vector<vector<int>> &users, vector<int> &emoticons){
    if(v.size() == emoticons.size()){
        int plus = 0,total = 0;
        
        for(int i = 0; i < users.size(); i++){
            int userTotal = 0;
            for(int j = 0; j < emoticons.size(); j++){
                if(users[i][0] > v[j])
                    continue;
                userTotal += (emoticons[j]/100)*(100 - v[j]);
            }
            if(userTotal >= users[i][1]){
                plus++;
            }
            else{
                total += userTotal;
            }
        }
        if(maxPlus > plus)
            return;
        if(maxPlus == plus && maxEmo >= total)
            return;
        maxPlus = plus;
        maxEmo = total;
        return ;
    }
    for(int i = 10; i <= 40 ; i+=10){
        v.push_back(i);
        func(v,users,emoticons);
        v.pop_back();
    }
}

vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    vector<int> answer;
    vector<int> v;
    func(v,users,emoticons);
    answer.push_back(maxPlus);
    answer.push_back(maxEmo);
    return answer;
}