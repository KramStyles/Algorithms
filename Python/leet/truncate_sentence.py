class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sentence = s.split(' ')[:k]
        print(' '.join(sentence))
        return ' '.join(sentence)
        
s = "Hello how are you doing"
k = 4

so = Solution()
so.truncateSentence(s,k)