
from types import coroutine


WORD_BANK=[]
def menue():
    print("< Translate >")
    print("""    1-> add new word 
    2-> translation english2persian 
    3-> translation persian2english 
    4->exit""")


def load_data():
    try:
        with open('words_bank.txt','r') as f:
            BIG_TEXT=f.read()
            words = BIG_TEXT.split('\n')

            for i in range(0,len(words),2):
                WORD_BANK.append({'en':words[i] , 'fa':words[i+1]})

        #for w in WORD_BANK:
            #print(w)
    except:
        print("The file could not be found and opened")

def translate_en2per(input_Text):
    user_word=input_Text.split(' ')
    text=""
    for UW in user_word:
        for word in WORD_BANK:
            if UW == word['en']:
                text+=word['fa'] + ' '
                break
        else:
            text+=UW+ ' '
    return text


def translate_per2en(input_Text):
    user_word=input_Text.split(' ')
    text=""
    for UW in user_word:
        for word in WORD_BANK:
            if UW == word['fa']:
                text+=word['en'] + ' '
                break
        else:
            text+=UW+ ' '
    return text

def add():
    eng=input("Enter your English word:")
    per=input("Enter the Persian means:")
    f=open('words_bank.txt','a')
    f.write('\n'+eng+'\n'+per)
    f.close()


load_data()

while True:

    menue()
    ch=int(input("Enter your choise:"))
    
    if ch==1:
        add()

    elif ch==2:
        user_text=input("enter your text: ") 
        output_text=translate_en2per(user_text)
        print(output_text)

    elif ch==3:
        user_text=input("enter your text: ") 
        output_text=translate_per2en(user_text)
        print(output_text)

    elif ch==4:
        break
    


