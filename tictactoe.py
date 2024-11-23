def afficher_jeu(M):
    """
    Affiche le plateau avec le numéro des lignes/colonnes.
    """
    print("   1 2 3   1 2 3   1 2 3 \n"
          f"1: {M[0][0][0]} {M[0][0][1]} {M[0][0][2]} | {M[1][0][0]} {M[1][0][1]} {M[1][0][2]} | {M[2][0][0]} {M[2][0][1]} {M[2][0][2]}\n"
          f"2: {M[0][1][0]} {M[0][1][1]} {M[0][1][2]} | {M[1][1][0]} {M[1][1][1]} {M[1][1][2]} | {M[2][1][0]} {M[2][1][1]} {M[2][1][2]}\n"
          f"3: {M[0][2][0]} {M[0][2][1]} {M[0][2][2]} | {M[1][2][0]} {M[1][2][1]} {M[1][2][2]} | {M[2][2][0]} {M[2][2][1]} {M[2][2][2]}\n"
          f"   ---------------------\n"
          f"1: {M[3][0][0]} {M[3][0][1]} {M[3][0][2]} | {M[4][0][0]} {M[4][0][1]} {M[4][0][2]} | {M[5][0][0]} {M[5][0][1]} {M[5][0][2]}\n"
          f"2: {M[3][1][0]} {M[3][1][1]} {M[3][1][2]} | {M[4][1][0]} {M[4][1][1]} {M[4][1][2]} | {M[5][1][0]} {M[5][1][1]} {M[5][1][2]}\n"
          f"3: {M[3][2][0]} {M[3][2][1]} {M[3][2][2]} | {M[4][2][0]} {M[4][2][1]} {M[4][2][2]} | {M[5][2][0]} {M[5][2][1]} {M[5][2][2]}\n"
          f"   ---------------------\n"
          f"1: {M[6][0][0]} {M[6][0][1]} {M[6][0][2]} | {M[7][0][0]} {M[7][0][1]} {M[7][0][2]} | {M[8][0][0]} {M[8][0][1]} {M[8][0][2]}\n"
          f"2: {M[6][1][0]} {M[6][1][1]} {M[6][1][2]} | {M[7][1][0]} {M[7][1][1]} {M[7][1][2]} | {M[8][1][0]} {M[8][1][1]} {M[8][1][2]}\n"
          f"3: {M[6][2][0]} {M[6][2][1]} {M[6][2][2]} | {M[7][2][0]} {M[7][2][1]} {M[7][2][2]} | {M[8][2][0]} {M[8][2][1]} {M[8][2][2]}\n")


def afficher_regles():
    print("Le but du jeu est d’aligner avant son adversaire 3 symboles "
          "identiques horizontalement, verticalement ou en diagonale.\n"
          "Chaque joueur a donc son propre symbole, généralement une"
          "croix pour l’un et un rond pour l’autre.\n"
          "Une fois qu'un joueur a fini de jouer c'est à l'autre jusqu'à"
          " la fin de la partie.\n")


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
    # Tant qu'aucun choix valide n'a été fait.
    while not termine:
        n = int(input("Entrez un nombre pour commencer la partie:\n"
                      "- 1: pour jouer contre l'ordinateur\n"
                      "- 2: pour jouer avec un autre joueur\n"
                      "- 3: pour charger la dernière partie sauvegardée\n"))

        M = creer_grille_vide()
        # Jouer seul
        if n == 1:
            jouer_seul(M, choisir_regles())
            termine = True
        # Jouer à deux
        elif n == 2:
            jouer_a_deux(M, choisir_regles())
            termine = True
        # Charger une partie
        elif n == 3:
            type_partie, mode_regles, M, tour_a, grille_a_jouer = charger_partie()
            # Partie contre l'ordinateur
            if type_partie == partie_seul_type:
                jouer_seul(M, mode_regles, tour_a, grille_a_jouer)
                termine = True
            # Partie à deux
            elif type_partie == partie_deux_joueur_type:
                jouer_a_deux(M, mode_regles, tour_a, grille_a_jouer)
                termine = True
            else:
                print(f"Une erreur c'est produite durant le chargement de la partie")
        else:
            print(f"Aucun choix n'est associé au nombre {n}.")


