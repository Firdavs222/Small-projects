# -*- coding: utf-8 -*-
"""
@author: Firdavs Shavqiddinov
"""


import random as r
from uzwords import words

def get_word():
    word = r.choice(words)
    while "-" in word or " " in word:
        word = r.choice(words)
    return word.upper()
    
def display(letters,word):
    display_letter = ""
    for letter in word:    
        if letter in letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def suz_top_uyini():
    word = get_word()
    word_letters = set(word)
    user_letters = ""
    msg = f"Men {len(word)} ta harfli so'z o'yladim, uni topa olasizmi?"
    msg += " O'yinni to'xtatish uchun 'STOP' deb yozing"
    print(msg)
    
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            
        letter = input("Harf kiriting:").upper()
        if letter.upper() == "STOP":
            print("Afsus siz bu so'zni topa olmadingiz ):")
            break
        else:
            if letter in user_letters:
                print("Bu harfni oldinam kiritgansiz. Iltimos boshqa harf kiriting:")
                continue
            elif letter in word:
                word_letters.remove(letter)
                print(f"{letter} harfi to'g'ri!")
            else:
                print("Bunday harf yo'q!")
            if len(word_letters) == 0 :
                print(f"Tabriklayman siz {word} so'zini {len(user_letters)} ta urinish bilan topdingiz!")
        user_letters += letter

        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
