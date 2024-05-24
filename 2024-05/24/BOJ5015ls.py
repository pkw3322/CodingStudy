import sys

NONE = -1
TRUE = 1
FALSE = 0

def recursive_pattern_check(pattern_index, input_index):
    if pattern_index >= len(pattern) and input_index >= len(input_str):
        return TRUE
    
    if pattern_index >= len(pattern):
        return FALSE
    
    if input_index >= len(input_str) and pattern[pattern_index] != '*':
        return FALSE
    
    if dp[pattern_index][input_index] != NONE:
        return dp[pattern_index][input_index]
    
    if pattern[pattern_index] == '*':
        result = FALSE
        
        if input_index <= len(input_str):
            if recursive_pattern_check(pattern_index + 1, input_index) == TRUE:
                result = TRUE
            if recursive_pattern_check(pattern_index + 1, input_index + 1) == TRUE:
                result = TRUE
            if recursive_pattern_check(pattern_index, input_index + 1) == TRUE:
                result = TRUE
        
        dp[pattern_index][input_index] = result
        return result
    else:  
        if pattern[pattern_index] == input_str[input_index]:  
            dp[pattern_index][input_index] = recursive_pattern_check(pattern_index + 1, input_index + 1)
            return dp[pattern_index][input_index]
        dp[pattern_index][input_index] = FALSE
        return dp[pattern_index][input_index]

def reset_dp_array():
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = NONE
if __name__ == "__main__":
    input_str = sys.stdin.readline().strip()
    pattern = list(input_str)
    dp = [[NONE] * 102 for _ in range(102)]
    
    n = int(sys.stdin.readline())
    result = []
    
    for _ in range(n):
        line = sys.stdin.readline().strip()
        input_str = list(line)
        reset_dp_array()
        
        if recursive_pattern_check(0, 0) == TRUE:
            result.append(line)
    
    print('\n'.join(result))

