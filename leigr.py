print("\n------------ Vägimees Leiger ------------\n")

#https://python.hotexamples.com/examples/gameStats/GameStats/-/python-gamestats-class-examples.html

def menu():
    print("[1] Alustage mänguga.")
    print("[2] Legend.")
    print("[3] Lahku mängust.")
    
menu()
valik = int(input("Sisestage valik: "))

while valik != 3:
    if valik == 1:
        #statid
        elud = 0 #max 100
        xp = 0 
        level = 0 #10 xpd 1 level
        jõud = 0 #max 10
        armor = 0 #max 50
        skoor = 0 #uueneb vastavalt

        
        
        
        
        
        
        
        
        
        
        
        
        
        print("m2ng")
    elif valik == 2:
        print("\nSelsamal ajal, kui Suur Tõll Saaremaal tähtsaid töid tegi\nelas Hiiumaal Tõlli vennapoeg Leiger.\nSeegi oli niisamasugune tugev mees nagu Suur Tõll,\n ehk küll viimane jõu poolest temast, üle käis.\nLeiger ja Suur Tõll armastasivad mõlemad vihtlemist.\nSuur Tõll käskinud Leigri sauna ehitada,tal enesel polla ehituseks aega.\nLeiger hakanudki tööle. Vedanud kümne sülla pikkused \npalgid metsast välja. Neist ehitanud siis \nvihtlemisesauna. Ahi saanud nii suur nagu saunamehe saun.\nKerisekivideks üksi vedanud Leiger seitse sülda ümmargusi kiva kokku.\nKui saun valmis saanud, tulnud Suur Tõll Hiiumaale \nsagedasti vihtlema. Leiger kütnud ahju tublisti soojaks, võtnud siis kummagi õla peale vaadi vett ja viinud leile viskamiseks sauna.\nPeale selle tapnud Leiger iga korra, kui Suur Tõll sauna tulnud, kaks härga ja keetnud need ära.\nSaunast ära tulles kutsunud Leiger Suure Tõlli ikka enese juure sööma.\nKumbki söönud terve härja ja teo leiva ära.\nOlnud kõht täis, siis läinud Suur Tõll Saaremaale magama, Leiger aga heitnud tihti sauna leiba luusse laskema.\nKuid, siis kui Leiger magas tuli vanapagan kes viis\n Leigri naise minema ning nii pidigi Leiger asuma pikale retkele.")    
    else:
        print("Sisestasite vale numbri")
    print()
    menu()
    valik = int(input("Sisestage oma valik: "))
    
print("Tänud kasutamast meie naturaalset produkti")











'''
#mängu alustamise menüü
def menuu():
    print("1 -- Alustage mänguga")
    print("2 -- Legend")
    print("3 -- lahku")
    
    valik = int(input("Sisestage oma valik: "))
    if option == 1:
        #mäng siia
    elif valik == 2
        print("legend")
    elif valik == 3:
        exit()
    else:
        print("Sisestasite vale numbri, vahemik on 1-3")
    menuu()
'''