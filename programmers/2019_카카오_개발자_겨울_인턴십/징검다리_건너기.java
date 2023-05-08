import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        int minFriend = 1;
        int maxFriend = 200000000;
        while(minFriend <= maxFriend){
            int mid = (minFriend + maxFriend)/2;
            
            if(checking(stones,k,mid)){
                minFriend = mid + 1;
                answer = Math.max(answer,mid);
            }
            else
                maxFriend = mid - 1;
        }
        return answer;
    }
    private boolean checking(int[] stones,int k,int friends){
        int flag = 0;
        for(int i = 0; i < stones.length; i++){
            if(stones[i] < friends)
                flag++;
            else
                flag = 0;
            if(flag == k)
                return false;
        }
        return true;
    }
}