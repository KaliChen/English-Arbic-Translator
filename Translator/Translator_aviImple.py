from Translator.BinarySearchTree.BinarySearchTree import BinarySearchTree
from Translator.AVLTree import AVLTree
from datetime import datetime
from Translator.SpellChecker import SpellChecker
from Translator.Result import Result
from tkinter import filedialog

##########################
# AVLTree Implementation #
##########################

class Translator_avlImple:
    """ AVLTree Implementation """

    def __init__(self):
        self.dictionaryPath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        time1 = datetime.now()
        print("Loading Database...")
        #self.__words = [line.rstrip('\r\n') for line in open("Dictionary/UltimateZeroDict.txt", "r", encoding='utf-8')]
        self.__words = [line.rstrip('\r\n') for line in open(self.dictionaryPath, "r", encoding='utf-8')]
        self.__tree = self.__getDictionary()
        self.SpellChecker = self.__makeSpellChecker()
        time2 = datetime.now()
        print("Loaded in {0}\r\n".format(time2 - time1))

    def __getDictionary(self):
        words = [line.rstrip('\r\n') for line in open(self.dictionaryPath, "r", encoding='utf-8')]
        #words = [line.rstrip('\r\n') for line in open("Dictionary/UltimateZeroDict.txt", "r", encoding='utf-8')]
        avl = AVLTree()
        for word in self.__words:
            temp = word.lower().split(':')
            avl.insert(temp[0], temp[1])
        return avl

    def __makeSpellChecker(self):
        #words = [line.rstrip('\r\n') for line in open("Dictionary/UltimateZeroDict.txt", "r", encoding='utf-8')]
        words = [line.rstrip('\r\n') for line in open(self.dictionaryPath, "r", encoding='utf-8')]
        english = []
        for word in self.__words:
            temp = word.lower().split(':')
            english.append(temp[0])
        return SpellChecker(english)

    #def hasWord(self, englishWord):
    #    return self.__tree.has_key(englishWord.lower())

    def Translate(self, englishWord):
        englishWord = englishWord.lower()
        trans = self.__tree.ValueOf(englishWord)
        result = Result()
        if trans is not None:
            result.Value = trans
        else:
            result.Suggesions = self.SpellChecker.GetSuggestions(englishWord)
        return result
    
    def TranslateSentense(self, sentense):
        words = sentense.split(' ')
        output = []
        wrong = "Unable to recognize these words, Here are some Suggestions:\r\n"
        w = False
        for word in words:
            trans = self.Translate(word)
            
            if trans.Translated():
                output.append(trans.Value)
            else:
                wrong += word + " => " + str(trans.Suggesions) + "\r\n"
                w = True
                output.append(word)

        return " ".join(output) + "\r\n" + (wrong if w else "")

#--------------------------------------------------------
# main
#--------------------------------------------------------
if __name__ == '__main__':
    T = Translator_avlImple()

    while True:
        word = input("Enter a word: ")
        if word == "-1":
            break
        wordTran = T.TranslateSentense(word)
        print(wordTran)

