# Mise en place d'un algo qui va fournir le tarif du sejour selon le type de séjour et l'age de la personne

# On demande l'âge
# On demande le type de forfait
# On renvoie le tarif

age = 0
type_forfait = 0

tarif = [
    {
        "adulte": 25.80,
        "-12": 18.70,
        " +60": 21.40
    },
    {
        "adulte": 510,
        "-12": 300,
        "+60": 340
    }
]

def tarif_sejour(forfait, age):
    
    statut = None
    price = 0

    if age >= 0 and age < 12:
        statut = "-12"
    elif age > 60:
        statut = "+60"
    else:
        statut = "adulte"

    if forfait == 1:
        price = tarif[0][statut]
    elif forfait == 2:
        price = tarif[1][statut]

    return price

print("*******")
print("Bienvenue à la station de ski LES OURS BRUNS")
print("*******")
print()

try:
    print("Quel type de forfait souhaitez-vous avoir?")
    print(" 1. 1 journée")
    print(" 2. Saison")
    type_forfait = int(input("Tapez 1 ou 2: "))
except:
    print("Erreur: Valeur incorrect")    

try:
    age = int(input("Quel âge avez-vous? "))
except:
    print("Erreur: Valeur incorrect")

prix = tarif_sejour(type_forfait, age)

print(f"Vous avez choisi un forfait {"1 journée " if type_forfait==1 else "saison "} pour une personne de {age} ans. Vous devrez payer: {prix}€.")