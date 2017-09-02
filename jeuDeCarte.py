"""
Fichier principal du jeu

Contenu: jeuDeCarte.py, constantes.py, classes_jeu.py, classes_cartes.py, fonctions.py
"""

import pygame, sys
import # autres library

from pygame.locals import *
from constantes import *
from classes_jeu import *
from classes_cartes import *
from fonctions import *

pygame.init()

# Declarations des variables necessaire


# GAME LOOP
while True:
    # INPUT
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # UPDATE


    # DISPLAY
    pygame.display.flip() # met a jour l'image
