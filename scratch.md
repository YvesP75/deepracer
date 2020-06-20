**en vrac**

Objet track
- attributs
    - tableau de nb complexes donnant le centre de la piste
    - Largeur de la piste
    - fonction polynomiale d'extrapolation (en chaque point? qui prend les 2 ou 3 précédents et suivants?)
- fonction
    - distance_au_point
    - distance à la courbe
    - courbure (fontion continue)
    - détermine les coefficients de la fonction d'interpolation en fonction du d°

- questions :
    - comment sont espacés les points?
    - est-ce qu'on met une fonction d'interpolation?
    - est-ce qu'on donne la courbure au point?


Objet voiture
- attributs
    - action space vitesses/angles
    - objet courbe d'accélération
    (tableau donnant le temps pour gagner 0,1m/s)
    - objet courbe de décélération
    (tableau donnant le temps pour baisser de 0,1m/s)
    - objet adherence
    vitesse max en fonction de la courbure et de l'accélération


Objet trajectoire-point
- liste de points (complexes)
- liste
- fonctions
    - distance par rapport aux points d'une racetrack
    - distance par rapport à la courbe d'une racetrack
    - minimum/maximum à gauche/dr par rapport à une racetrack



Objet trajectoire-segment
- liste de segments
-

Objet politique

Objet segment-catalogue
- attributs immuables (inputs)
    - angle des roues
    - 
- attributs immuables (déduits)
     - vitesse max (en fonction de la courbure)
- fonction
    - voiture, vitesse origine => vitesse sortie
    -                          => adhérence
     
Objet segment-trajectoire
- hérite d'objet-catalogue   
- autres attributs
    - start : boolean
    - index 
    - trajectory
    - vitesse théorique max dans une trajectoire
    - on-track : boolean
    


Objet trajectoire-segment
- liste de segments trajectoires
- commentaire :
    - la longueur de la liste donne la taille
   

Objet segment
- attributs
    - position origine
    - position fin
    - vitesse théorique origine
    - axe des roues
    - courbure
    - vitesse origine
- fonctions
    - vitesse max (car)
    - accélération max (car, vitesse_origine)
    - décélération max (car, vitesse_origine)
    


Main
- fonction
    - arg
        - track
        - car
    - returns list
        - positions
        
        
        
 Idées : exploiter les logs pour :
 - apprendre sur la voiture
 - apprendre sur le trackrace (affiner le modèle depuis les trackpoints)
 


Dans un premier temps, on met seulement bout à bout des segments parmi une vingtaine caractérisés par vitesse, un angle
leur longueur est déterminée par la vitesse puisque l'intervalle de temps est fixe. (ex. 500 ms)



Simplification :
- l'adhérence en première approximation ne dépend pas de l'accélération, ni décé
- l'accélération : en 1 IT, la vitesse croit d'un coeff * delta(Vmax-V)
- la décélération : en 1 IT, la vitesse décroit d'un coeff * V et au min de Vmax/coeef2

Ordre de grandeur :
piste = 100 m
vmax = 4 m/s
IT = 0,5 s
adhérence telle que 30° + 1 m/s = ok
angle max = 30°
nb types de segments = 20



Algorithme

// 
création de la track
= la fonction (z => ontrack?)
simplification = distance au segment formé par les deux points les plus proches
ou x = a cos theta * (1 + 0.2 cos theta/2)
et y = b sin theta * (1 + 0.2 cos theta/3)
intérieur = coeff_int <1
ext = coeff_ext >1

//algo génétique

population = 23 traj de 20 segments viables et on voit qui va le plus loin

loi de croisement :
traj1 ++ traj2 => traj12 et traj21 coupées aléatoirement
traj1 et traj2 choisis en fonction de leur vitalité (d-dmin)

loi de mort :
la vitalité = longueur. 
probablité de mort  (dmax-d)/(dmax-dmin)

loi de 
changement d'un segment (avec proba de proximité de segment)

//gradient sur les paramètres des segments 


###### idées du samedi

itérer sur le nb d'actions :
- commencer par 4 puis atteindre un consensus et puis ajouter des actions
- doper les nouvelles générations : les saturer systématiquement (en ne les tuant pas)
- faire une indirection sur les actions, de manière  à pouvoir changer le z point tout en modifiant l'action
- faire entrer en contact la consigne et la vitesse
- faire tourner sans contrainte du champ des actions, puis resserer les actions (optim génétique?)
