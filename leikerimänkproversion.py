import random


#karakteri statid
characterHealth = 100

#vanapagana statid
enemyHealth = 100
enemyPunch = random.choice(range(0,20))
enemySword = 100


#karu statid
bearPunch = random.choice(range(3,9))

#skoor
unexpected_gameScore = -100
score = 0

#löögid
characterPunch = random.choice(range(0,21))
characterLegp = random.choice(range(20,40))
characterPee = random.choice(range(10,30))
characterJump = 69


#m2ngu alustamine
gameChoice = int(input("\nAlusta mänguga\n[1] -- Davs\n[2] -- Lahku mängust\n"))

#alustab m2ngu
if gameChoice == 1:
    
    print("\nAlustasite mänguga\n")
    
#lahkub mängust
elif gameChoice == 2:
    
    print("\nLahkusite\n")
    exit()
    
else:
    #kui on sisestatud vahemikust väline number tuleb see teade
    print("vale vahemik")
    
print("Sündisite Leigrina iiumaal.\nNäete kusagil kaugel Palumäel vanapaganat vanureid peksmas")

#löökide valik
gameChoice = int(input("Mida te teha soovite Leiger?:\n[1] -- Anna jalaga\n[2] -- Liitu temaga\n"))

if gameChoice == 1:
    if characterPunch > 3:
        
        #löögi hittimise puhul saad 10 skoori pointi
        score = score + 10
        enemyHealth = enemyHealth - characterPunch

        print("Andsite talle jalaga, mis tekitas talle",characterPunch,"dämmi\nMeie märajatsejal on alles",enemyHealth,"Hp")
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

#teekonna valik
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
    
    score = score - 4

    print("Teil on alles",score,"skoori punkti\n")
    print("Krabasite käbe maast puuoksa ning panite talle normi lataka vastu pääd\nRaisk sai surma :(\n")
    print("Selle peale te sattusite paanikasase ning jooksite sügavamale metsa\n")
    print("Järsult spawnis teie ette vanapagan\nAndiste talle uuesti löögi vastu pääd, millepeale ta kummuli kukkus ja hakkas nutma\n") 

    enemyHealth = enemyHealth - characterPunch

    print("Teie löök tegi talle üllatavalt",characterPunch,"dämmi\nTal on nyyd alles",enemyHealth,"elu\n")

    score = score + 10

    print("Pihta saamisega teenisite",score,"punkti,\n")
    print("Paratamatult ta koperdas, ning teil on nüüd valik kudias teda lüüa")

else:

    print("vale vahemik")

#löögi valik
gameChoice = int(input("[1] - Jalaga (min 20 DMG)\n[2] - Hüppad peale talle (lebo 69 DMG)\n[3] - Sülita näkku (max 30 DMG) \n"))

if gameChoice == 1:

    print("\nValisite jalaga lõõgi andmise\n")

    enemyHealth = enemyHealth - characterLegp

    print("Tegite vanamehele",characterLegp,"dämmi.\nTal on alles vaid",enemyHealth,"elu.")

    score = score + 10

elif gameChoice == 2:

    print("\nValisite peale hüppamise")

    enemyHealth = enemyHealth - characterJump

    print("Tegite vanamehele",characterJump,"dämmi.\nTal on nüüd",enemyHealth,"elu")

    score = score + 10

elif gameChoice == 3:

    print("\nValisite näkku sülitamise")

    enemyHealth = enemyHealth - characterPee

    print("Tegite vanamehele",characterPee,"dämmi.\nTal on",enemyHealth,"elu")

    score = score + 10

else:
    
    print("\nVale vahemik")

if enemyHealth >= 1:

    print('\nTeil tekkis uus võimalus talle lõuksi külvata, aga ta palus teil ennem külvamist luuletus läbi lugeda.\n\nHommik üle maja käib,\npuistab kambri päikest täis.\nKui sa ärkad, imestad\nKes mind nõnda pimestab?\nPäike palub: "Kas võin jääda?"\nSulle seltsiks kogu päeva\ntäna olema ma pean,\nsest üht saladust ma tean:\n"sul on täna sünnipäev!"\n')
    print("\nPange uuesti: ")

    gameChoice = int(input("[1] - Jalaga (min 20 DMG)\n[2] - Hüppad peale talle (lebo 69 DMG)\n[3] - Sülita näkku (max 30 DMG) \n"))
    
    if gameChoice == 1:

        print("\nValisite Jalaga andmise\n")

        enemyHealth = enemyHealth - characterLegp

        print("Tegite vanamehele",characterLegp,"dämmi.\nTal on alles vaid",enemyHealth,"elu.")

        score = score + 10

    elif gameChoice == 2:

        print("\nValisite peale hüppamise")

        enemyHealth = enemyHealth - characterJump

        print("Tegite vanamehele",characterJump,"dämmi.\nTal on nüüd",enemyHealth,"elu")

        score = score + 10

    elif gameChoice == 3:

        print("\nValisite näkku sülitamise\n")

        enemyHealth = enemyHealth - characterPee

        print("Tegite vanamehele",characterPee,"dämmi.\nTal on",enemyHealth,"elu")

        score = score + 10

    else:
        
        print("\nVale vahemik\n")

    if enemyHealth > 1:

        print("Kahjuks või siis juba õnneks, teil sai jõud otsa.\nVanapagan sai sellest aru, ja kasutas võimalust, et sulle mõõgaga vastu anda.\n")
        
        characterHealth = characterHealth - enemySword

        print("Vanapagan tegi teile",enemySword,"dämmi.")
        print("Teil paratamatult on alles",characterHealth,"elu\n")
        print("Te saite haledalt ülli ning kaotasite mängu.")

        #surma saamisega kaotab 10 punkti
        score = score - 10

        print("Teie skoor:",score,"\n")

    
    elif enemyHealth < 0:

        print("\nVõidsite mängu! WoopWoop\n")
        print("\nTeie skoori lõpptulemus on:",score,"\n")

elif enemyHealth < 0:

    print("Vanapeer sai surma")
    print("Võitiste mängu. Teie skoori lõpptulemus on:",score,"\n")
    