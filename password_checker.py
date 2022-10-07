from calendar import c
import sys
#döngü
while True:
    komut=["!",".","?","-"]
    #şifre girsin
    sifre=input("Password: ")


    #şifre 6 karakterden büyük mü
    if len(sifre)>= 16:
        print("Password must be less than or equal to 16 characters and contain special letters")
        continue
    if len(sifre) >=6:
        if "!"in sifre:
            print("Password Compatible")
            break
        elif "?"in sifre:
            print("Password Compatible")
            break
        elif "."in sifre:
                print("Password Compatible")
                break
        elif "'"in sifre:
                print("Password Compatible")
                break
    
        
    else:
        print("Password must be more than 6 characters")
        continue
        