def afficher_jeu(M):
    """
    Affiche le plateau avec le numéro des lignes/colonnes.
    """
    print("  1 2 3\n"
          f"1:{M[0][0]}|{M[0][1]}|{M[0][2]}\n"
          f"2:{M[1][0]}|{M[1][1]}|{M[1][2]}\n"
          f"3:{M[2][0]}|{M[2][1]}|{M[2][2]}\n")


def afficher_regles():
    print("Le but du jeu est d’aligner avant son adversaire 3 symboles "
          "identiques horizontalement, verticalement ou en diagonale.\n"
          "Chaque joueur a donc son propre symbole, généralement une"
          "croix pour l’un et un rond pour l’autre.\n"
          "Une fois qu'un joueur a fini de jouer c'est à l'autre jusqu'à"
          " la fin de la partie.")


def lancement():
    """
    Lance le jeu, fonction principale du programme.
    """
    afficher_regles()
    print()  # Ajoute un retour à la ligne.
    menu()


def menu():
    """
    Permet à l'utilisateur de sélectionner ce qu'il veut faire.
    """
    termine = False
    while not termine:
        n = int(input("Entrez un nombre pour commencer la partie:\n"
                      "- 1: pour jouer contre l'ordinateur\n"
                      "- 2: pour jouer avec un autre joueur\n"
                      "- 3: pour charger la dernière partie sauvegardée\n"))

        M = creer_grille_vide()
        if n == 1:
            jouer_seul(M)
            termine = True
        elif n == 2:
            jouer_a_deux(M)
            termine = True
        elif n == 3:
            type_partie, M, tour_a = charger_partie()
            if type_partie == partie_seul_type:
                jouer_seul(M, tour_a)
                termine = True
            elif type_partie == partie_deux_joueur_type:
                jouer_a_deux(M, tour_a)
                termine = True
            else:
                print(f"Une erreur c'est produite durant le chargement de la partie")
        else:
            print(f"Aucun choix n'est associé au nombre {n}.")


def jouer_seul(M, tour_a=1):
    """
    Boucle de jeu pour jouer avec l'ordinateur.
    """
    gagnant = -1
    while gagnant == -1:
        afficher_jeu(M)
        symbole = symbole1 if tour_a == 1 else symbole2

        if tour_a == 1:
            print(f"C'est à vous de jouer avec les \"{symbole}\".")
            ligne, colonne = demander_position(M)
            if ligne is colonne is None:
                sauvegarder_partie(partie_seul_type, M, tour_a)
                return
        else:
            print(f"C'est à l'ordinateur de jouer avec les \"{symbole}\".")
            ligne, colonne = deviner_position(M)

        modifier_symbole(M, ligne, colonne, symbole)
        gagnant = partie_finie(M)
        tour_a = 1 if tour_a == 0 else 0  # ou tour_a = 1 - tour_a

    afficher_jeu(M)
    if gagnant == 0:
        print("La partie se termine sur un match nul!")
    else:
        symbole = symbole1 if gagnant == 1 else symbole2
        print("La partie est terminée.")
        if gagnant == 1:
            print(f"Vous avez gagné avec les \"{symbole}\"!")
        else:
            print(f"L'ordinateur a gagné avec les \"{symbole}\"!")


def jouer_a_deux(M, tour_a=1):
    """
    Boucle de jeu pour jouer à deux joueurs.
    """
    gagnant = -1
    while gagnant == -1:
        afficher_jeu(M)
        symbole = symbole1 if tour_a == 1 else symbole2
        print(f"C'est au joueur numéro {tour_a} de jouer avec les \"{symbole}\".")

        ligne, colonne = demander_position(M)
        if ligne is colonne is None:
            sauvegarder_partie(partie_deux_joueur_type, M, tour_a)
            return

        modifier_symbole(M, ligne, colonne, symbole)
        gagnant = partie_finie(M)
        tour_a = 1 if tour_a == 0 else 0  # ou tour_a = 1 - tour_a

    afficher_jeu(M)
    if gagnant == 0:
        print("La partie se termine sur un match nul, aucun joueur n'a gagné!")
    else:
        symbole = symbole1 if gagnant == 1 else symbole2
        print("La partie est terminée.")
        print(f"Le joueur numéro {gagnant} a gagné avec les \"{symbole}\"!")


def partie_finie(M):
    """
    Renvoie -1 si la partie n'est pas terminée, 0 s'il y a match nul, 1 si le symbole1 gagne, 2 si le symbole2 gagne.
    """
    if grille_pleine(M):
        return 0

    if symbole_gagne(M, symbole1):
        return 1

    if symbole_gagne(M, symbole2):
        return 2

    return -1


def grille_pleine(M):
    """
    Renvoie si la grille est pleine.
    """
    for i in range(3):
        for j in range(3):
            if M[i][j] == symbole_vide:
                return False

    return True


