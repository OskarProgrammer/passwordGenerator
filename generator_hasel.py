###generator haseł 
from random import choice
from os import system
y=0


litery="qwertyuiopasdfghjklzxcvbnm"
litery=list(litery)
cyfry="123456789"
cyfry=list(cyfry)
wielkosc="12"
wielkosc=list(wielkosc)
znaki_specjalne="!@#$%^&*:;~"
znaki_specjalne=list(znaki_specjalne)
haslo=""
def hasło(poziom,ilosc,haslo):
    lista=[]
    suma=[]
    if poziom==1:
        for x in range (0,ilosc):
            y=choice(litery)
            lista.append(y)
        
        haslo="".join(lista)
        print(f"Twoje haslo to {haslo}")
    elif poziom==2:
        for x in range (0,ilosc):
            suma=litery+cyfry
            y=choice(suma)
            lista.append(y)
        
        haslo="".join(lista)
        print(f"Twoje haslo to {haslo}")
    elif poziom==3:
        for x in range (0,ilosc):
            suma=litery+cyfry
            y=choice(suma)
            w=choice(wielkosc)
            if w=="1" :
                y=y.upper()
                lista.append(y)
            elif w=="2" :
                y=y.lower()
                lista.append(y)
        haslo="".join(lista)
        print(f"Twoje haslo to {haslo}")
    elif poziom==4:
        for x in range(0,ilosc):
            suma=litery+cyfry+znaki_specjalne
            y=choice(suma)
            w=choice(wielkosc)
            if w=="1" :
                y=y.upper()
                lista.append(y)
            elif w=="2" :
                y=y.lower()
                lista.append(y)
        haslo="".join(lista)
        print(f"Twoje haslo to {haslo}")

system("cls")
print("1.Poziom (same litery alfabetu greckiego")
print("2.Poziom (litery + cyfry ")
print("3.Poziom (litery + cyfry + rozna wielkosc znakow ")
print("4.Poziom (litery + cyfry + rozna wielkosc znakow + znaki specjalne  ")

poziom=int(input("Jakiego poziomu chcesz miec haslo:"))

ilosc=int(input("Podaj ilosc znakow  w twoim hasle: "))
system("cls")
print(f"Twoje haslo bedzie poziomu {poziom} oraz bedzie miec {ilosc} znakow ")
hasło(poziom,ilosc,haslo)###generator !!!
