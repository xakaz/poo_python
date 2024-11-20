class Personne:
    def __init__(self)->None:
        self.nom = input("Entrez votre nom: ")
        self.prenom = input("Entrez votre prénom: ")
        self.age = input("Entrez votre âge: ")
        self.est_majeur = True if int(self.age) >= 18 else False

    def se_presenter(self)->str:
        return f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans. Je suis {'majeur' if self.est_majeur else 'mineur'}."


personne1 = Personne()
print(personne1.se_presenter())