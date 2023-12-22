import random

#met en place les attributs 
def Attribut():
    random1 = random.randint(1, 6)
    random2 = random.randint(1, 6)
    random3 = random.randint(1, 6)
    random4 = random.randint(1, 6)

    list = [random1, random2, random3, random4]
    list.sort()
    list.pop(0)
    list[0] + list[1] + list[2]

    if random1 < random2 and random1 < random3 and random1 < random4:
        return random2 + random3 + random4
    elif random2 < random3 and random2 < random4:
        return random1 + random3 + random4
    elif random3 < random4:
        return random1 + random2 + random4
    else:
        return random1 + random2 + random3

#definit les stats de base des Npc
class NPC:
    def __init__(self, nom, race, espece, profession):
        self.Force = Attribut()
        self.Agilite = Attribut()
        self.Constitution = Attribut()
        self.Intelligence = Attribut()
        self.Sagesse = Attribut()
        self.Charisme = Attribut()
        self.classe_armure = random.randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.points_vie = random.randint(1, 20)
        self.profession = profession

#definit caracteristique self
    def caracteristique(self):
        print("\nNom:", self.nom)
        print("Force:", self.Force)
        print("Agilite:", self.Agilite)
        print("Constitution:", self.Constitution)
        print("Intelligence:", self.Intelligence)
        print("Sagesse:", self.Sagesse)
        print("Charisme:", self.Charisme)
        print("Race:", self.race)
        print("Espece:", self.espece)
        print("Points de vie:", self.points_vie)
        print("Profession:", self.profession)

#definit classe JP
class JP(NPC):
    def attaquer(self, cible):
        attaque = random.randint(1, 20)
        if attaque == 20:
            dommages = random.randint(1, 8)
            cible.subir_dommages(dommages)
        elif attaque == 1:
            print("Aucun effet")
        else:
            if attaque > cible.classe_armure:
                dommages = random.randint(1, 6)
                cible.subir_dommages(dommages)

    def subir_dommages(self, dommages):
        self.points_vie -= (dommages - self.classe_armure)

#defni classe hero
class hero(NPC):
    def attaquer(self, cible):
        attaque = random.randint(1, 20)
        if attaque == 20:
            dommages = random.randint(1, 8)
            cible.subir_dommages(dommages)
        elif attaque == 1:
            print("Aucun effet")
        else:
            if attaque > cible.classe_armure:
                dommages = random.randint(1, 6)
                cible.subir_dommages(dommages)

    def subir_dommages(self, dommages):
        self.points_vie -= (dommages - self.classe_armure)