# Auteurs: À compléter

from piece import Piece
from position import Position


class Damier:
    """Plateau de jeu d'un jeu de dames. Contient un ensemble de pièces positionnées à une certaine position
    sur le plateau.

    Attributes:
        cases (dict): Dictionnaire dont une clé représente une Position, et une valeur correspond à la Piece
            positionnée à cet endroit sur le plateau. Notez bien qu'une case vide (sans pièce blanche ou noire)
            correspond à l'absence de clé la position de cette case dans le dictionnaire.

        n_lignes (int): Le nombre de lignes du plateau. La valeur est 8 (constante).
        n_colonnes (int): Le nombre de colonnes du plateau. La valeur est 8 (constante).

    """

    def __init__(self):
        """Constructeur du Damier. Initialise un damier initial de 8 lignes par 8 colonnes.

        """
        self.n_lignes = 8
        self.n_colonnes = 8

        self.cases = {
            Position(7, 0): Piece("blanc", "pion"),
            Position(7, 2): Piece("blanc", "pion"),
            Position(7, 4): Piece("blanc", "pion"),
            Position(7, 6): Piece("blanc", "pion"),
            Position(6, 1): Piece("blanc", "pion"),
            Position(6, 3): Piece("blanc", "pion"),
            Position(6, 5): Piece("blanc", "pion"),
            Position(6, 7): Piece("blanc", "pion"),
            Position(5, 0): Piece("blanc", "pion"),
            Position(5, 2): Piece("blanc", "pion"),
            Position(5, 4): Piece("blanc", "pion"),
            Position(5, 6): Piece("blanc", "pion"),
            Position(2, 1): Piece("noir", "pion"),
            Position(2, 3): Piece("noir", "pion"),
            Position(2, 5): Piece("noir", "pion"),
            Position(2, 7): Piece("noir", "pion"),
            Position(1, 0): Piece("noir", "pion"),
            Position(1, 2): Piece("noir", "pion"),
            Position(1, 4): Piece("noir", "pion"),
            Position(1, 6): Piece("noir", "pion"),
            Position(0, 1): Piece("noir", "pion"),
            Position(0, 3): Piece("noir", "pion"),
            Position(0, 5): Piece("noir", "pion"),
            Position(0, 7): Piece("noir", "pion"),
        }

    def recuperer_piece_a_position(self, position):
        """Récupère une pièce dans le damier à partir d'une position.

        Args:
            position (Position): La position où récupérer la pièce.

        Returns:
            La pièce (de type Piece) à la position reçue en argument, ou None si aucune pièce n'était à cette position.

        """
        if position not in self.cases:
            return None

        return self.cases[position]

    def position_est_dans_damier(self, position):
        """Vérifie si les coordonnées d'une position sont dans les bornes du damier (entre 0 inclusivement et le nombre
        de lignes/colonnes, exclusement.

        Args:
            position (Position): La position à valider.

        Returns:
            bool: True si la position est dans les bornes, False autrement.

        """
        if 0 <= position.ligne <= 7 and 0 <= position.colonne <= 7 :
            return True
        else:
            return False

    def piece_peut_se_deplacer_vers(self, position_piece, position_cible):
        """Cette méthode détermine si une pièce (à la position reçue) peut se déplacer à une certaine position cible.
        On parle ici d'un déplacement standard (et non une prise).

        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).

        Une pièce de type pion ne peut qu'avancer en diagonale (vers le haut pour une pièce blanche, vers le bas pour
        une pièce noire). Une pièce de type dame peut avancer sur n'importe quelle diagonale, peu importe sa couleur.
        Une pièce ne peut pas se déplacer sur une case déjà occupée par une autre pièce. Une pièce ne peut pas se
        déplacer à l'extérieur du damier.

        Args:
            position_piece (Position): La position de la pièce source du déplacement.
            position_cible (Position): La position cible du déplacement.

        Returns:
            bool: True si la pièce peut se déplacer à la position cible, False autrement.

        """
        # TODO: À compléter

        if not self.position_est_dans_damier(position_cible):
            return False

        elif position_cible in self.cases:
            return False

        elif position_piece not in self.cases:
            return False

        elif self.cases[position_piece].type_de_piece == "pion":
            if self.cases[position_piece].est_blanche():
                if position_cible not in position_piece.positions_diagonales_haut():
                    return False

            if self.cases[position_piece].est_noire():
                if position_cible not in position_piece.positions_diagonales_bas():
                    return False

        else:
            self.cases[position_cible].est_dame()
            if position_cible not in position_piece.quatre_positions_diagonales():
                return False

        return True

    def piece_peut_sauter_vers(self, position_piece, position_cible):
        """Cette méthode détermine si une pièce (à la position reçue) peut sauter vers une certaine position cible.
        On parle ici d'un déplacement qui "mange" une pièce adverse.

        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).

        Une pièce ne peut que sauter de deux cases en diagonale. N'importe quel type de pièce (pion ou dame) peut sauter
        vers l'avant ou vers l'arrière. Une pièce ne peut pas sauter vers une case qui est déjà occupée par une autre
        pièce. Une pièce ne peut faire un saut que si elle saute par dessus une pièce de couleur adverse.

        Args:
            position_piece (Position): La position de la pièce source du saut.
            position_cible (Position): La position cible du saut.

        Returns:
            bool: True si la pièce peut sauter vers la position cible, False autrement.

        """
        # TODO: À compléter

        if not self.position_est_dans_damier(position_cible):
            return False

        if position_cible in self.cases:
            return False

        elif position_piece not in self.cases:
            return False

        if position_cible not in position_piece.quatre_positions_sauts():
            return False

        ligne = (position_cible.ligne - position_piece.ligne) / 2
        colonne = (position_cible.colonne - position_piece.colonne) / 2

        ligne += position_piece.ligne
        colonne += position_piece.colonne

        position = Position(ligne, colonne)

        if position in self.cases:
            if self.cases[position_piece].couleur == self.cases[position].couleur:

                return False
        return True


    def piece_peut_se_deplacer(self, position_piece):
        """Vérifie si une pièce à une certaine position a la possibilité de se déplacer (sans faire de saut).

        ATTENTION: N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
        les positions des quatre déplacements possibles.

        Args:
            position_piece (Position): La position source.

        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut se déplacer, False autrement.

        """
        # TODO: À compléter

        if position_piece in self.cases:
            if self.cases[position_piece].type_de_piece == "dame":
                position_d = position_piece.quatre_positions_diagonales()
                for i in range(len(position_d)):
                    if self.position_est_dans_damier(position_d[i]):
                        if self.piece_peut_se_deplacer_vers(position_piece, position_d[i]):
                            return True

            if self.cases[position_piece].type_de_piece == "pion":
                if self.cases[position_piece].couleur == "blanc":
                    position_b = position_piece.positions_diagonales_haut()
                    for j in range(len(position_b)):
                        if self.position_est_dans_damier(position_b[j]):
                            if self.piece_peut_se_deplacer_vers(position_piece, position_b[j]):
                                return True

                if self.cases[position_piece].couleur == "noir":
                    position_n = position_piece.positions_diagonales_bas()
                    for k in range(len(position_n)):
                        if self.position_est_dans_damier(position_n[k]):
                            if self.piece_peut_se_deplacer_vers(position_piece, position_n[k]):
                                return True

        return False

    def piece_peut_faire_une_prise(self, position_piece):
        """Vérifie si une pièce à une certaine position a la possibilité de faire une prise.

        Warning:
            N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
            les positions des quatre sauts possibles.

        Args:
            position_piece (Position): La position source.

        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut faire une prise. False autrement.

        """
        # TODO: À compléter

        if position_piece in self.cases:
            position = position_piece.quatre_positions_sauts()
            for p in range(len(position)):
                if self.piece_peut_sauter_vers(position_piece, position[p]):
                    return True

        return False

    def piece_de_couleur_peut_se_deplacer(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de se déplacer
        vers une case adjacente (sans saut).

        ATTENTION: Réutilisez les méthodes déjà programmées!

        Args:
            couleur (str): La couleur à vérifier.

        Returns:
            bool: True si une pièce de la couleur reçue peut faire un déplacement standard, False autrement.
        """
        # TODO: À compléter

        for position in self.cases:
            if self.cases[position].couleur == couleur:
                if self.piece_peut_se_deplacer(position):
                    return True

        return False


    def piece_de_couleur_peut_faire_une_prise(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de faire un
        saut, c'est à dire vérifie s'il existe une pièce d'une certaine couleur qui a la possibilité de prendre une
        pièce adverse.

        ATTENTION: Réutilisez les méthodes déjà programmées!

        Args:
            couleur (str): La couleur à vérifier.

        Returns:
            bool: True si une pièce de la couleur reçue peut faire un saut (une prise), False autrement.
        """
        # TODO: À compléter

        for position in self.cases:
            if self.cases[position].couleur == couleur:
                if self.piece_peut_faire_une_prise(position):
                    return True

        return False

    def deplacer(self, position_source, position_cible):
        """
        Effectue le déplacement sur le damier. Si le déplacement est valide, on doit mettre à jour le dictionnaire
        self.cases, en déplaçant la pièce à sa nouvelle position (et possiblement en supprimant une pièce adverse qui a
        été prise).
        Cette méthode doit également:
        - Promouvoir un pion en dame si celui-ci atteint l'autre extrémité du plateau.
        - Retourner un message indiquant "ok", "prise" ou "erreur".
        ATTENTION: Si le déplacement est effectué, cette méthode doit retourner "ok" si aucune prise n'a été faite,
            et "prise" si une pièce a été prise.
        ATTENTION: Ne dupliquez pas de code! Vous avez déjà programmé (ou allez programmer) des méthodes permettant
            de valider si une pièce peut se déplacer vers un certain endroit ou non.
        """
        # TODO: À compléter

        if self.piece_peut_se_deplacer_vers(position_source, position_cible):
            self.cases[position_cible] = Piece(self.cases[position_source].couleur, self.cases[position_source].type_de_piece)
            self.cases.pop(position_source)
            if position_cible.ligne == 0 or position_cible.ligne == 7:
                self.cases[position_cible].type_de_piece = "dame"
            return "ok"

        if self.piece_peut_sauter_vers(position_source, position_cible):
            self.cases[position_cible] = Piece(self.cases[position_source].couleur, self.cases[position_source].type_de_piece)
            self.cases.pop(position_source)
            l = (position_cible.ligne - position_source.ligne) / 2
            c = (position_cible.colonne - position_source.colonne) / 2
            l += position_source.ligne
            c += position_source.colonne
            vlc = Position(l, c)
            self.cases.pop(vlc)
            if position_cible.ligne == 0 or position_cible.ligne == 7:
                self.cases[position_cible].type_de_piece = "dame"
            return "prise"

        else:
            return "erreur"


    def __repr__(self):
        """Cette méthode spéciale permet de modifier le comportement d'une instance de la classe Damier pour
        l'affichage. Faire un print(un_damier) affichera le damier à l'écran.

        """
        s = " +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
        for i in range(0, 8):
            s += str(i) + "| "
            for j in range(0, 8):
                if Position(i, j) in self.cases:
                    s += str(self.cases[Position(i, j)]) + " | "
                else:
                    s += "  | "
            s += "\n +---+---+---+---+---+---+---+---+\n"

        return s


if __name__ == "__main__":
    print('Test unitaires de la classe "Damier"...')

    un_damier = Damier()

    # TODO: À compléter
    assert un_damier.recuperer_piece_a_position(Position(6, 1)).couleur == "blanc"
    assert un_damier.recuperer_piece_a_position(Position(4, 3)) is None

    assert un_damier.position_est_dans_damier(Position(4, 4)) is True
    assert un_damier.position_est_dans_damier(Position(-1, 5)) is False

    assert un_damier.piece_peut_se_deplacer_vers(Position(5, 0), Position(4, 1)) is True
    assert un_damier.piece_peut_se_deplacer_vers(Position(6, 1), Position(7, 0)) is False
    assert un_damier.piece_peut_sauter_vers(Position(5, 0), Position(3, 2)) == True
    assert un_damier.piece_peut_sauter_vers(Position(7, 0), Position(6, 1)) == False

    assert un_damier.piece_peut_faire_une_prise(Position(5, 0)) is True

    # assert un_damier.deplacer(Position(5, 0), Position(3, 2)) == "prise"
    # assert un_damier.deplacer(Position(4, 1), Position(3, 2)) == "ok"

    un_damier.cases = {Position(0, 0): Piece("blanc", "pion")}
    un_damier.deplacer(Position(0, 0), Position(7, 7))
    # assert un_damier.cases[Position(7, 7)].type_de_piece == "dame"
    print('Test unitaires passés avec succès!')


    print(un_damier)

    # NOTEZ BIEN: Pour vous aider lors du développement, affichez le damier!