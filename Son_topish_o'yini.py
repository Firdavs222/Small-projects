

import random as r

def son_top(x=10):
    taxminlar=0
    son=r.randint(1,x)
    while True:
        taxminlar +=1
        javob=int(input(f"1 dan to {x} gacha sonlar ichidan o'ylagan sonimni kiriting:"))
        if javob>son:
            print("Men o'ylagan son bundan kichikroq. Boshqa son kiriting:")
        elif javob<son:
            print("Men o'ylagan son bundan kattaroq. Boshqa son kiriting:")
        elif javob==son:
            break
    print(f"Siz to'g'ri topdingiz, men o'ylagan son {son} ga teng edi. Tabriklayman!")
    return taxminlar
  

def sonimni_top(x=10):
    print(f"1 dan to {x} gacha biror-bir raqam o'ylang!")
    quyi=1
    yuqori=x
    taxminlarim=0
    while True:
        taxminlarim +=1
        taxmin=r.randint(quyi, yuqori)
        javob=input(f"Siz o'ylagan son {taxmin} ga tengmi(t), yoki kattaroq(+), yoki kichikroq(-)?".lower())
        if javob=="-":
            yuqori=taxmin-1
        elif javob=="+" :
            quyi = taxmin + 1
        elif javob=="t" :
            break
    print("Men to'g'ri topdim!")
    return taxminlarim


def son_top_uyini(x=10):
    while True:        
        taxminlar_odam = son_top(x)
        taxminlar_komp = sonimni_top(x)
        if taxminlar_odam <taxminlar_komp:
            print(f"Tabriklayman siz {taxminlar_odam} ta taxmin bilan yutdingiz!")
        elif taxminlar_odam>taxminlar_komp:
            print(f"Afsuski men {taxminlar_komp} ta taxmin bilan yutdim!")
        else:
            print("O'yin durrang bilan tugadi!")   
        savol = input("Yana o'ynashni xohlaysizmi?(ha/yo'q)".lower())
        if savol != "ha" :
            break

