def choisir_regles():
    """
    Demande à l'utilisateur de choisir les règles avec lesquelles il souhaite jouer.
    - 0 : le joueur choisit la grille dans laquelle il veut jouer à chaque tour
    - 1 : le joueur doit jouer dans une grille en fonction de la case dans laquelle a joué l'adversaire
    - 2 : aucun joueur ne peut changer de grille dans que celle qui a été commencée n'a pas été terminée
    """
    print(
        ""
        "Voici les règles disponible pour ce jeu:"
        "0 : Le joueur choisit la grille dans laquelle il veut jouer à chaque tour"
        "1 : Le joueur doit jouer dans une grille en fonction de la case dans laquelle a joué l'adversaire"
        "2 : Aucun joueur ne peut changer de grille dans que celle qui a été commencée n'a pas été terminée"
        ""
    )

    mode_regles = -1
    while not (0 <= mode_regles <= 2):
        mode_regles = int(input("Veuillez choisir les règles du jeux: "))

    return mode_regles


def jouer_seul(M, mode_regles, tour_a=1, grille_a_jouer=9):
    """
    Boucle de jeu pour jouer avec l'ordinateur.
    """
    gagnant = -1
    while gagnant == -1:
        # Affichage de début de tour
        afficher_jeu(M)
        symbole = symbole1 if tour_a == 1 else symbole2

        # Si le joueur doit jouer, sinon l'ordinateur doit jouer
        if tour_a == 1:
            # Affichage de début de tour
            print(f"C'est à vous de jouer avec les \"{symbole}\".")

            # Choix de la grille si besoin
            if mode_regles == 0 or grille_a_jouer == 9 or grille_finie(M, grille_a_jouer):
                grille_a_jouer = demander_grille(M)
                if grille_a_jouer is None:
                    sauvegarder_partie(partie_deux_joueur_type, mode_regles, M, tour_a, 9)
                    return
            print(f"Vous jouez dans la grille numéro {grille_a_jouer + 1}.")

            # Choix de la position dans la grille
            ligne, colonne = demander_position(M, grille_a_jouer)
            if ligne is colonne is None:
                sauvegarder_partie(partie_seul_type, mode_regles, M, tour_a, grille_a_jouer)
                return
        else:
            # Affichage de début de tour
            print(f"C'est à l'ordinateur de jouer avec les \"{symbole}\".")

            # Choix de la grille si besoin
            if mode_regles == 0 or grille_a_jouer == 9 or grille_finie(M, grille_a_jouer):
                grille_a_jouer = deviner_grille(M)
            print(f"Il joue dans la grille numéro {grille_a_jouer + 1}.")

            # Choix de la position dans la grille
            ligne, colonne = deviner_position(M, grille_a_jouer)

        # Actions de fin de tour : placement de symbole, changement de tour, changement de grille si besoin et
        # vérification de la présence d'un gagnant
        modifier_symbole(M, grille_a_jouer, ligne, colonne, symbole)
        if mode_regles == 1:
            grille_a_jouer = ligne * 3 + colonne
        gagnant = partie_finie(M)
        tour_a = 1 if tour_a == 0 else 0  # ou tour_a = 1 - tour_a

    # La partie est gagné, affichage de fin
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


def jouer_a_deux(M, mode_regles, tour_a=1, grille_a_jouer=9):
    """
    Boucle de jeu pour jouer à deux joueurs.
    """
    gagnant = -1

    while gagnant == -1:
        # Affichage de début de tour
        afficher_jeu(M)
        symbole = symbole1 if tour_a == 1 else symbole2
        print(f"C'est au joueur numéro {tour_a} de jouer avec les \"{symbole}\".")

        # Choix de la grille si besoin
        if mode_regles == 0 or grille_a_jouer == 9 or grille_finie(M, grille_a_jouer):
            grille_a_jouer = demander_grille(M)
            if grille_a_jouer is None:
                sauvegarder_partie(partie_deux_joueur_type, mode_regles, M, tour_a, 9)
                return
        print(f"Vous jouez dans la grille numéro {grille_a_jouer + 1}.")

        # Choix de la position dans la grille
        ligne, colonne = demander_position(M, grille_a_jouer)
        if ligne is colonne is None:
            sauvegarder_partie(partie_deux_joueur_type, mode_regles, M, tour_a, grille_a_jouer)
            return

        # Actions de fin de tour : placement de symbole, changement de tour, changement de grille si besoin et
        # vérification de la présence d'un gagnant
        modifier_symbole(M, grille_a_jouer, ligne, colonne, symbole)
        if mode_regles == 1:
            grille_a_jouer = ligne * 3 + colonne
        gagnant = partie_finie(M)
        tour_a = 1 if tour_a == 0 else 0  # ou tour_a = 1 - tour_a

    # La partie est gagné, affichage de fin
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
    if jeu_plein(M):
        return 0

    if symbole_gagne(M, symbole1):
        return 1

    if symbole_gagne(M, symbole2):
        return 2

    return -1

