class EtreVivant:
    ESPECE_ETRE_VIVANT = "(être vivant non identifié)"

    def  Afficher_info_etre_vivant(self):
        return f"Info être vivant: {self.ESPECE_ETRE_VIVANT}."


class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"

    def __init__(self, nom:str, age:int)->None:
        self.nom = nom
        self.age = age

    def miauler(self)->str:
        return f"{self.nom} dit : Miaou !"

class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (Mammifère homo sapiens)"

    def __init__(self, nom:str, prenom:str,age:int)->None:
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.est_majeur = True if int(self.age) >= 18 else False

    def SePresenter(self)->str:
        return f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans. Je suis {'majeur' if self.est_majeur else 'mineur'}."

class Etudiant(Personne):
    ESPECE_ETRE_VIVANT = "Etudiant (Humain)"

    def __init__(self, nom: str, prenom: str, age:int, etude: str)->None:
        super().__init__(nom,prenom,age)
        self.etude = etude

    def SePresenter(self)->str:
        print(super().SePresenter())
        return f"Je suis étudiant en {self.etude}."


personne1 = Personne("Doe", "John", 25)
etudiant1 = Etudiant("Doe", "John", 17,"Informatique")

print(personne1.SePresenter())
print(etudiant1.SePresenter())
print(etudiant1.Afficher_info_etre_vivant())
