import java.util.*;

class Solution {
    String[] userIds;
    String[] bannedIds;
    boolean[] Visit;
    HashSet<HashSet<String>> res = new HashSet<>();
    
    public int solution(String[] user_id, String[] banned_id) {
        userIds = user_id;
        bannedIds = banned_id;
        Visit = new boolean[user_id.length];
        dfs(new HashSet<String>(),0);
        
        return res.size();
    }
    
    private void dfs(HashSet<String> hash,int dep){
        if(dep == bannedIds.length){
            res.add(hash);
            return ;
        }
        for(int i = 0; i < userIds.length; i++){
            if(hash.contains(userIds[i]))
                continue;
            if(check(userIds[i],bannedIds[dep])){
                hash.add(userIds[i]);
                dfs(new HashSet<>(hash),dep+1);
                hash.remove(userIds[i]);
            }
        }
    }
    
    private boolean check(String userId,String bannedId){
        if(userId.length() != bannedId.length()){
            return false;
        }
        for(int i = 0; i < userId.length(); i++){
            if(bannedId.charAt(i) != '*' && bannedId.charAt(i) != userId.charAt(i))
                return false;
        }
        return true;
    }
}