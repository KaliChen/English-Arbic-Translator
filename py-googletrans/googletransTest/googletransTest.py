
from googletrans import Translator
import linecache

##1)Basic Usage
##  If source language is not given, google translate attempts to detect the source language.
#translator = Translator()
#print(translator.translate('안녕하세요.'))
## <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
#print(translator.translate('안녕하세요.', dest='ja'))
## <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
#print(translator.translate('veritas lux mea', src='la'))
## <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
#print(translator.translate('Hello', dest = 'ar'))

##2)Customize service URL
##  You can use another google translate domain for translation. If multiple URLs are provided it then randomly chooses a domain.

translator = Translator(service_urls=[
    'translate.google.com',
#    'translate.google.co.kr',
])

#3)Advanced Usage (Bulk)
#  Array can be used to translate a batch of strings in a single method call and a single HTTP session. 
#  The exact same method shown above work for arrays as well.
"""
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
"""
# The quick brown fox  ->  빠른 갈색 여우
# jumps over  ->  이상 점프
# the lazy dog  ->  게으른 개

##4)Language detection
##  The detect method, as its name implies, identifies the language used in a given sentence.
#translator.detect('이 문장은 한글로 쓰여졌습니다.')
## <Detected lang=ko confidence=0.27041003>
#translator.detect('この文章は日本語で書かれました。')
## <Detected lang=ja confidence=0.64889508>
#translator.detect('This sentence is written in English.')
## <Detected lang=en confidence=0.22348526>
#translator.detect('Tiu frazo estas skribita en Esperanto.')
## <Detected lang=eo confidence=0.10538048>


def add_num():
    f = open('words_alpha.txt','r')

    add_num = open('words_alpha-add_num.txt', 'a')

    line_nu = 0#计数器
    tmp  = ''
    for line in f:#一行行的把数据从硬盘加载到内存里读出来
        #print('['+ str(line_nu) +'] \t'+ line.strip()+'\n')
        tmp += '['+ str(line_nu) +'] \t'+ line.strip()+'\n'
        add_num.write(tmp)
        line_nu += 1
        tmp =''
    f.close()
    add_num.close()

def translate():
    f = open('arabic-stop-words.txt','r')
    ara2eng_write_in = open('arabic-stop-words2eng.txt', 'w')

    #print(f.read())
    tmp = ''
    line_nu = 0#计数器
    for line in f:#一行行的把数据从硬盘加载到内存里读出来
        #print(line_nu)
        tmp += '['+ str(line_nu) +'] \t'+ line.strip()+'\n'
        #tmp += line.strip()+'\n'
        #translations = translator.translate( line.strip(), dest='en')
        #print(str(line_nu)+":" + line.strip() + translations.text)
        #print(str(line_nu)+":" + line.strip())
        line_nu += 1

        if(line_nu%100 == 0):
            translations = translator.translate( tmp, dest='en')
            print(translations.text)
            ara2eng_write_in.write(translations.text)
            tmp = ''

    #print(tmp)

    ara2eng_write_in.close()

    f.close()

if __name__ == '__main__':
    add_num()    
"""
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

LANGCODES = dict(map(reversed, LANGUAGES.items()))
"""
