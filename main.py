class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom
        self.age = age
        self.genre = genre

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        genre_str = "Masculin " if self.genre else " Feminin"
        print(f"Genre : {genre_str}")
        e_optionnel = "" if self.genre else "e"
        if self.EstMajeur():
            print("Je suis majeur" + e_optionnel)
        else:
            print("Je suis mineur" + e_optionnel)

        print()

    def EstMajeur(self):
        return self.age >= 18


personne1 = Personne("Jean", 30, True)
personne1.SePresenter()
personne2 = Personne("Mathilde",12,False)
personne2.SePresenter()
