import random


#karakteri statid
characterHealth = 100

#vanapagana statid
enemyHealth = 100
enemyPunch = random.randint(0,20)
#karu statid
bearPunch = random.randint(3,9)
#skoor
#sen see kui vahele jääd pedofiilsusega 
unexpected_gameScore = -100
score = 0
#löögid
characterPunch = random.choice(range(0,21))
characterLegp = random.choice(range(20,40))
characterPee = random.randint(10,30)
characterJump = 69

#m2ngu alustamine
gameChoice = int(input("\nAlusta mänguga\n[1] -- Davs\n[2] -- mkm tp - tao pihku aka tao onni\n"))

if gameChoice == 1:
    
    print("\nAlustasite mänguga\n")
    
elif gameChoice == 2:
    
    print("\nLahkusite\n")
    exit()
    
else:
    
    print("vale vahemik")
    
print("Sündisite Leigrina iiumaal.\nNäete kusagil kaugel Palumäel vanapaganat lapsi käperdamas")
gameChoice = int(input("Mida te teha soovite Leiger?:\n[1] -- Anna jalaga\n[2] -- Liitu temaga\n"))
if gameChoice == 1:
    if characterPunch > 3:
        
        #löögi hittimise puhul saad 10 skoori pointi
        score = 0 + 10
        enemyHealth = enemyHealth - characterPunch
        print("Andsite talle jalaga, mis tekitas talle",characterPunch,"dämmi\nMeie pedofiilil on alles",enemyHealth,"Hp")
        print("Saite löögi pihta panemisega",score,"punkti")
        print("\nKahjuks vanapagan pani jooksu. \nHint: tan metsas puu taga\n")

elif gameChoice == 2:
    
    print("\nLiitusite vanapaganaga, kuid jäite politseile vahele, kes sattus teile kogematta peale.\n")
    print("\nKaotasite Mängu!\nSkoor:",unexpected_gameScore,"\nTeil on abi vaja\nUuesti alustamiseks käivitage mäng\n")
    exit()

else:
    
    #tegelt ei valinud, mdea kumb mähib siin, kas mina v see kood    
    print("vale vahemik, valisime teile 1 valiku\n")
    
gameChoice = int(input("Te mõtlesite teda otsima minna ning teile jäi silma 2 teekonda kust minna\n[1] -- Minge küsige kaas liiklejatelt, kas nad on näinud juhuslikult vanapaganat.\n[2] -- Minge mööda lambist matkarada\n"))

if gameChoice == 1:
    
    print("\nLeidsite paar venda Kärdlast, kuigi te ei saanud neilt infi, sealt edasi")
    print("liikusite edasi Kõppu. Kuid kukkusite ja saite surma xD")
    print("Saite haledalt ülli, mängu alustamiseks käivitage mäng uuesti.")
    quit()
    
elif gameChoice == 2:
    
    print("\nKõndisite paar KM metsarajal ning leidsite kummalised jalajäljed\n")
    print("\nTe hakkasite uurima neid, ning tuli välja, et see oli karu oma, kes pesitseb lähedal.\n")
    print("\npaarkümmend sammu edasi liikudes märkas ta teid.\n Ta tuli teile kallale ja saite talt 12 dämmi\n")
    characterHealth = characterHealth - bearPunch
    print("\nTeil on",characterHealth,"elu alles.\n")
    print("Kaotasite löögi tagajärjel 4 skoori punkti")
    score = 10 - 4
    print("Tei l on alles",score,"skoori punkti\n")
    print("Krabasite käbe maast puuoksa ning panite talle normi lataka vastu pääd\nRaisk sai surma :(\n")
    print("Selle peale te sattusite paanikasase ning jooksite sügavamale metsa\n")
    print("Järsult spawnis teie ette vanapagan\nAndiste talle uuesti löögi vastu pääd, millepeale ta kummuli kukkus ja hakkas nutma\n") 
    enemyHealth = enemyHealth - characterPunch
    print("Teie löök tegi talle üllatavalt",characterPunch,"dämmi\nTal on nyyd alles",enemyHealth,"elu\n")
    score = +10
    print("Pihta saamisega teenisite",score,"punkti,\n")
    print("Paratamatult ta koperdas, ning teil on nüüd valik kudias teda lüüa")
else:
    print("vale vahemik")
    
       
       
gameChoice = int(input("[1] - Jalaga (min 20 DMG)\n[2] - Hüppad peale talle (lebo 69 DMG)\n[3] - Pissi peale (max 30 DMG) \n"))

if gameChoice == 1:

    print("\nValisite jaalga lõõgi andmise\n")
    enemyHealth = enemyHealth - characterLegp
    print("tegite vanamehele",characterLegp,"dämmi.\nTal on alles vaid",enemyHealth,"elu.")
    
elif gameChoice == 2:

    print("Valisite pepale hüppamise")
    enemyHealth = enemyHealth - characterJump
    print("tegite vanamehele",characterJump,"dämmi.\nTal on nüüd",enemyHealth,"elu")
    
elif gameChoice == 3:

    print("Valisite peale pissimise")
    enemyHealth = enemyHealth - characterPee
    print("Tegite vanamehele",characterPee,"dämmi.\nTal on",enemyHealth,"elu")

else:
    
    print("Vale vahemik")
    
if enemyHealth
