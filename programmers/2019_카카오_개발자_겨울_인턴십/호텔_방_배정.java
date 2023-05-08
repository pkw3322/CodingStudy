import java.util.*;

class Solution {
    static HashMap<Long,Long> map = new HashMap<>();
    
    public long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        for(int i = 0; i < room_number.length; i++){
            answer[i] = findRoom(room_number[i]);
        }
        return answer;
    }
    
    private Long findRoom(long room_number){
        if(!map.containsKey(room_number)){
            map.put(room_number,room_number+1);
            return room_number;
        }
        Long temp = findRoom(map.get(room_number));
        map.put(room_number,temp);
        return temp;
    }
}