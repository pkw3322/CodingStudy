import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> s = new Stack<>();
        s.push(0);
        for(int m : moves){
            for(int j = 0; j < board.length; j++){
                if(board[j][m-1] != 0){
                    if(s.peek() == board[j][m-1]){
                        s.pop();
                        answer += 2;
                    }
                    else{
                        s.push(board[j][m-1]);
                    }
                    board[j][m-1] = 0;
                    break;
                }
            }
        }
        return answer;
    }
}