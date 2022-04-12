def game():
    
    import random
    
    answer = input("Alusta mängu\n [1] JAH\n [2] EI\n")
    print("-------------VÄGIMEES  LEIGER---------------")
    if answer.lower()=='1':
        print("Tere tulemast")
        start=True
        inventory=[]
        
    else:
        print("Lahkusid mängust")
        
        
    if start==True:
        print("Näed vanapaganat röövimas su naist")
        choice=input("Mine talle järgi\n [1] JAH\n [2] EI\n")
        
        if choice()=='1':
            choiceY1=True
            print("Lähed vanapaganale järgi nin leiad tee peal leiad mõõga")
            inventory.append("Mõõk")
            
        else:
            choiceY1=False
            print("Lähed mööda teist teed ning leiad kaarti")
            inventory.append("Kaart")
            
        if choiceY1==False and "Kaart" in inventory:
            print("Kaarti järgi peaksid sa minema Lõuna suunas")
            decide=input("Kas lähed\n [lõuna] \n[ida]\n")
            
        elif choiceY1==True:
            print("Lähed Lõunasse ja näed seal kedagi")
            approach=input("Kas lähed talle lähemale?\n[1] JAH\n[2] EI\n")
            
           #if approach()='2':
            #    print("Kusik")
             #   print("MÄNG LÄBI")
            
        if decide.lower()== 'lõuna':
            print("Sa läksid mööda teed edasi, kuid ei näinud massiivset auku ning kukkusid sinna sisse ja said surma")
            print("MÄNG LÄBI")
            
        elif decide.lower()== 'ida':
            approachl=input("Sa jõudsid metsa ning seal näed vargaid kes tahavad sinuga võidelda, \[jah] Võitle nendega\n[ei] Jookse minema\n")
        
        if approach.lower()=='ei':
            print("Kusik")
            print("MÄNG LÄBI")
        
        if approach.lower()=='jah':
            print("Hakkasid nendega võitlema, mida teha?\n[A] Tõmba lõuksi\n[B] Pane varbaga\n[C] Kasuta mõõka")
            decision=input("Mida kasutad [A] [B] [C] ?")
            
            minPoint=1
            maxPoint=100
            
            #ChA = (random.randint(minPoint, maxPoint)) *. 85
            #ChB = (random.randint(minPoint, maxPoint)) *. 33
            #ChC = (random.randint(minPoint, maxPoint)) *. 95
            
        if decision.upper()=='A' and ChA>25:
            print("Sa tõmbasid talle lõuksi\n Vend lendas nokki")
        elif decision.upper()=='B' and ChB>25:
            print("Panid varbaga \n Varbad haisesid nii hullusti, et tüüp pani sussid püsti")
        elif decision.upper()=='C' and ChC>25 and 'Mõõk' in inventory:
            print("Tõmbasid välja oma suure hiiglasliku tohutu gigantse hiilgava võmba, oih mõõga*\nVastane pani hirmust pagema")
        
        else:
            print("Said ise vastu hambaid")
            print("MÄNG LÄBI")
        

game()