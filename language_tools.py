class LanguageHelper:
    words = []

    def __init__(self,words):
        self.words = set(words) #converting to a set
        
    def get_words(self):
        return self.words #stores the value

    def __contains__(self,query):
        language=self.words
        if query in language:
            return True
        else:
            return False

    def getSuggestions(self, query):
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #used to generate suggestions
        wordsone=query #wordsone is input
        language=self.words
        answer = set() #answer is output
        correction = []
        correction.append(wordsone.lower())

        #Delete a character
        for i in range(len(wordsone)):
            new = wordsone.replace(str(wordsone[i]),'')#replace with an empty string for each letter in word until one in language is generated
            correction.append(new)
            if new in language:
                answer.add(new)
        
        #Add a character
        for index in range(len(correction)):
            for index2 in range(len(alphabet)):
                for index3 in range(len(correction[index])):
                    letter=alphabet[index2] #checking for each letter in alphabet
                    word = correction[index]
                    newWord=word[:index3]+letter+word[index3:] #adding each possible letter until one in language is generated
                    words = []
                    #checking for capitalization
                    if wordsone[0].isupper():
                        words.append(newWord[0].upper() + newWord[1:]) 
                    words.append(newWord)
                    words.append(newWord.lower())
                    for upperWord in words:
                        if upperWord in language:
                            if wordsone[0].isupper():
                                answer.add(newWord[0].upper() + newWord[1:])
                            else:
                                answer.add(newWord)
                            break
         
        #Change a character
        for index in range(len(wordsone)):
            inword=wordsone[index]
            for index2 in range(len(alphabet)): #checking for each letter in alphabet
                letter=alphabet[index2]
                new=wordsone.replace(inword,letter) #replacing characters until one in language is generated             
                if new in language and answer.__contains__(new) == False:
                    if answer.__contains__(new[0].upper() + new[1:]) == False:
                        answer.add(new)
                            
        return sorted(answer) #answer is output
