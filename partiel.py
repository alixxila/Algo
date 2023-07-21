class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.emprunte_par = None

class Magazine:
    def __init__(self, titre, numero, date_publication):
        self.titre = titre
        self.numero = numero
        self.date_publication = date_publication

class Utilisateur:
    def __init__(self, nom, id_utilisateur):
        self.nom = nom
        self.id_utilisateur = id_utilisateur
        self.livres_empruntes = []

bibliotheque = []

def ajouter_livre(titre, auteur, isbn):
    livre = Livre(titre, auteur, isbn)
    bibliotheque.append(livre)

def ajouter_magazine(titre, numero, date_publication):
    magazine = Magazine(titre, numero, date_publication)
    bibliotheque.append(magazine)

def emprunter_livre(utilisateur, livre):
    if livre.emprunte_par is None:
        livre.emprunte_par = utilisateur
        utilisateur.livres_empruntes.append(livre)
        print(f"{livre.titre} a été emprunté par {utilisateur.nom}.")
    else:
        print(f"{livre.titre} est déjà emprunté par {livre.emprunte_par.nom}.")

def rendre_livre(utilisateur, livre):
    if livre.emprunte_par == utilisateur:
        livre.emprunte_par = None
        utilisateur.livres_empruntes.remove(livre)
        print(f"{livre.titre} a été rendu par {utilisateur.nom}.")
    else:
        print(f"{livre.titre} n'a pas été emprunté par {utilisateur.nom}.")

def chercher_livre_par_titre(titre):
    resultats = [livre for livre in bibliotheque if isinstance(livre, Livre) and livre.titre == titre]
    return resultats

def chercher_livre_par_auteur(auteur):
    resultats = [livre for livre in bibliotheque if isinstance(livre, Livre) and livre.auteur == auteur]
    return resultats

def livres_empruntes_par_utilisateur(utilisateur):
    return utilisateur.livres_empruntes

#Test de l'utilisation :
utilisateur1 = Utilisateur("Toto", 1)
ajouter_livre("1984", "George Orwell", "9780451524935")
ajouter_magazine("Science et Vie", "Vol. 2023", "Janvier 2023")
livre1 = chercher_livre_par_titre("1984")[0]
emprunter_livre(utilisateur1, livre1)
print(livres_empruntes_par_utilisateur(utilisateur1))
