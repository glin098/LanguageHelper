from language_tools import LanguageHelper
import unittest

# We define the custom lexicon that we will use for our controlled tests
sample = ('car', 'cat', 'Cate', 'cater', 'care',
          'cot', 'cute', 'dare', 'date', 'dog', 'dodge',
          'coffee', 'pickle', 'grate')

rhymesWithDog = ('bog', 'cog', 'clog', 'fog', 'frog', 'hog', 'log')

singleLetter=('I','A')

long=('gorgeous','beautiful')


class BasicTest(unittest.TestCase):
  
# make sure that all the words in the lexicon are recognized
    def testContainment(self):
        helper = LanguageHelper(sample)
        for w in sample:
            self.assertTrue(w in helper)
  
    def testFailures(self):
        helper = LanguageHelper(sample)
        self.assertFalse('cate' in helper)     # only allowed when capitalized
        self.assertFalse('fox' in helper)      # word is not there
        self.assertFalse('cofee' in helper)    # mis-spell word is not there

    def testSuggestInsertion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('pikle'), ['pickle'])
        self.assertEqual(helper.getSuggestions('ct'), ['cat','cot'])

    def testSuggestDeletion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('gratle'), ['grate'])

    def testSugeestionsMany(self):
        helper = LanguageHelper(rhymesWithDog)
        self.assertEqual(helper.getSuggestions('rog'), ['bog','cog','fog','frog','hog','log'])

    def testSugeestionsCapitalization(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('Gate'), ['Cate', 'Date', 'Grate'])

    def testSuggestionsNone(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('blech'), [])

#check movie/game title (proper noun)
    def testMovieTitle(self):
        helper=LanguageHelper(sample)
        self.assertFalse('Rango' in helper) #Movie title should not be in language-too specific    
        self.assertFalse('Pokemon' in helper) #Same as above

#check a keyboard smash (incomprehensible string)
    def testKeyboardSmash(self):
        helper=LanguageHelper(sample)
        self.assertFalse('asdfadwhgkfads' in helper) #Incomprehensible string, should not be in language and too far away from any word to be corrected
            
#Check spelling of a single letter word 'A', 'I'
    def testSingleLetterWords(self):
        helper=LanguageHelper(singleLetter)
        self.assertEqual(helper.getSuggestions('B'),[]) #Cannot correct a single letter misspelling, Microsoft Word spell-checker does not

#Misspelling of a long word 
    def testLongWord(self):
        helper=LanguageHelper(long) 
        self.assertEqual(helper.getSuggestions('georgeous'),['gorgeous']) #correcting longer words, more likely to be misspelled
        self.assertEqual(helper.getSuggestions('beautifl'),['beautiful'])
        
#word entered twice 'catcat'
    def testWordEnteredTwice(self):
        helper=LanguageHelper(sample)
        self.assertFalse('catcat' in helper) #checker only corrects for one letter difference, 'catcat' is three letters away from a correct word



        

if __name__ == '__main__':
    unittest.main()
