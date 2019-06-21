class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mourse_codes = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for word in words:
            print ('current word :', word)
        
        dct = {i:j for i,j in zip(alphabet, mourse_codes)}
    
        words_morse = []
        for word in words:
            words_morse.append(''.join(list(map(dct.get, list(word)))))
        
        return len(set(words_morse))
