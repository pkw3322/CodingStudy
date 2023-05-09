#include <string>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

bool open[101];
vector<vector<int> >box(2);

void func(vector<int> cards, int card, int type){
    if(!open[card-1]){
        box[type].push_back(card-1);
        open[card-1] = true;
        func(cards, cards[card-1],type);
        if(type)
            open[card-1] = false;
    }
}

int solution(vector<int> cards) {
    int answer = 0;
    for(int i = 0; i < cards.size(); i++){
        memset(open,false,sizeof(open));
        open[i] = true;
        box[0].push_back(i);
        func(cards,cards[i],0);
        for(int j = 0; j < cards.size(); j++){
            if(!open[j]){
                open[j] = true;
                box[1].push_back(j);
                func(cards,cards[j],1);
                answer = max(answer,(int)(box[0].size()*box[1].size()));
                open[j] = false;
                box[1].clear();
            }
        }
        box[0].clear();
    }
    return answer;
}