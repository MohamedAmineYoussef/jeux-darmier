# Auteurs: À compléter

from tkinter import Tk, Label, NSEW
from canvas_damier import CanvasDamier
from partie import Partie
from position import Position


class FenetrePartie(Tk):
    """Interface graphique de la partie de dames.

    Attributes:
        partie (Partie): Le gestionnaire de la partie de dame
        canvas_damier (CanvasDamier): Le «widget» gérant l'affichage du damier à l'écran
        messages (Label): Un «widget» affichant des messages textes à l'utilisateur du programme

        TODO: AJOUTER VOS PROPRES ATTRIBUTS ICI!

    """

    def __init__(self):
        """Constructeur de la classe FenetrePartie. On initialise une partie en utilisant la classe Partie du TP3 et
        on dispose les «widgets» dans la fenêtre.
        """

        # Appel du constructeur de la classe de base (Tk)
        super().__init__()

        # La partie
        self.partie = Partie()

        # Création du canvas damier.
        self.canvas_damier = CanvasDamier(self, self.partie.damier, 60)
        self.canvas_damier.grid(sticky=NSEW)
        self.canvas_damier.bind('<Button-1>', self.selectionner)

        # Ajout d'une étiquette d'information.
        self.messages = Label(self)
        self.messages.grid()

        # Nom de la fenêtre («title» est une méthode de la classe de base «Tk»)
        self.title("Jeu de dames")

        # Truc pour le redimensionnement automatique des éléments de la fenêtre.
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)



    def selectionner(self, event):
        """Méthode qui gère le clic de souris sur le damier.

        Args:
            event (tkinter.Event): Objet décrivant l'évènement qui a causé l'appel de la méthode.

        """

        ligne = event.y // self.canvas_damier.n_pixels_par_case
        colonne = event.x // self.canvas_damier.n_pixels_par_case
        position = Position(ligne, colonne)

        if self.partie.position_source_selectionnee is None:
            piece = self.partie.damier.recuperer_piece_a_position(position)

            if piece is None:
                self.messages['foreground'] = 'red'
                self.messages['text'] = 'Erreur: Aucune pièce à cet endroit.'
            elif piece.couleur != self.partie.couleur_joueur_courant:
                self.messages['foreground'] = 'red'
                self.messages['text'] = "Erreur: Ce n'est pas votre pièce."
            else:
                self.messages['foreground'] = 'black'
                self.messages['text'] = 'Pièce sélectionnée à la position {}.'.format(position)
                self.partie.position_source_selectionnee = position
        else:
            pos_source = self.partie.position_source_selectionnee
            pos_cible = position
            move_valid, move_message = self.partie.position_cible_valide(pos_cible)

            if move_valid:
                self.partie.damier.deplacer(pos_source, pos_cible)
                self.messages['foreground'] = 'black'
                self.messages['text'] = 'Pièce déplacée de {} à {}.'.format(pos_source, pos_cible)
                self.partie.position_source_selectionnee = None
                self.canvas_damier.actualiser()

                self.partie.couleur_joueur_courant = "blanc" if self.partie.couleur_joueur_courant == "noir" else "noir"
            else:
                self.messages['foreground'] = 'red'
                self.messages['text'] = move_message
                self.partie.position_source_selectionnee = None