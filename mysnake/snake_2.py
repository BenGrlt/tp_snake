"""
v02 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((400, 400))
clock = pg.time.Clock()

nb_tuiles_L, nb_tuiles_l = 30,30
dim_tuiles_L, dim_tuiles_l = 400/nb_tuiles_L,400/nb_tuiles_l

def damier():
    for i in range(nb_tuiles_L):
        for j in range(nb_tuiles_l):
             x, y = dim_tuiles_L*i, dim_tuiles_l*j            # les coordonnées du coin du rectangle (en pixels)

# la taille du rectangle
             width, height = dim_tuiles_L, dim_tuiles_l     # largeur et hauteur du rectangle, toujours en pixels

# on crée un objet 'Rect'
             rect = pg.Rect(x, y, width, height)

# la couleur de remplissage
             a=255*((i+j)%2)
             color = (a, a, a)        
# et on le dessine comme ceci dans l'écran virtuel
             pg.draw.rect(screen, color, rect)
             pg.display.update()


# les coordonnées du corps du serpent
snake =[[10, 15], [11, 15], [12, 15]]
def move(A):
    for i in range(len(A)-1):
         A[i]=A[i+1]
         A[i][0]+=10
         A[-1][0]+=10
    for elt in A:
        x, y = elt[0], elt[1]
        width, height = dim_tuiles_L, dim_tuiles_l 
        rect = pg.Rect(x, y, width, height)
        color = (0,255,0)        
        # et on le dessine comme ceci dans l'écran virtuel
        pg.draw.rect(screen, color, rect)
        pg.display.update()


# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)
    damier()
    move(snake)
    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...
    



# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
