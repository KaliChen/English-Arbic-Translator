參考使用源碼為以下:
[https://github.com/amrelarabi/English-Arbic-Translator](http://https://github.com/amrelarabi/English-Arbic-Translator)
程式一開始載入字典檔並初始化
![https://ithelp.ithome.com.tw/upload/images/20201104/20119608zahyhtcSfK.jpg](https://ithelp.ithome.com.tw/upload/images/20201104/20119608zahyhtcSfK.jpg)
字典檔以AVLTree方式儲存
![https://ithelp.ithome.com.tw/upload/images/20201104/20119608bINhgyBniq.jpg](https://ithelp.ithome.com.tw/upload/images/20201104/20119608bINhgyBniq.jpg)

翻譯
![https://ithelp.ithome.com.tw/upload/images/20201104/20119608HK2cl1CSTC.jpg](https://ithelp.ithome.com.tw/upload/images/20201104/20119608HK2cl1CSTC.jpg)

重新整理過的
[https://github.com/KaliChen/Translator](http://https://github.com/KaliChen/Translator)

```

    from Translator.Translator_aviImple import Translator_avlImple
    from Translator.Translator_dicImple import Translator_dicImple

    def Translation_avl(self, event = None):
        T = Translator_avlImple()

        while True:
            word = input("Enter a word: ")
            if word == "-1":
                break
            wordTran = T.TranslateSentense(word)
            print(wordTran)

    def Translation_dic(self, event = None):
        T = Translator_dicImple()
        while True:
            word = input("Enter a word: ")
            if word == "-1":
                break
            wordTran = T.TranslateSentense(word)
            print(wordTran)  
```
![https://ithelp.ithome.com.tw/upload/images/20201105/20119608plCVRE9ZOW.jpg](https://ithelp.ithome.com.tw/upload/images/20201105/20119608plCVRE9ZOW.jpg)

[Find some Dictionaries](https://github.com/a3f/arabic-wordlists)
