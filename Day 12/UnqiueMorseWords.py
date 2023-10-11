class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s1=list('abcdefghijklmnopqrstuvwxyz')
        print(s1)
        map1=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        map={}
        for i in range(len(s1)):
            map[s1[i]]=map1[i]
        l=[]
        c=0
        for word in words:
            s=''
            for char in word:
                
                s+=map[char]
            if s not in l:
                l.append(s)
                c+=1
                
        return c