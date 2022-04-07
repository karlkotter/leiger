#https://www.instructables.com/How-to-Create-a-Python-Text-Based-Game/
def game():
    
    print("\n------------ Vägimees Leiger ------------\n")
    menu = input("\n [1] Alusta\n [2] Lahku")
    
    if menu.lower()=="1":
        print("Alustasid mängu")
        start = True
        inventory = []
    else:
        print("Lahkusid mänust")
        
    
    if start == True:
        print("\nSelsamal ajal, kui Suur Tõll Saaremaal tähtsaid töid tegi\nelas Hiiumaal Tõlli vennapoeg Leiger.\nSeegi oli niisamasugune tugev mees nagu Suur Tõll,\n ehk küll viimane jõu poolest temast, üle käis.\nLeiger ja Suur Tõll armastasivad mõlemad vihtlemist.\nSuur Tõll käskinud Leigri sauna ehitada,tal enesel polla ehituseks aega.\nLeiger hakanudki tööle. Vedanud kümne sülla pikkused \npalgid metsast välja. Neist ehitanud siis \nvihtlemisesauna. Ahi saanud nii suur nagu saunamehe saun.\nKerisekivideks üksi vedanud Leiger seitse sülda ümmargusi kiva kokku.\nKui saun valmis saanud, tulnud Suur Tõll Hiiumaale \nsagedasti vihtlema. Leiger kütnud ahju tublisti soojaks, võtnud siis kummagi õla peale vaadi vett ja viinud leile viskamiseks sauna.\nPeale selle tapnud Leiger iga korra, kui Suur Tõll sauna tulnud, kaks härga ja keetnud need ära.\nSaunast ära tulles kutsunud Leiger Suure Tõlli ikka enese juure sööma.\nKumbki söönud terve härja ja teo leiva ära.\nOlnud kõht täis, siis läinud Suur Tõll Saaremaale magama, Leiger aga heitnud tihti sauna leiba luusse laskema.\nKuid, siis kui Leiger magas tuli vanapagan kes viis\n Leigri naise minema ning nii pidigi Leiger asuma pikale retkele. Elas Hiiumaal Tõlli vennapoeg Leiger.")    
    choice=input("\nOma teel tuleb Leigrile ette 2 teed.\n Vali teekond: [1] Vasakule [2] Paremale:\n")
    if choice.lower()=="1":
        choice1=True
        print("Läksid teelt vasakule ning leidsid maast kulda")
        inventory.append("Kuld")
        
    else:
        choice1=False
        print("Läksid paremale ning leidsid põõsast kaardi")
        inventory.append("Kaart")
        
    if choice1==False and "Kaart" in inventory:
        decide=input("Seejärel vaatab Leiger kaarti ja sealt peaks ta edasi minema Ida suunas\n [1] Mine idasse [2] Mine lõunasse")
        #decide.lower()=="1":
        print("Läksid mööda teed edasi")
        #elif decide.lower()=="2":
        approach1=input("Lõuna pooles minnes tulid sulle ette Ristid\nKas võidelda nendega? [1] JAH [2] EI\n")
            
    
game()