class Personne:
    def __init__(self, nom:str, prenom:str, age:int)->None:
        self.nom = input("Entrez votre nom: ")
        self.prenom = input("Entrez votre prénom: ")
        self.age = input("Entrez votre âge: ")

    def se_presenter(self)->str:
        return f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans."


personne1 = Personne("Doe", "John", 30)
print(personne1.se_presenter())