class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""
        for word in strs:
            encode+=str(len(word))+"#"+word
        return encode



    def decode(self, s: str) -> List[str]:
        decode=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            size=int(s[i:j])
            word=s[j+1:j+size+1]
            decode.append(word)
            i=j+size+1
        return decode

