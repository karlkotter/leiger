def character():
    character_name = input("Sisestage oma karakteri nimi: ")
    character_health = 100
    character_strenght = 20
    character_naised = 0
    print("\nTeie karakteri nimi on",character_name,"\nTeil on:\n",character_health,"HP\n",character_strenght,"Tugevust\n",character_naised,"Naist\n")
    

def enemy_boss():
    enemy_name = "Vanapagan"
    enemy_health = 100
    enemy_strenght = 10
    enemy_naised = 12
    
    print("Teie ette ilmus",enemy_name,"\nTal on:\n",enemy_health,"HP\n",enemy_strenght,"Tugevust\n",enemy_naised,"Naist\n")
enemy_hunt():
    enemy_name = "Hunt"
    enemy_health = 50
    enemy_strenght = 19
    
def loll():
    enemy = enemy_hunt()
    print("Jalutasite metsas Hundile otsa")
    choice = input("[1] Pohh pab käega v\n[2] Rüüpa kiviga\n[3] Näita nokut (OP)\n[4] löö kusema ja pane pagema\n")
        if choice == 1:
            print('Valisite "Pohh pab käega v"')
loll()