def grille_finie(M, grille):
    """
    Renvoie si la grille est terminée.
    C'est à dire, si la grille est pleine ou déjà remportée par un joueur.
    """
    return grille_pleine(M, grille) or symbole_gagne_grille(M, grille, symbole1) or symbole_gagne_grille(M, grille, symbole2)

def jeu_plein(M):
    """
    Renvoie si le jeu est "plein".
    Il est considéré comme plein si toutes les grilles sont terminées (!= pleines)
    """
    for i in range(9):
        if not grille_finie(M, i):
            return False

    return True

def grille_pleine(M, grille):
    """
    Renvoie si la grille est pleine.
    """
    for i in range(3):
        for j in range(3):
            if M[grille][i][j] == symbole_vide:
                return False

    return True

def symbole_gagne(M, symbole):
    """
    Renvoie si le symbole `symbole` à gagner, c'est-à-dire, s'il y a une colonne/ligne/diagonale de grilles gagnées par le symbole.
    """
    diagonale1_complete = True
    diagonale2_complete = True
    for i in range(3):
        ligne_complete = True
        colonne_complete = True

        # Vérification des diagonales de grille
        if not symbole_gagne_grille(M, i * 3 + i, symbole):
            diagonale1_complete = False
        if not symbole_gagne_grille(M, (2 - i) * 3 + i, symbole):
            diagonale2_complete = False

        # Vérification des lignes/colonnes de grille en même temps
        for j in range(3):
            if not symbole_gagne_grille(M, i * 3 + j, symbole):
                ligne_complete = False
            if not symbole_gagne_grille(M, j * 3 + i, symbole):
                colonne_complete = False

        if ligne_complete or colonne_complete:
            return True

    return diagonale1_complete or diagonale2_complete

def symbole_gagne_grille(M, grille, symbole):
    """
    Renvoie si le symbole `symbole` à gagner la grille, c'est-à-dire, s'il y a une colonne/ligne/diagonale du symbole.
    """
    diagonale1_complete = True
    diagonale2_complete = True
    for i in range(3):
        ligne_complete = True
        colonne_complete = True

        # Vérification des diagonales
        if M[grille][i][i] != symbole:
            diagonale1_complete = False
        if M[grille][2 - i][i] != symbole:
            diagonale2_complete = False

        # Vérification des lignes/colonnes en même temps
        for j in range(3):
            if M[grille][i][j] != symbole:
                ligne_complete = False
            if M[grille][j][i] != symbole:
                colonne_complete = False

        if ligne_complete or colonne_complete:
            return True

    return diagonale1_complete or diagonale2_complete


def deviner_grille(M) -> int:
    """
    L'ordinateur renvoie la grille dans laquelle il souhaite jouer.
    TODO
    """
    pass


def deviner_position(M, grille) -> [int, int]:
    """
    L'ordinateur renvoie la position (ligne/colonne) à laquelle il souhaite jouer dans la `grille`.
    TODO
    """
    pass


def demander_grille(M):
    """
    Demande au joueur la grille dans laquelle il souhaite jouer.
    NB : renvoie None si le joueur souhaite sauvegarder et arrêter la partie.
    """
    grille = -1
    valide = False

    # Tant que la grille n'est pas valide
    while not (0 <= grille < 9 and valide):
        grille = int(input("Veuillez entrer le numéro de la grille dans laquelle vous souhaitez jouer (ou 0 pour "
                           "enregistrer): ")) - 1
        if grille == -1:
            return None

        valide = not grille_finie(M, grille)
        # Si la grille est déjà terminée
        if not valide:
            print("Cette grille est déjà terminée.")

    return grille

