class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #sorted approach
        # if(len(s)!=len(t)):
        #     return False
        # return(sorted(s)== sorted(t))
        if len(s) != len(t):
            return False
        
        count = {}
        
        # Increment count for characters in s, decrement for t
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
                
        return True
            
 
        