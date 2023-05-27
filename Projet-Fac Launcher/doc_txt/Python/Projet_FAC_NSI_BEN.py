# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:11:32 2022

@author: Matthis
"""

# ================================= MODULES ===================================

from tkinter import *
from playsound import playsound
import time

from random import randint
from random import *

from boutons import *
from score import *
from pile_file import *

# ========================= CRÉATIONS DE LA FENETRE ===========================

MaFenetre=Tk()
MaFenetre.geometry('1920x1080')

# ======================== IMPORTATIONS DES IMAGES ============================

fond_menu=PhotoImage(file="images/images_menu/Menu_tele_no_signal.png")
fond_plato_om=PhotoImage(file="images/images_menu/Menu_tele_operations_manuscrites.png")
fond_jeux_inexistant_1=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_1.png")
fond_jeux_inexistant_2=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_2.png")
fond_jeux_inexistant_3=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_3.png")
fond_jeux_inexistant_4=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_4.png")
fond_jeux_inexistant_5=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_5.png")
fond_jeux_inexistant_6=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_6.png")
fond_jeux_inexistant_7=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_7.png")    
fond_jeux_inexistant_8=PhotoImage(file="images/images_menu/Menu_tele_jeux_inexistant_8.png")
fond_jeux_inexistant_9=PhotoImage(file="images/images_menu/RickAstley.png")

# ===================== IMPORTATIONS DES IMAGES JEUX 1 ========================

#plato

fond_jeux_1=PhotoImage(file="images/image_jeux_1/plato_perso.png")
plato_lettre=PhotoImage(file="images/image_jeux_1/eppreuve_lettre_v1.png")
bravo1=PhotoImage(file="images/image_jeux_1/bravo_lettre.png")

#regles 

regles_questions=PhotoImage(file="images/image_jeux_1/regles_questions.png")
regles=PhotoImage(file="images/image_jeux_1/regles.png")


#random

epreuve_lettre=PhotoImage(file="images/image_jeux_1/epreuve_l.png")
epreuve_ope=PhotoImage(file="images/image_jeux_1/epreuve_o.png")
grise_case=PhotoImage(file="images/image_jeux_1/grise2.png")

#opération
operation_jeux=PhotoImage(file="images/image_jeux_1/operation_jeux.png")

#Attribution des points
vingcinq=PhotoImage(file="images/image_jeux_1/25pts.png")
quinze=PhotoImage(file="images/image_jeux_1/15pts.png")
dix=PhotoImage(file="images/image_jeux_1/10pts.png")
cinqpts=PhotoImage(file="images/image_jeux_1/5pts.png")
unpts=PhotoImage(file="images/image_jeux_1/1pts.png")
zeropts=PhotoImage(file="images/image_jeux_1/0pts.png")
mot_null=PhotoImage(file="images/image_jeux_1/mot_null.png")

#Page final
final=PhotoImage(file="images/image_jeux_1/fin.png")

# ============================== CLASS LETTRES ================================

# Importations Images lettres : 
    
a_image=PhotoImage(file="./images/image_jeux_1/lettres/A.png")
b_image=PhotoImage(file="./images/image_jeux_1/lettres/B.png")
c_image=PhotoImage(file="./images/image_jeux_1/lettres/C.png")
d_image=PhotoImage(file="./images/image_jeux_1/lettres/D.png")
e_image=PhotoImage(file="./images/image_jeux_1/lettres/E.png")
f_image=PhotoImage(file="./images/image_jeux_1/lettres/F.png")
g_image=PhotoImage(file="./images/image_jeux_1/lettres/G.png")
h_image=PhotoImage(file="./images/image_jeux_1/lettres/H.png")
i_image=PhotoImage(file="./images/image_jeux_1/lettres/I.png")
j_image=PhotoImage(file="./images/image_jeux_1/lettres/J.png")
k_image=PhotoImage(file="./images/image_jeux_1/lettres/K.png")
l_image=PhotoImage(file="./images/image_jeux_1/lettres/L.png")
m_image=PhotoImage(file="./images/image_jeux_1/lettres/M.png")
n_image=PhotoImage(file="./images/image_jeux_1/lettres/N.png")
o_image=PhotoImage(file="./images/image_jeux_1/lettres/O.png")
p_image=PhotoImage(file="./images/image_jeux_1/lettres/P.png")
q_image=PhotoImage(file="./images/image_jeux_1/lettres/Q.png")
r_image=PhotoImage(file="./images/image_jeux_1/lettres/R.png")
s_image=PhotoImage(file="./images/image_jeux_1/lettres/S.png")
t_image=PhotoImage(file="./images/image_jeux_1/lettres/T.png")
u_image=PhotoImage(file="./images/image_jeux_1/lettres/U.png")
v_image=PhotoImage(file="./images/image_jeux_1/lettres/V.png")
w_image=PhotoImage(file="./images/image_jeux_1/lettres/W.png")
x_image=PhotoImage(file="./images/image_jeux_1/lettres/X.png")
y_image=PhotoImage(file="./images/image_jeux_1/lettres/Y.png")
z_image=PhotoImage(file="./images/image_jeux_1/lettres/Z.png")

# =============================================================================
# Importation Chiffres
# =============================================================================

# un=PhotoImage(file="images/image_jeux_1/chiffres/1.png")
# deux=PhotoImage(file="images/image_jeux_1/chiffres/2.png")
# trois=PhotoImage(file="images/image_jeux_1/chiffres/3.png")
# quatre=PhotoImage(file="images/image_jeux_1/chiffres/4.png")
# cinq=PhotoImage(file="images/image_jeux_1/chiffres/5.png")
# six=PhotoImage(file="images/image_jeux_1/chiffres/6.png")
# sept=PhotoImage(file="images/image_jeux_1/chiffres/7.png")
# huit=PhotoImage(file="images/image_jeux_1/chiffres/8.png")
# neuf=PhotoImage(file="images/image_jeux_1/chiffres/9.png")

# ============================  Score initialisations =========================

Score = SCORE(0)
Score.ajouter_score()

# ===================================== TEST ==================================

# Définition des labels


# LabelResultat=Label(MaFenetre, textvariable = None , bg ="white",font=("Courier",60),width=3,height=1)

# =============================================================================
# ========================== FONCTIONS DU PROGRAMME ===========================
    
def menu():
    global can1, Bouton1, Bouton2, Bouton3, Bouton4, Bouton5, Bouton6, Bouton7,Bouton8, liste_button, bou1, cand_rep, compteur,Score
    Score = SCORE(0)
    
    can1=Canvas(MaFenetre,width=1920,height=1080)
    can1.place(x=0,y=0)
    
    
    # ====================== CRÉATIONS DES BOUTONS + LISTE ====================
    
    reset_liste(liste_button)
    
    Bouton1 = bouton([1078, 284], [1117, 298], "Bouton1", fond_plato_om, "ecran_1()", None,)
    Bouton2 = bouton([1078, 314], [1117, 324], "Bouton2",fond_jeux_inexistant_2, "ecran_2()", None)
    Bouton3 = bouton([1078, 339], [1117, 350], "Bouton3",fond_jeux_inexistant_3, "ecran_3()", None)
    Bouton4 = bouton([1078, 367], [1117, 379], "Bouton4",fond_jeux_inexistant_4,"ecran_4()", None)
    Bouton5 = bouton([1078, 394], [1117, 406], "Bouton5",fond_jeux_inexistant_5,"ecran_5()", None)
    Bouton6 = bouton([1078, 420], [1117, 432], "Bouton6",fond_jeux_inexistant_6,"ecran_6()", None)
    Bouton7 = bouton([1078, 447], [1117, 461], "Bouton7",fond_jeux_inexistant_7,"ecran_7()", None)
    Bouton8 = bouton([1078, 474], [1777, 489], "Bouton8",fond_jeux_inexistant_8,"ecran_8()", None)
    
    Bouton9 = bouton([1117, 541], [1154, 553], "Bouton9", fond_menu, "menu()", None)
    
    Bouton10 = bouton([1169, 544], [1202, 561],"Bouton10", None, "rick()", None)
    Bouton45=bouton([1298, 772],[1880, 968],"quitter",None,"MaFenetre.destroy()",None)
    
    liste_button=[Bouton1, Bouton2, Bouton3, Bouton4, Bouton5, Bouton6, Bouton7, Bouton8, Bouton9, Bouton10,Bouton45]
    #=================== MISE EN PLACE FOND + REGARD CLIQUE ====================
    
    image_fond=can1.create_image(0,0,image=fond_menu,anchor="nw") #set-up de la premiere iage a afficher
    
    can1.focus_set()
    can1.bind('<ButtonPress-1>', Clique)

def ecran_1():
    '''fonction pour jouer au jeux 1 : Opérations manuscrite'''
    image_fond=can1.create_image(0,0,image=fond_plato_om,anchor="nw")
    
    Bouton11 = bouton([282, 633], [895, 759], "Bouton11", None, "jeux_1_init()", None)
    liste_button.append(Bouton11)
    

# =================================   JEUX 1   ================================

def jeux_1_init():
    '''initialisation du jeux1 -> mise en route (regles)'''
    global Labelscore,liste_button
    reset_liste(liste_button)
    
    can1.after(0,affiche_image(fond_jeux_1))
    can1.update()
    
    score1 = StringVar()
    Labelscore = Label(MaFenetre, textvariable = score1 , bg ="lightblue",font=("Courier",60),width=3,height=1)
    score1.set(Score.get_score())
    Labelscore.place(x=1596,y=45)
    Labelscore.destroy()
    
    # can1.after(1000, playsound('operations_manuscrites.wav'))
    # can1.update()
    
    can1.after(0,affiche_image(regles_questions))
    can1.update()
    
    reset_liste(liste_button)
    
    Bouton_arret=bouton([1541, 51],[1899, 165],"Arreter",None,"fin_du_jeu()",None)
    liste_button.append(Bouton_arret)

    Bouton12 = bouton([582, 750],[922, 918],"Bouton12",None,"jeux_1_regles()",None)
    liste_button.append(Bouton12)  
    
    Bouton13 = bouton([978, 750],[1318, 918],"Bouton13",None,"jeux_1()",None)
    liste_button.append(Bouton13)

def jeux_1_regles():
    global liste_button
    reset_liste(liste_button)
    
    
    '''fonction qui permet d'afficher les règles du jeux 1'''
    
    can1.after(0,affiche_image(regles)) #mise en place de l'image avec les règles
   
    Bouton_arret=bouton([86,780],[440, 888],"Arreter",None,"fin_du_jeu()",None)
    liste_button.append(Bouton_arret)
    #bouton commencer :
    
    Bouton50 = bouton([665, 890], [1250, 1020], 'Bouton50', None, 'jeux_1()', None)
    liste_button.append(Bouton50)

def jeux_1():
    global liste_button,compteur,cand_rep,Labelscore
    reset_liste(liste_button)
    Labelscore.destroy()
    
    Bouton_arret=bouton([1541, 51],[1899, 165],"Arreter",None,"fin_du_jeu()",None)
    liste_button.append(Bouton_arret)
    
    
    
    '''fonction qui choisit aléatoirement entre : jeux opés / jeux lettres'''
    
    a=randint(0,1) # Création d'une variable avec un chiffre aléatoire
    if a == 0 : # si a == 0 -> lettres 
        can1.after(0, jeux_1_lettres())
        can1.update()
    else : #sinon -> opés
        can1.after(0, jeux_1_operations())
        can1.update()

# Partie LETTRES

def jeux_1_lettres():
    '''fonction qui permet de jouer au mini jeux de lettre'''
    global liste_button, l_mot_trouver,liste_button #, lettre0, lettre1, lettre2, lettre3, lettre4, lettre5, lettre6, lettre7, lettre8, lettre9
    
    #on réinitialise la liste_button, pour supprimer tous les précédent boutons
    reset_liste(liste_button)
    Bouton_arret=bouton([1541, 51],[1899, 165],"Arreter",None,"fin_du_jeu()",None)
    liste_button.append(Bouton_arret)
    # mise en place des images  de fond de base :
    can1.after(2000,affiche_image(epreuve_lettre))
    can1.update()
    can1.after(2000,affiche_image(plato_lettre))
    can1.update()
    
    # =============================================================================
    # Créations du mot
    # =============================================================================
    
    l_mot_trouver=melange()
    print(l_mot_trouver)
    
    jeux_1_lettre_2()
    
def jeux_1_lettre_2():                  
    
    global dico_ltr_img, dico_ltr_img_coord, compteur, cand_rep,liste_button
        
    compteur = 1
    cand_rep=[]
    
    reset_liste(liste_button)
    
  
    # =============================================================================
    # Mise en place images des images des lettres
    # =============================================================================
    
    lettre1 = can1.create_image(149,772, anchor='nw', image=quelle_lettre(str(l_mot_trouver[0][0])))
    lettre2 = can1.create_image(271,774, anchor='nw', image=quelle_lettre(str(l_mot_trouver[1][0])))
    lettre3 = can1.create_image(390,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[2][0])))
    lettre4 = can1.create_image(511,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[3][0])))
    lettre5 = can1.create_image(632,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[4][0])))
    lettre6 = can1.create_image(753,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[5][0])))
    lettre7 = can1.create_image(873,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[6][0])))
    lettre8 = can1.create_image(993,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[7][0])))
    lettre9 = can1.create_image(1115,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[8][0])))
    lettre10 = can1.create_image(1236,773, anchor='nw', image=quelle_lettre(str(l_mot_trouver[9][0])))
    
    dico_ltr_img = {'lettre1' : lettre1, 'lettre2' : lettre2, 'lettre3' : lettre3, 'lettre4' : lettre4,
                    'lettre5' : lettre5, 'lettre6' : lettre6, 'lettre7' : lettre7, 'lettre8' : lettre8,
                    'lettre9' : lettre9, 'lettre10' : lettre10}
    
    dico_ltr_img_coord = {'coord1' : [149, 772], 'coord2' : [271,774], 'coord3' : [390,773], 'coord4' : [511,773],
                    'coord5' : [632,773], 'coord6' : [753,773], 'coord7' : [873,773], 'coord8' : [993,773],
                    'coord9' : [1115,773], 'coord10' : [1236,773]}
    
    for i in range(1,11) :
        xn = dico_ltr_img_coord[('coord'+str(i))][0]
        yn = int(dico_ltr_img_coord[('coord'+str(i))][1])+156
        case_vide = can1.create_image(xn,yn , anchor='nw', image=grise_case)
    
    # =============================================================================
    # Créations boutons lettres + Ajout des boutons dans la liste pour ceux ci
    # =============================================================================
    
    Bouton14 = bouton([149, 772], [249, 874], "Bouton14", "lettre1", 'Make_Rep("'+l_mot_trouver[0][0]+'", "Bouton14")', l_mot_trouver[0][0])
    Bouton15 = bouton([269, 772], [371, 874], "Bouton15", "lettre2", 'Make_Rep("'+l_mot_trouver[1][0]+'", "Bouton15")', l_mot_trouver[1][0])
    Bouton16 = bouton([389, 772], [493, 874], "Bouton16", "lettre3", 'Make_Rep("'+l_mot_trouver[2][0]+'", "Bouton16")', l_mot_trouver[2][0])
    Bouton17 = bouton([509, 772], [615, 874], "Bouton17", "lettre4", 'Make_Rep("'+l_mot_trouver[3][0]+'", "Bouton17")', l_mot_trouver[3][0])
    Bouton18 = bouton([629, 772], [737, 874], "Bouton18", "lettre5", 'Make_Rep("'+l_mot_trouver[4][0]+'", "Bouton18")', l_mot_trouver[4][0])
    Bouton19 = bouton([749, 772], [859, 874], "Bouton19", "lettre6", 'Make_Rep("'+l_mot_trouver[5][0]+'", "Bouton19")', l_mot_trouver[5][0])
    Bouton20 = bouton([869, 772], [981, 874], "Bouton20", "lettre7", 'Make_Rep("'+l_mot_trouver[6][0]+'", "Bouton20")', l_mot_trouver[6][0])
    Bouton21 = bouton([989, 772], [1103, 874], "Bouton21", "lettre8", 'Make_Rep("'+l_mot_trouver[7][0]+'", "Bouton21")', l_mot_trouver[7][0])
    Bouton22 = bouton([1109, 772], [1225, 874], "Bouton22", "lettre9", 'Make_Rep("'+l_mot_trouver[8][0]+'", "Bouton22")', l_mot_trouver[8][0])
    Bouton23 = bouton([1229, 772], [1347, 874], "Bouton23", "lettre10", 'Make_Rep("'+l_mot_trouver[9][0]+'", "Bouton23")', l_mot_trouver[9][0])
    
    liste_button.append(Bouton14)
    liste_button.append(Bouton15)
    liste_button.append(Bouton16)
    liste_button.append(Bouton17)
    liste_button.append(Bouton18)
    liste_button.append(Bouton19)
    liste_button.append(Bouton20)
    liste_button.append(Bouton21)
    liste_button.append(Bouton22)
    liste_button.append(Bouton23)
    
    # =============================================================================
    # Bouton 'valider'
    # =============================================================================
    
    Bouton24 = bouton([1446, 839], [1809, 956], "om_lettre ---- VALIDER", None, 'est_mot()', None)
    liste_button.append(Bouton24)
    
    # =============================================================================
    # Bouton 'reset'
    # =============================================================================
    Bouton_arret=bouton([1541, 51],[1899, 165],"Arreter",None,"fin_du_jeu()",None)
    liste_button.append(Bouton_arret)
    
    Bouton25 = bouton([134, 921], [1350, 1033], "RESET", None, 'jeux_1_lettre_2()', None)
    liste_button.append(Bouton25)
    

def Make_Rep(t_lettre:str, bouton_mk:str):
    global cand_rep, cand_rep_str,liste_button
    '''on donne un str et un bouton qui sont envoyer dans différente fonction'''
    but_ltr_img(liste_button, bouton_mk) # Creer une nouvelle image sur la barre en dessous
    cand_rep.append(str(t_lettre)) # Ajoute t_lettre dans la reponse du joueur
    supp_bou_liste(liste_button, bouton_mk)  # Supprime le bouton cliqué par le joueur 
    cand_rep_str = lst_to_str(cand_rep)
    
def but_ltr_img(listee:list, bouton_dle:str):
    global compteur
    for elt in listee :
        if elt.get_nom() == str(bouton_dle) :
            
            can1.itemconfig(dico_ltr_img[elt.get_image()], image=grise_case)
            
            x1 = dico_ltr_img_coord[('coord'+str(compteur))][0]
            print(x1)
            y1 = int(dico_ltr_img_coord[('coord'+str(compteur))][1])+156
            print(y1)
            nvl_image = quelle_lettre(str(elt.get_lettre()))
            nvll_lettre = can1.create_image(x1,y1 , anchor='nw', image=nvl_image)
            compteur = compteur + 1 

def quelle_lettre(lettre:str):
    dico = {'a' :a_image, 'b' :b_image, 'c' :c_image, 'd' :d_image, 'e' :e_image, 'f' :f_image, 'g' :g_image, 'h' :h_image, 'i' :i_image, 'j' :j_image, 'k' :k_image, 'l' :l_image, 'm' :m_image, 'n' :n_image, 'o' :o_image, 'p' :p_image, 'q' :q_image, 'r' :r_image, 's' :s_image, 't' :t_image, 'u' :u_image, 'v' :v_image, 'w' :w_image, 'x' :x_image, 'y' :y_image, 'z' :z_image}
    return(dico[lettre])
    
def melange():
    liste=[]
    nv_mot=[]
    with open("doc_txt/10_liste6.txt", "r") as tf:
        lines = tf.read().split('\n')
    for elt in lines:
        liste.append(elt)
        mot=choice(liste)
    for elti in mot:
        nv_mot.append(elti.split())
    print(nv_mot)
    shuffle(nv_mot)
    return(nv_mot)

def lst_to_str(liste_mot:list):
    mot=''
    for elt in liste_mot :
        mot = mot + elt
    return(mot)

def est_mot():
    global liste_button, cand_rep_str
    n=0
    cand_rep_str = cand_rep_str + str("\n")
    lst_fr = open("./doc_txt/liste_francais.txt", 'r')
    for elt in lst_fr:
        if elt == cand_rep_str:
            n+=1
            score_chiffre()
            return(True)
    can1.after(0, affiche_image(mot_null))   
    can1.update()
    can1.after(1500,affiche_image(plato_lettre))
    can1.update()
    can1.after(0, jeux_1_lettre_2())

def score_chiffre():
    global cand_rep_str,score,liste_button
    reset_liste(liste_button)
    Bouton_arret=bouton([1541, 51],[1899, 165],"Arreter",None,"fin_du_jeu()",None)
    liste_button.append(Bouton_arret)
    if len(cand_rep_str)-1==10:
        can1.after(0,affiche_image(vingcinq))
        can1.update()
        Score.set_score(25)
        actualise_score(Score)
    elif len(cand_rep_str)-1<10 and len(cand_rep_str)-1>8:
        can1.after(0,affiche_image(quinze))
        can1.update()
        Score.set_score(15)
        actualise_score(Score)
    elif len(cand_rep_str)-1<=8 and len(cand_rep_str)-1>6:
        can1.after(0,affiche_image(dix))
        can1.update()
        Score.set_score(10)
        actualise_score(Score)
    elif len(cand_rep_str)-1<=6 and len(cand_rep_str)-1>4:
        can1.after(0,affiche_image(cinqpts))
        can1.update()
        Score.set_score(5)
        actualise_score(Score)
    elif len(cand_rep_str)-1<=4:
        can1.after(0,affiche_image(unpts))
        can1.update()
        Score.set_score(1)
        actualise_score(Score)

def actualise_score(score):
    global Labelscore
    score1 = StringVar()
    Labelscore = Label(MaFenetre, textvariable = score1 , bg ="white",font=("Courier",60),width=13,height=2)
    score1.set(Score.get_score())
    Labelscore.place(x=915,y=785)
    can1.update()
    can1.after(2000,jeux_1())
    can1.update()

    
# =============================================================================
# Jeux des opérations
# =============================================================================


def jeux_1_operations():
    global liste_buttonLabelscore
    reset_liste(liste_button)
    Labelscore.destroy()
    can1.after(2000,affiche_image(epreuve_ope))
    can1.update()
    can1.after(0,operation())
    can1.update()

def kill_label():
    global Champ1,liste_button,LabelResultat,LabelResultat2,LabelResultat3,LabelResultat4
    Champ1.destroy()
    LabelResultat.destroy()
    LabelResultat2.destroy()
    LabelResultat3.destroy()
    LabelResultat4.destroy()
    can1.update()
    can1.after(0,fin_du_jeu)
    can1.update()    

def operation():
    global operation1,LabelResultat,LabelResultat2,LabelResultat3,LabelResultat4,liste_button,Champ1
    reset_liste(liste_button)
    Bouton_arret=bouton([1541, 51],[1899, 165],"Arreter",None,"kill_label()",None)
    liste_button.append(Bouton_arret)
    operation1=0
    can1.after(2000,affiche_image(operation_jeux))
    can1.update()
    a=randint(0,50)
    b=randint(0,50)
    c=randint(1,12)
    d=randint(0,50)
    e=str(a)
    f=str(b)
    g=str(c)
    h=str(d)
    operation_afficher="(("+e+"+"+f+")*"+g+")-"+h
    operation1=((a+b)*c)-d
    Text = StringVar()
    LabelResultat = Label(MaFenetre, textvariable = Text , bg ="white",font=("Courier",60),width=3,height=1)
    Text.set(e)
    LabelResultat.place(x=423,y=650)
       
    Text2 = StringVar()
    LabelResultat2 = Label(MaFenetre, textvariable = Text2 , bg ="white",font=("Courier",60),width=3,height=1)
    Text2.set(f)
    LabelResultat2.place(x=688,y=650)
        
    Text3 = StringVar()
    LabelResultat3 = Label(MaFenetre, textvariable = Text3 , bg ="white",font=("Courier",60),width=3,height=1)
    Text3.set(g)
    LabelResultat3.place(x=1064,y=650)
        
    Text4 = StringVar()
    LabelResultat4 = Label(MaFenetre, textvariable = Text4 , bg ="white",font=("Courier",60),width=3,height=1)
    Text4.set(h)
    LabelResultat4.place(x=1406,y=650)
        
    print(operation_afficher)
    print(operation1)
    
    Nombre1= IntVar()
    Nombre1.set(0)
    Champ1 = Entry(MaFenetre, textvariable= Nombre1, bg ="bisque", fg="maroon",font=("Courier",80),justify="center")
    Champ1.focus_set()
    Champ1.place(x=945,y=793,width=500, height=170)
    print("ok")
    Bouton_rep=bouton([1470, 793],[1800, 954], "Réponse", None, "rep()", None)   
    liste_button.append(Bouton_rep)

def rep():
    global Champ1,LabelResultat,LabelResultat2,LabelResultat3,LabelResultat4,Labelscore
    reset_liste(liste_button)
    
    
    Res=int(Champ1.get())
    print(Res)
    LabelResultat.destroy()
    LabelResultat2.destroy()
    LabelResultat3.destroy()
    LabelResultat4.destroy()
    resultat(Res)

def resultat(reponse):
    global operation1,Champ1,liste_button
    print("bonjour")
    Champ1.destroy()
    Bouton_arret=bouton([1541, 51],[1899, 165],"Arreter",None,"fin_du_jeu()",None)
    liste_button.append(Bouton_arret)
    if reponse==operation1:
        print("Succès vous gagnez 15 points !")
        can1.after(0,affiche_image(quinze))
        can1.update()
        Score.set_score(15)
        actualise_score(Score)
        
    elif reponse<=operation1+15 and reponse>operation1+10:
        print("Succès vous gagnez 1 points !")
        can1.after(0,affiche_image(unpts))
        can1.update()
        Score.set_score(1)
        actualise_score(Score)

    elif reponse<=operation1+10 and reponse>operation1+5:
        print("Succès vous gagnez 5 points !")
        can1.after(0,affiche_image(cinqpts))
        can1.update()
        Score.set_score(5)
        actualise_score(Score)

    elif reponse<=operation1+5 and reponse>operation1:
        print("Succès vous gagnez 10 points !")
        can1.after(0,affiche_image(dix))
        can1.update()
        Score.set_score(10)
        actualise_score(Score)

    elif reponse>=operation1-15 and reponse<operation1-10:
        print("Succès vous gagnez 1 points !")
        can1.after(0,affiche_image(unpts))
        can1.update()
        Score.set_score(1)
        actualise_score(Score)
    
    elif reponse>=operation1-10 and reponse<operation1-5:
        print("Succès vous gagnez 5 points !")
        can1.after(0,affiche_image(cinqpts))
        can1.update()
        Score.set_score(5)
        actualise_score(Score)
   
    elif reponse>=operation1-5 and reponse<operation1:
        print("Succès vous gagnez 10 points !")
        can1.after(0,affiche_image(dix))
        can1.update()
        Score.set_score(10)
        actualise_score(Score)
    
    else:
        print("Echec vous ne gagnez aucun points !")
        can1.after(1,affiche_image(zeropts))
        can1.update()
        Score.set_score(0)
        actualise_score(Score)


    
# ===================== FIN JEUX 1 / ECRAN AUTRE JEUX==========================
def fin_du_jeu():
    global Champ1,Labelscore,LabelResultat, LabelResultat2, LabelResultat3,LabelResultat4,liste_button,Score
    reset_liste(liste_button)
    can1.after(0,affiche_image(final))
    can1.update()
    Bouton_menu=bouton([1480, 504],[1811, 613],"Menu",None,"menu()",None)
    liste_button.append(Bouton_menu)
    score1 = StringVar()
    Labelscore = Label(MaFenetre, textvariable = score1 , bg ="white",font=("Courier",60),width=13,height=2)
    score1.set(Score.get_score())
    Labelscore.place(x=1089,y=776)
    Score.ajouter_score()
    can1.update()
    

def ecran_2():
    '''fonction pour jouer au jeu 1 : finit le freestyle'''
    affiche_image(fond_jeux_inexistant_2)


def ecran_3():
    affiche_image(fond_jeux_inexistant_3)


def ecran_4():
    affiche_image(fond_jeux_inexistant_4)
    
    
def ecran_5():
    affiche_image(fond_jeux_inexistant_5)
    
    
def ecran_6():
    affiche_image(fond_jeux_inexistant_6)

    
def ecran_7():
    affiche_image(fond_jeux_inexistant_7)
 
    
def ecran_8():
    affiche_image(fond_jeux_inexistant_8)
    

    
def est_bouton(lcoo:list, lbut:list):
    '''On parcours la liste de bouton pour verifier si les axes X et Y où il y a eu le click,
    puis on regarde si cette zone est attribué à un bouton'''
    global can1, Bouton1, Bouton2, Bouton3, Bouton4, Bouton5, Bouton6, Bouton7,Bouton8, Bouton9, Bouton10, liste_button, bou1
    try :
        for boutton in liste_button: #début du parcours
            if lcoo[0] > boutton.get_coo_min()[0]: #test 1 
                if lcoo[0] < boutton.get_coo_max()[0]: #test2
                    if lcoo[1] > boutton.get_coo_min()[1]: # test 3
                        if lcoo[1] < boutton.get_coo_max()[1]: #test 4 
                            #puisque tous les test sont réussi, on peut afficher l'image qui est défini au bouton.
                            #entre autre, on regarde le bouton que l'on testait, et puisque tout est bon, on prend l'image
                            #de ce bouton et on l'affiche.
                            exec(boutton.get_fonction())
            else:
                #sinon on pass au test du prochain bouton
                pass
    except :
        print("Le bouton n'existe plus ou ce n'est pas un bouton")


def affiche_image(img):
    '''permet d'afficher une image sur la main-loop '''
    global can1, Bouton1, Bouton2, Bouton3, Bouton4, Bouton5, Bouton6, Bouton7,Bouton8, Bouton9, Bouton10, liste_button, bou1
    image_fond=can1.create_image(0,0,image=img,anchor="nw")

def random():
    rand=random.randint(0,1)
    return rand

def Clique(event):
    '''Dans cette fonction, on récupère les coordonées où a eu lieu le clique puis on les stocks
    dans la liste l, pour pouvoir utilisé ces coordonées pour les comparées ect (#est_bouton)'''
    l=[] # Création de la liste pour tout stocker 
    abscisse=event.x #Récupération de l'abscisse 
    l.append(abscisse) #Ajout de la position en abscisse a la liste 
    ordonnee=event.y #Récupération de l'ordonnee
    l.append(ordonnee) #Ajout de la position en ordonnée a la liste
    est_bouton(l, liste_button) #Ici, on envoie la liste de coordonnéesainsi que la liste des boutons dans #est_boutons
    print(l)

def rick():
    pass
    # playsound("operations_manuscrites.wav")
    
# ============================== FONCTION LISTE ===============================

def affiche_but_liste(liste:list):
    '''renvoie le nom des boutons contenus dans une liste'''
    for elt in liste:
        print(elt.get_nom())

def reset_liste(liste:list):
    '''réinitialise la liste donner'''
    for i in range(len(liste)):
        liste_button.pop()

def supp_bou_liste(liste:list, bouton_sbl:str):
    '''supprime un bouton donner dans la liste donner'''
    for elt in liste :
        if elt.get_nom() == str(bouton_sbl) :
            liste.remove(elt)
        else:
            pass

# ========================== LANCEMENT DU PROGRAMME ===========================

liste_button=[]

# [['t'], ['i'], ['s'], ['f'], ['t'], ['s'], ['a'], ['i'], ['s'], ['a']] : facile 

menu()

MaFenetre.mainloop()