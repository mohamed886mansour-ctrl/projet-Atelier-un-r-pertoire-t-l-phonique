#repertoire.py — Petit répertoire téléphonique en ligne de commande.
#Auteur : [med yassine , med amin , mouheb]


# ---------------------------------------------------------------------------
# I. LE NOYAU DU PROJET
# ---------------------------------------------------------------------------


def afficher(contacts):
    #Affiche tous les contacts, tries par ordre alphabetique du nom.
    if not contacts:
        print("Repertoire vide.")
        return

    for nom in contacts:
        numero = contacts[nom]
        print("  " + nom + " : " + numero)



    #Ajoute un contact, sauf si le nom existe deja.
    if nom in contacts:
        print("Le contact " + nom + " existe deja : " + contacts[nom])
        return
def ajouter(contacts, nom, numero):
    contacts[nom] = numero
    print("Contact " + nom + " ajoute.")


def chercher(contacts, nom):
    #Renvoie le numero du contact, ou Non si le nom est absent.
    return contacts.get(nom,"contact non trouve")


def supprimer(contacts, nom):
    #Supprime un contact s'il existe, sinon informe l'utilisateur.
    if nom not in contacts:
        print("Le contact " + nom + " n'existe pas.")
        return

    del contacts[nom]
    print("Contact " + nom + " supprime.")


def nombre_contacts(contacts):
    #Renvoie le nombre total de contacts.
    return len(contacts)
