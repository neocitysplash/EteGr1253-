class Personne:
    def __init__(self, p_nom, p_prenom, p_age):
        self.nom = p_nom
        self.prenom = p_prenom
        self.age = p_age
    def presenteToi(self):
        print("Je suis", self.prenom, "et j'ai", self.age, "ans.")

class Etudiant(Personne):
    def __init__(self, p_nom, p_prenom, p_age, p_NumEtudiant, p_Groupe, p_AnneeGraduation):
        super().__init__(p_nom, p_prenom, p_age)
        self.NumEtudiant = p_NumEtudiant
        self.Groupe = p_Groupe
        self.AnneeGraduation = p_AnneeGraduation
    def presenteToi(self):
        print("Je suis", self.prenom, "et je suis dans le groupe", self.Groupe)

class Employee(Personne):
    def __init__(self, p_nom, p_prenom, p_age, p_NumEmployee, p_Service, p_Bureau):
        super().__init__(p_nom, p_prenom, p_age)
        self.NumEmployee = p_NumEmployee
        self.Service = p_Service
        self.Bureau = p_Bureau
    def presenteToi(self):
        print("Je suis", self.prenom, "et je suis dans le service", self.Service)

class Enseignant(Employee):
    def __init__(self, p_nom, p_prenom, p_age, p_NumEmployee, p_Service, p_Bureau, p_Departement):
        super().__init__(p_nom, p_prenom, p_age, p_NumEmployee, p_Service, p_Bureau)
        self.Departement = p_Departement
    def presenteToi(self):
        print("Je suis", self.prenom, "et je suis dans le département", self.Departement)

# Création des objets : Instantiation
liste = []
liste.append(Personne('babari', 'raouf', 31))
liste.append(Personne('bachir', 'Fikry', 25))
liste.append(Personne('Nabil', 'Agsous', 40))
E1 = Etudiant(liste[1].nom, liste[1].prenom, liste[1].age, 1234567, 1253, 2024)
E2 = Etudiant('Nabil', 'Agsous', 40, 1234567, 1253, 2024)
Em1 = Employee('brahim', 'hbaieb', 42, 12345, 'informatique', 'maintenance')
Ens1 = Enseignant('Marwa', 'letaief', 18, 123654, 'informatique', 'maintenance', 'Réseau')

liste.append(E1)
liste.append(E2)
liste.append(Em1)
liste.append(Ens1)
# constructeur V2 : E3 = Etudiant('Nabil', 'Agsous', 40, 1234567, 1253, 2024)
# Les objets de la même classe se comportemt souvent de la même manière ...

for x in liste:
    x.presenteToi()