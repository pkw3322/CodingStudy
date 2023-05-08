import java.util.*;


class Solution {
    public ArrayList<Integer> solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        s = s.substring(2,s.length());
        s = s.substring(0,s.length()-2).replace("},{","-");
        
        String str[] = s.split("-");
        
        Arrays.sort(str,new Comparator<String>(){
            public int compare(String s1, String s2){
                return Integer.compare(s1.length(),s2.length());
                
            }
        });
        
        for(String tem : str){
            String[] temp = tem.split(",");
            
            for(int i = 0; i < temp.length; i++){
                int num = Integer.parseInt(temp[i]);
                
                if(!answer.contains(num))
                    answer.add(num);
            }
        }
        
        return answer;
    }
}