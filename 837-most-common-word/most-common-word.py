class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        import re
        
        words = re.findall(r'\w+', paragraph.lower())
        
        count = {}
        
        for word in words:
            if word not in banned:
                count[word] = count.get(word, 0) + 1
        
        return max(count, key=count.get)
       
        