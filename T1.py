def minSubsequences(source, target):
    count = 0  
    t_idx = 0  
    while t_idx < len(target):
        found = False
        for s_idx in range(len(source)):
            if t_idx < len(target) and source[s_idx] == target[t_idx]:
                t_idx += 1
                found = True
        if not found:  
            return -1
        
        count += 1  
    return count

print(minSubsequences("abc", "abcbc"))  
print(minSubsequences("abc", "acdbc"))  
print(minSubsequences("xyz", "xzyxz"))  
