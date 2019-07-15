# -*- coding: utf-8 -*-

from Translator import Translator1
from Translator import Translator2

T1 = Translator1()
T2 = Translator2()

while True:
    word = input("Enter a word: ")
    if word == "-1":
        break
#    word = T.TranslateSentense(word)
#    print(word)
    word1 = T1.TranslateSentense(word)
    word2 = T2.TranslateSentense(word)
    print(word1)
    print(word2)