def symbole_gagne(M, symbole):
    """
    Renvoie si le symbole `symbole` à gagner la partie, c'est-à-dire, s'il y a une colonne/ligne/diagonale du symbole.
    """
    diagonale1_complete = True
    diagonale2_complete = True
    for i in range(3):
        ligne_complete = True
        colonne_complete = True

        if M[i][i] != symbole:
            diagonale1_complete = False
        if M[2 - i][i] != symbole:
            diagonale2_complete = False

        for j in range(3):
            if M[i][j] != symbole:
                ligne_complete = False
            if M[j][i] != symbole:
                colonne_complete = False

        if ligne_complete or colonne_complete:
            return True

    return diagonale1_complete or diagonale2_complete


def deviner_position(M):
    """
    L'ordinateur renvoie la position (ligne/colonne) à laquelle il souhaite jouer.
    TODO
    """
    pass


def demander_position(M):
    """
    Demande une position (ligne/colonne) au joueur pour y placer son symbole.
    NB : renvoie (None, None) si le joueur souhaite sauvegarder et arrêter la partie.
    """
    ligne = -1
    colonne = -1
    valide = False

    while not (0 <= ligne < 3 and 0 <= colonne < 3 and valide):
        ligne = int(input(
            "Veuillez entrer le numéro de la ligne à laquelle vous souhaitez jouer (ou 0 pour enregistrer): ")) - 1
        if ligne == -1:
            return None, None

        colonne = int(input(
            "Veuillez entrer le numéro de la colonne à laquelle vous souhaitez jouer (ou 0 pour enregistrer): ")) - 1
        if colonne == -1:
            return None, None

        valide = secure_est_vide(M, ligne, colonne)
        if not valide:
            print(f"Un symbole est déjà placé à la ligne {ligne + 1} et colonne {colonne + 1}.")

    return ligne, colonne


def secure_est_vide(M, ligne, colonne):
    """
    Renvoie True si l'emplacement `ligne` et `colonne` est invalide.
    Renvoie si l'emplacement à la ligne `ligne` et à la colonne `colonne` est vide sinon.
    """
    if not (0 <= ligne < 3 and 0 <= colonne < 3):
        return True

    return est_vide(M, ligne, colonne)


def est_vide(M, ligne, colonne):
    """
    Renvoie si l'emplacement à la ligne `ligne` et à la colonne `colonne` est vide.
    """
    return M[ligne][colonne] == symbole_vide


def modifier_symbole(M, ligne, colonne, symbole):
    """
    Remplace le symbole de la ligne `ligne` et de la colonne `colonne` par le symbole donné en paramètre.
    """
    M[ligne][colonne] = symbole


def creer_grille_vide():
    """
    Renvoie une grille de tic tac toe vide.
    """
    return [
        [symbole_vide, symbole_vide, symbole_vide],
        [symbole_vide, symbole_vide, symbole_vide],
        [symbole_vide, symbole_vide, symbole_vide]
    ]


def sauvegarder_partie(type_partie, M, tour_a):
    """
    Sauvegarde le plateau, le type de partie et la personne qui doit jouer dans le fichier de sauvegarde.
    Il écrase alors l'ancienne sauvegarde.
    """
    donnees = f"{type_partie};{tour_a}"
    for i in range(3):
        for j in range(3):
            valeur = M[i][j]
            if valeur == symbole_vide:
                index = 0
            elif valeur == symbole1:
                index = 1
            else:
                index = 2

            donnees += f";{index}"

    sauvegarder_fichier(fichier_sauvegarde, donnees)


def charger_partie():
    """
    Charge le plateau, le type de partie et la personne qui doit jouer à partir du fichier de sauvegarde.
    """
    donnees = lire_fichier(fichier_sauvegarde).split(";")
    if len(donnees) != 11:
        return None, None, None

    type_partie = int(donnees[0])
    tour_a = int(donnees[1])
    M = creer_grille_vide()

    for i in range(3):
        for j in range(3):
            index = int(donnees[2 + 3 * i + j])

            if index == 0:
                symbole = symbole_vide
            elif index == 1:
                symbole = symbole1
            else:
                symbole = symbole2

            M[i][j] = symbole

    return type_partie, M, tour_a


def sauvegarder_fichier(fichier, contenu):
    """
    Sauvegarde le contenu en paramètre dans le fichier.
    """
    f = open(fichier, "w")
    f.write(contenu)
    f.close()


def lire_fichier(fichier):
    """
    Lit le contenu du fichier.
    """
    try:
        f = open(fichier, "r")
        donnees = f.read()
        f.close()
        return donnees
    except:
        return ""


# Ici :
# " " pour une case vide
# "o" pour le premier joueur
# "x" pour le second joueur/ordinateur
symbole_vide = " "
symbole1 = "o"
symbole2 = "x"

# Constantes pour le système de sauvegarde.
partie_seul_type = 0
partie_deux_joueur_type = 1
fichier_sauvegarde = "sauvegarde.txt"

lancement()
