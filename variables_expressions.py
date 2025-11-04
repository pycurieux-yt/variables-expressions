## Variables

# Nombre Entier (int)
mon_entier: int = 100
mon_entier2: int = 50
# print(type(mon_entier))

# Chaîne de caractère (str)
ma_chaine: str = "pycurieux"
# mon_entier(100) -> "100"

# Booléen (bool)
mon_booleen_vrai: bool = True
# Nombre flottant (float)

mon_flottant: float = 100.0
# Déclaration puis Assignation (ou 2 en 1)
ma_chaine2: str = "pycurieux \n"

## Expressions

# Arithmétiques (+ - * / // % **)
exp_arithm: float = 5 / 2
# Comparaison (== != > < >= <=)
exp_comp: bool = (mon_entier <= mon_entier2)
print(exp_comp)

# Logique (and or not)

exp_logique: bool = exp_comp or (True and True)
print(exp_logique)

# Convertisseur € → $
euros = float(input("Montant en € ? "))
taux = 1.15
dollars = euros * taux
print(str(euros) + "€ -> " + str(round(dollars, 2)) + "$")
