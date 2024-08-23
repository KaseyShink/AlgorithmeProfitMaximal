import operator


class Compteur:
    def __init__(self, text):
        self.text = text
        self.mots_a_retirer = ("de","le","la")
        self.symboles_a_retirer = (",",".")

    def compter_les_mots(self):
        mots = self.text.split()
        compte_de_mots = {}
        for mot in mots:
            for symbole in self.symboles_a_retirer:
                mot = mot.replace(symbole, "")
            if mot not in compte_de_mots:
                compte_de_mots[mot] = 1
            else:
                compte_de_mots[mot] += 1
            if mot in self.mots_a_retirer:
                del compte_de_mots[mot]

        mots_tries = sorted(compte_de_mots.items(), key=operator.itemgetter(1), reverse=True)
        return mots_tries
