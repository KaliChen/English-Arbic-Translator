
from googletrans import Translator
import linecache


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

def words_alpha_reunion():
    words_alpha = open('words_alpha-add_num.txt', 'r')
    words_alpha2ara = open('words_alpha2ara.txt', 'r')
    words_alpha2zhtw = open('words_alpha2zhtw.txt', 'r')
    words_alpha_reunion = open('words_alpha_reunion', 'w')
    line_nu_eng = 0
    #tmp
    for line in words_alpha:        
        print(line)

        #find the pair ara word for line[line_nu_eng](eng)
        #line_nu_ara = 0
        for line_ara in words_alpha2ara:
            if line_ara.find(str(line_nu_eng)):
                print("["+line_ara+"]")
                break

        #find the pair zhtw word for line[line_nu_eng](eng)
        #line_nu_zhtw = 0
        for line_zhtw in words_alpha2zhtw:
            if line_zhtw.find(str(line_nu_eng)):
                print("{"+line_zhtw+"}")
                break
 
        line_nu_eng += 1

if __name__ == '__main__':
#    add_num()    
    words_alpha_reunion()

