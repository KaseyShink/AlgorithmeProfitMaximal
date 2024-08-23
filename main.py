from compteur import Compteur

fichier = open("Text.txt","r",encoding='utf8')
text = fichier.read()
fichier.close()

compteur = Compteur(text)

mots = compteur.compter_les_mots()
print(mots)