def demander_position(M, grille):
    """
    Demande une position (ligne/colonne) au joueur pour y placer son symbole.
    NB : renvoie (None, None) si le joueur souhaite sauvegarder et arrêter la partie.
    """
    ligne = -1
    colonne = -1
    valide = False

    # Tant que l'emplacement n'est pas valide
    while not (0 <= ligne < 3 and 0 <= colonne < 3 and valide):
        ligne = int(input(
            "Veuillez entrer le numéro de la ligne à laquelle vous souhaitez jouer (ou 0 pour enregistrer): ")) - 1
        if ligne == -1:
            return None, None

        colonne = int(input(
            "Veuillez entrer le numéro de la colonne à laquelle vous souhaitez jouer (ou 0 pour enregistrer): ")) - 1
        if colonne == -1:
            return None, None

        valide = secure_est_vide(M, grille, ligne, colonne)
        # Si ligne et colonne sont valide et que la case n'est pas vide
        if not valide:
            print(f"Un symbole est déjà placé à la ligne {ligne + 1} et colonne {colonne + 1}.")

    return ligne, colonne


def secure_est_vide(M, grille, ligne, colonne):
    """
    Renvoie True si l'emplacement `ligne` et `colonne` de la `grille` est invalide.
    Renvoie si l'emplacement à la `ligne` et à la `colonne` de la `grille` est vide sinon.
    """
    if not (0 <= ligne < 3 and 0 <= colonne < 3):
        return True

    return est_vide(M, grille, ligne, colonne)


def est_vide(M, grille, ligne, colonne):
    """
    Renvoie si l'emplacement à la `ligne` et à la `colonne` de la `grille` est vide.
    """
    return M[grille][ligne][colonne] == symbole_vide


def modifier_symbole(M, grille, ligne, colonne, symbole):
    """
    Remplace le symbole à la `ligne` et à la `colonne` de la `grille` par le symbole donné en paramètre.
    """
    M[grille][ligne][colonne] = symbole


def creer_grille_vide():
    """
    Renvoie une grille de tic tac toe vide.
    """
    return [
        [
        [symbole_vide, symbole_vide, symbole_vide],
        [symbole_vide, symbole_vide, symbole_vide],
        [symbole_vide, symbole_vide, symbole_vide]
    ] for _ in range(9)]


def sauvegarder_partie(type_partie, mode_regles, M, tour_a, grille_a_jouer):
    """
    Sauvegarde le plateau, le type de partie et la personne qui doit jouer dans le fichier de sauvegarde.
    Il écrase alors l'ancienne sauvegarde.
    """
    donnees = f"{type_partie}{tour_a}{grille_a_jouer}{mode_regles}"
    # Sauvegarde des grilles
    for g in range(9):
        for i in range(3):
            for j in range(3):
                valeur = M[g][i][j]
                # Convertion du symbole en nombre
                if valeur == symbole_vide:
                    index = 0
                elif valeur == symbole1:
                    index = 1
                else:
                    index = 2

                donnees += f"{index}"

    sauvegarder_fichier(fichier_sauvegarde, donnees)


def charger_partie():
    """
    Charge le plateau, le type de partie et la personne qui doit jouer à partir du fichier de sauvegarde.
    """
    donnees = lire_fichier(fichier_sauvegarde)
    if len(donnees) != 85:
        return None, None, None, None, None

    type_partie = int(donnees[0])
    tour_a = int(donnees[1])
    grille_a_jouer = int(donnees[2])
    mode_regles = int(donnees[3])
    M = creer_grille_vide()

    # Chargement des grilles
    for g in range(9):
        for i in range(3):
            for j in range(3):
                index = int(donnees[4 + 9 * g + 3 * i + j])

                # Convertion du nombre en symbole
                if index == 0:
                    symbole = symbole_vide
                elif index == 1:
                    symbole = symbole1
                else:
                    symbole = symbole2

                M[g][i][j] = symbole

    return type_partie, mode_regles, M, tour_a, grille_a_jouer


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
