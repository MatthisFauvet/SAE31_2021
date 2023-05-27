# -*- coding: utf-8 -*-
"""
Created on Tue May 17 03:53:47 2022

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
from scoreBDD import *


# ========================= CRÉATIONS DE LA FENETRE ===========================

MaFenetre=Tk()
MaFenetre.geometry('1280x720')

# ======================== IMPORTATIONS DES IMAGES INTRO =======================

adresse_mail_image=PhotoImage(file="./images/images_menu/debut/mail.png")
presente_image=PhotoImage(file="./images/images_menu/debut/presente.png")
mauvais_mail=PhotoImage(file="./images/images_menu/mauvai_mail.png")
debut_image1=PhotoImage(file="./images/images_menu/debut/image1.png")
debut_image2=PhotoImage(file="./images/images_menu/debut/image2.png")
debut_image3=PhotoImage(file="./images/images_menu/debut/image3.png")
debut_image4=PhotoImage(file="./images/images_menu/debut/image4.png")
debut_image5=PhotoImage(file="./images/images_menu/debut/image5.png")
debut_image6=PhotoImage(file="./images/images_menu/debut/image6.png")
debut_image7=PhotoImage(file="./images/images_menu/debut/image7.png")
debut_image8=PhotoImage(file="./images/images_menu/debut/image8.png")
debut_image9=PhotoImage(file="./images/images_menu/debut/image9.png")
debut_image10=PhotoImage(file="./images/images_menu/debut/image10.png")
debut_image11=PhotoImage(file="./images/images_menu/debut/image11.png")
debut_image12=PhotoImage(file="./images/images_menu/debut/image12.png")
debut_image13=PhotoImage(file="./images/images_menu/debut/image13.png")
debut_image14=PhotoImage(file="./images/images_menu/debut/image14.png")
debut_image15=PhotoImage(file="./images/images_menu/debut/image15.png")
debut_image16=PhotoImage(file="./images/images_menu/debut/image16.png")
debut_image17=PhotoImage(file="./images/images_menu/debut/image17.png")

list_image_intro=[debut_image1, debut_image2, debut_image3, debut_image4, debut_image5, debut_image6, debut_image7, debut_image8,debut_image9,
               debut_image10,debut_image11, debut_image12,debut_image13, debut_image14, debut_image15, debut_image16,debut_image17]

# ======================== IMPORTATIONS DES IMAGES MENU =======================

fond_menu=PhotoImage(file="./images/images_menu/Menu_tele_no_signal.png")
fond_plato_om=PhotoImage(file="./images/images_menu/Menu_tele_operations_manuscrites.png")
fond_jeux_inexistant_1=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_1.png")
fond_jeux_inexistant_2=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_2.png")
fond_jeux_inexistant_3=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_3.png")
fond_jeux_inexistant_4=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_4.png")
fond_jeux_inexistant_5=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_5.png")
fond_jeux_inexistant_6=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_6.png")
fond_jeux_inexistant_7=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_7.png")    
fond_jeux_inexistant_8=PhotoImage(file="./images/images_menu/Menu_tele_jeux_inexistant_8.png")
fond_jeux_inexistant_9=PhotoImage(file="./images/images_menu/RickAstley.png")

# ===================== IMPORTATIONS DES IMAGES JEUX 1 ========================

#plato

fond_jeux_1=PhotoImage(file="./images/image_jeux_1/plato_perso.png")
plato_lettre=PhotoImage(file="./images/image_jeux_1/eppreuve_lettre_v1.png")
bravo1=PhotoImage(file="./images/image_jeux_1/bravo_lettre.png")

#regles 

regles_questions=PhotoImage(file="./images/image_jeux_1/regles_questions.png")
regles=PhotoImage(file="./images/image_jeux_1/regles.png")


#random

epreuve_lettre=PhotoImage(file="./images/image_jeux_1/epreuve_l.png")
epreuve_ope=PhotoImage(file="./images/image_jeux_1/epreuve_o.png")
grise_case=PhotoImage(file="./images/image_jeux_1/grise2.png")

#opération
operation_jeux=PhotoImage(file="./images/image_jeux_1/operation_jeux.png")

#Attribution des points
vingcinq=PhotoImage(file="./images/image_jeux_1/25pts.png")
quinze=PhotoImage(file="./images/image_jeux_1/15pts.png")
dix=PhotoImage(file="./images/image_jeux_1/10pts.png")
cinqpts=PhotoImage(file="./images/image_jeux_1/5pts.png")
unpts=PhotoImage(file="./images/image_jeux_1/1pts.png")
zeropts=PhotoImage(file="./images/image_jeux_1/0pts.png")
mot_null=PhotoImage(file="./images/image_jeux_1/mot_null.png")

#Page final
final=PhotoImage(file="./images/image_jeux_1/fin.png")

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
# Liste de toutes les images pour les resize (list)
# =============================================================================


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
    global can1, mail_text
    
    try :    
        Labelscore.destroy()
    except :
        pass
    
    for elt in list_image_intro :
        affiche_image(elt)
    
    file = open("./doc_txt/mail_joueur.txt", 'r')
    email = ""
    for elt in file :
        email = email + elt
    file.close()
    
    if email == "empty_please_enter_value":
        can1.after(0, affiche_image(adresse_mail_image))
        mail_text = Entry(MaFenetre, bg ="bisque", fg="maroon",font=("Courier",25),justify="center")
        mail_text.focus_set()
        mail_text.place(x=86,y=550,width=727, height=110)
        
        Bouton0 = bouton([909, 549], [1221, 658], "Bouton0", None, "ajouter_mail()", None)
        pile_button.empiler(Bouton0)
        
    else :
        get_score_online()
        menu2()
    
def menu2():
    global can1, Bouton1, Bouton2, Bouton3, Bouton4, Bouton5, Bouton6, Bouton7,Bouton8, pile_button, bou1,cand_rep, compteur,Score
    
    try :
        mail_text.destroy()
    except :
        pass
    
    try :
        mail_text_cu.destroy()
    except :
        pass
    
    Score = SCORE(0)
    
    # ====================== CRÉATIONS DES BOUTONS + LISTE ====================
    
    reset_pile_file(pile_button)
    
    Bouton1 = bouton([718, 188], [744, 201], "Bouton1", fond_plato_om, "ecran_1()", None)
    Bouton2 = bouton([718, 206], [744, 218], "Bouton2",fond_jeux_inexistant_2, "ecran_2()", None)
    Bouton3 = bouton([718, 224], [744, 236], "Bouton3",fond_jeux_inexistant_3, "ecran_3()", None)
    Bouton4 = bouton([718, 243], [744, 255], "Bouton4",fond_jeux_inexistant_4,"ecran_4()", None)
    Bouton5 = bouton([718, 262], [744, 272], "Bouton5",fond_jeux_inexistant_5,"ecran_5()", None)
    Bouton6 = bouton([718, 279], [744, 292], "Bouton6",fond_jeux_inexistant_6,"ecran_6()", None)
    Bouton7 = bouton([718, 297], [744, 309], "Bouton7",fond_jeux_inexistant_7,"ecran_7()", None)
    Bouton8 = bouton([718, 315], [744, 328], "Bouton8",fond_jeux_inexistant_8,"change_user()", None)
    
    Bouton9 = bouton([744, 361], [770, 371], "Bouton9", fond_menu, "menu()", None)
    
    Bouton10 = bouton([776, 363], [800, 372],"Bouton10", None, "rick()", None)
    
    Bouton45=bouton([866, 517],[1244, 644],"quitter",None,"MaFenetre.destroy()",None)
    
    pile_button.empiler(Bouton1)
    pile_button.empiler(Bouton2)
    pile_button.empiler(Bouton3)
    pile_button.empiler(Bouton4)
    pile_button.empiler(Bouton5)
    pile_button.empiler(Bouton6)
    pile_button.empiler(Bouton7)
    pile_button.empiler(Bouton8)
    pile_button.empiler(Bouton9)
    pile_button.empiler(Bouton10)
    pile_button.empiler(Bouton45)
    
    #=================== MISE EN PLACE FOND + REGARD CLIQUE ====================
    
    image_fond=can1.create_image(0,0,image=fond_menu, anchor="nw") #set-up de la premiere iage a afficher

def ecran_1():
    '''fonction pour jouer au jeux 1 : Opérations manuscrite'''
    image_fond=can1.create_image(0,0,image=fond_plato_om,anchor="nw")
    
    Bouton11 = bouton([182, 430], [610, 516], "Bouton11", None, "jeux_1_init()", None)
    pile_button.empiler(Bouton11)
    
# =================================   JEUX 1   ================================

def jeux_1_init():
    '''initialisation du jeux1 -> mise en route (regles)'''
    global Labelscore,pile_button
    reset_pile_file(pile_button)
    
    can1.after(0,affiche_image(fond_jeux_1))
    can1.update()
    
    score1 = StringVar()
    Labelscore = Label(MaFenetre, textvariable = score1 , bg ="lightblue",font=("Courier",60),width=3,height=1)
    score1.set(Score.get_score())
    Labelscore.place(x=1596,y=45)
    Labelscore.destroy()
    
    can1.after(0,affiche_image(regles_questions))
    can1.update()
    
    reset_pile_file(pile_button)
    
    
    
    Bouton_arret=bouton([1028, 34],[1264, 108],"Arreter",None,"fin_du_jeu()",None)
    pile_button.empiler(Bouton_arret)
    
    

    Bouton12 = bouton([387, 498],[615, 612],"Bouton12",None,"jeux_1_regles()",None)
    pile_button.empiler(Bouton12) 
    
    Bouton13 = bouton([652, 498],[878, 612],"Bouton13",None,"jeux_1()",None)
    pile_button.empiler(Bouton13)
    
def jeux_1_regles():
    '''fonction qui permet d'afficher les règles du jeux 1'''
    
    reset_pile_file(pile_button)
    
    can1.after(0,affiche_image(regles)) #mise en place de l'image avec les règles
   
    Bouton_arret=bouton([13, 608],[250, 684],"Arreter",None,"fin_du_jeu()",None)
    pile_button.empiler(Bouton_arret)
    
    #bouton commencer :
    Bouton50 = bouton([449, 591],[830, 676], 'Bouton50', None, 'jeux_1()', None)
    pile_button.empiler(Bouton50)

def jeux_1():
    global pile_button,compteur,cand_rep,Labelscore
    reset_pile_file(pile_button)
    Labelscore.destroy()
    
    Bouton_arret=bouton([1028, 34],[1264, 108],"Arreter",None,"fin_du_jeu()",None)
    pile_button.empiler(Bouton_arret)
    
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
    global pile_button, l_mot_trouver, pile_button #, lettre0, lettre1, lettre2, lettre3, lettre4, lettre5, lettre6, lettre7, lettre8, lettre9
    
    # print("========================== ENTRE DANS JEU_1_lettres =======================")
    
    #on réinitialise la pile_button, pour supprimer tous les précédent boutons
    reset_pile_file(pile_button)
    
    Bouton_arret=bouton([1028, 34],[1264, 108],"Arreter",None,"fin_du_jeu()",None)
    pile_button.empiler(Bouton_arret)
    
    # mise en place des images  de fond de base :
    can1.after(2000,affiche_image(epreuve_lettre))
    can1.update()
    can1.after(2000,affiche_image(plato_lettre))
    can1.update()
    
    # =============================================================================
    # Créations du mot
    # =============================================================================
    
    # On détermine quelle mot les joueurs devront trouver :
    l_mot_trouver=melange()
    
    jeux_1_lettre_2()
    
def jeux_1_lettre_2():                  
    
    global dico_ltr_img, dico_ltr_img_coord, compteur, cand_rep,pile_button, dico_ltr_to_modify_image
    
    #print("========================== ENTRE DANS jeux_1_lettre_2 =======================")
        
    compteur = 1
    cand_rep=[]
    
    reset_pile_file(pile_button)
    
  
    # =============================================================================
    # Mise en place images des images des lettres
    # =============================================================================
    
    lettre1 = can1.create_image(99,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[0][0])))
    lettre2 = can1.create_image(180,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[1][0])))
    lettre3 = can1.create_image(260,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[2][0])))
    lettre4 = can1.create_image(341,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[3][0])))
    lettre5 = can1.create_image(421,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[4][0])))
    lettre6 = can1.create_image(502,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[5][0])))
    lettre7 = can1.create_image(583,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[6][0])))
    lettre8 = can1.create_image(663,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[7][0])))
    lettre9 = can1.create_image(744,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[8][0])))
    lettre10 = can1.create_image(824,515, anchor='nw', image=quelle_lettre(str(l_mot_trouver[9][0])))
    
    dico_ltr_img = {'lettre1' : lettre1, 'lettre2' : lettre2, 'lettre3' : lettre3, 'lettre4' : lettre4,
                    'lettre5' : lettre5, 'lettre6' : lettre6, 'lettre7' : lettre7, 'lettre8' : lettre8,
                    'lettre9' : lettre9, 'lettre10' : lettre10}
    
    dico_ltr_img_coord = {'coord1' : [99, 515], 'coord2' : [180, 515], 'coord3' : [260, 515], 'coord4' : [341, 515],
                    'coord5' : [421, 515], 'coord6' : [502, 515], 'coord7' : [583, 515], 'coord8' : [663, 515],
                    'coord9' : [744, 515], 'coord10' : [824, 515]}
    
    dico_ltr_to_modify_image = {'lettre1' : quelle_lettre(str(l_mot_trouver[0][0])), 'lettre2' : quelle_lettre(str(l_mot_trouver[1][0])),
                                'lettre3' : quelle_lettre(str(l_mot_trouver[2][0])), 'lettre4' : quelle_lettre(str(l_mot_trouver[3][0])),
                                'lettre5' : quelle_lettre(str(l_mot_trouver[4][0])), 'lettre6' : quelle_lettre(str(l_mot_trouver[5][0])),
                                'lettre7' : quelle_lettre(str(l_mot_trouver[6][0])), 'lettre8' : quelle_lettre(str(l_mot_trouver[7][0])),
                                'lettre9' : quelle_lettre(str(l_mot_trouver[8][0])), 'lettre10' : quelle_lettre(str(l_mot_trouver[9][0]))}
    
    # Création des cases grises du bas 
    for i in range(1,11) :
        xn = dico_ltr_img_coord[('coord'+str(i))][0]
        yn = int(dico_ltr_img_coord[('coord'+str(i))][1])+104
        case_vide = can1.create_image(xn,yn , anchor='nw', image=grise_case)
    
    # =============================================================================
    # Créations boutons lettres + Ajout des boutons dans la liste pour ceux ci
    # =============================================================================
    
    global Bouton14, Bouton15, Bouton16, Bouton17, Bouton18, Bouton19, Bouton20, Bouton21, Bouton22, Bouton23
    
    Bouton14 = bouton([99, 515], [167, 583], "Bouton14", "lettre1", 'Make_Rep("'+l_mot_trouver[0][0]+'", "Bouton14")', l_mot_trouver[0][0])
    Bouton15 = bouton([180, 515], [247, 581], "Bouton15", "lettre2", 'Make_Rep("'+l_mot_trouver[1][0]+'", "Bouton15")', l_mot_trouver[1][0])
    Bouton16 = bouton([260, 515], [328, 582], "Bouton16", "lettre3", 'Make_Rep("'+l_mot_trouver[2][0]+'", "Bouton16")', l_mot_trouver[2][0])
    Bouton17 = bouton([341, 515], [408, 582], "Bouton17", "lettre4", 'Make_Rep("'+l_mot_trouver[3][0]+'", "Bouton17")', l_mot_trouver[3][0])
    Bouton18 = bouton([421, 515], [489, 583], "Bouton18", "lettre5", 'Make_Rep("'+l_mot_trouver[4][0]+'", "Bouton18")', l_mot_trouver[4][0])
    Bouton19 = bouton([502, 515], [569, 582], "Bouton19", "lettre6", 'Make_Rep("'+l_mot_trouver[5][0]+'", "Bouton19")', l_mot_trouver[5][0])
    Bouton20 = bouton([583, 515], [650, 582], "Bouton20", "lettre7", 'Make_Rep("'+l_mot_trouver[6][0]+'", "Bouton20")', l_mot_trouver[6][0])
    Bouton21 = bouton([663, 515], [730, 582], "Bouton21", "lettre8", 'Make_Rep("'+l_mot_trouver[7][0]+'", "Bouton21")', l_mot_trouver[7][0])
    Bouton22 = bouton([744, 515], [811, 581], "Bouton22", "lettre9", 'Make_Rep("'+l_mot_trouver[8][0]+'", "Bouton22")', l_mot_trouver[8][0])
    Bouton23 = bouton([824, 515], [892, 581], "Bouton23", "lettre10", 'Make_Rep("'+l_mot_trouver[9][0]+'", "Bouton23")', l_mot_trouver[9][0])
    
    pile_button.empiler(Bouton14)
    pile_button.empiler(Bouton15)
    pile_button.empiler(Bouton16)
    pile_button.empiler(Bouton17)
    pile_button.empiler(Bouton18)
    pile_button.empiler(Bouton19)
    pile_button.empiler(Bouton20)
    pile_button.empiler(Bouton21)
    pile_button.empiler(Bouton22)
    pile_button.empiler(Bouton23)
    
    # =============================================================================
    # Bouton 'valider'
    # =============================================================================
    
    Bouton24 = bouton([964, 561], [1205, 639], "om_lettre ---- VALIDER", None, 'est_mot()', None)
    pile_button.empiler(Bouton24)
    
    # =============================================================================
    # Bouton Arret jeu 
    # =============================================================================
    
    Bouton_arret=bouton([1028, 34],[1264, 108],"Arreter",None,"fin_du_jeu()",None)
    pile_button.empiler(Bouton_arret)
    
    # =============================================================================
    # Bouton 'reset'
    # =============================================================================
    
    Bouton25 = bouton([90, 613], [904, 688], "RESET", None, 'retire_elt_rep()', None)
    pile_button.empiler(Bouton25)

def Make_Rep(t_lettre:str, bouton_mk:str):
    global cand_rep, cand_rep_str,pile_button, tempo, pile_supp
    '''on donne un str et un bouton qui sont envoyer dans différente fonction'''
    but_ltr_img(pile_button, bouton_mk) # Creer une nouvelle image sur la barre en dessous
    cand_rep.append(str(t_lettre)) # Ajoute t_lettre dans la reponse du joueur
    supp_bou_liste(pile_button, bouton_mk)  # Supprime le bouton cliqué par le joueur
    pile_supp.empiler(bouton_mk)
    cand_rep_str = lst_to_str(cand_rep)
    
    
def but_ltr_img(pile:list, bouton_dle:str):
    global compteur, temorary_memory, pile_supp_2
    
    Pile2 = Pile()
    Pile_res = Pile()
    
    while pile.vide() != True :
        n = pile.depiler()
        Pile2.empiler(n)
        Pile_res.empiler(n)
    while Pile_res.vide() != True :
        m = Pile_res.depiler()
        pile_button.empiler(m)
        
    while Pile2.vide() != True:
        temp_memory = Pile2.depiler()
        if temp_memory.get_nom() == str(bouton_dle) :
            
            can1.itemconfig(dico_ltr_img[temp_memory.get_image()], image=grise_case)
            
            x1 = dico_ltr_img_coord[('coord'+str(compteur))][0]
            #print(x1)
            y1 = int(dico_ltr_img_coord[('coord'+str(compteur))][1])+104
            #print(y1)
            
            nvl_image = quelle_lettre(str(temp_memory.get_lettre()))
            nvll_lettre = can1.create_image(x1,y1 , anchor='nw', image=nvl_image)
            pile_supp_2.empiler(nvll_lettre)
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
    #print(nv_mot)
    shuffle(nv_mot)
    return(nv_mot)




def retire_elt_rep():
    global cand_rep, dico_ltr_bouton, compteur
    assert len(cand_rep) > 0
    
    # Étape 1 : supprimer la derniere lettre ajouter dans le mot du joueur
    
    cand_rep.pop()
        
    #Étape 2 : Remmettre le bouton en services, réajouter son image
    
    dico_ltr_bouton = {'Bouton14' : Bouton14, 'Bouton15' : Bouton15, 'Bouton16' : Bouton16, 'Bouton17' : Bouton17,
                    'Bouton18' : Bouton18, 'Bouton19' : Bouton19, 'Bouton20' : Bouton20, 'Bouton21' : Bouton21,
                    'Bouton22' : Bouton22, 'Bouton23' : Bouton23}
    
    tempo = pile_supp.depiler()
    can1.itemconfig(dico_ltr_img[dico_ltr_bouton[tempo].get_image()], image=dico_ltr_to_modify_image[dico_ltr_bouton[tempo].get_image()])
    
    pile_button.empiler(dico_ltr_bouton[tempo])
    
    compteur = compteur-1
    
    #Étape 3 : Modifier l'image qui a été déplacer en bas 
    tempo2 = pile_supp_2.depiler()
    can1.itemconfig(tempo2, image=grise_case)
    
    return cand_rep_str


def lst_to_str(liste_mot:list):
    mot=''
    for elt in liste_mot :
        mot = mot + elt
    return(mot)


def est_mot():
    global pile_button, cand_rep_str
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
    global cand_rep_str,score,pile_button
    reset_pile_file(pile_button)
    Bouton_arret=bouton([1028, 34],[1264, 108],"Arreter",None,"fin_du_jeu()",None)
    pile_button.empiler(Bouton_arret)
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
    Labelscore = Label(MaFenetre, textvariable = score1 , bg ="white",font=("Courier",60),width=8,height=1)
    score1.set(Score.get_score())
    Labelscore.place(x=700,y=540)
    can1.update()
    can1.after(2000,jeux_1())
    can1.update()

    
# =============================================================================
# Jeux des opérations
# =============================================================================


def jeux_1_operations():
    global pile_buttonLabelscore
    reset_pile_file(pile_button)
    Labelscore.destroy()
    can1.after(2000,affiche_image(epreuve_ope))
    can1.update()
    can1.after(0,operation())
    can1.update()

def kill_label():
    global Champ1,pile_button,LabelResultat,LabelResultat2,LabelResultat3,LabelResultat4
    Champ1.destroy()
    LabelResultat.destroy()
    LabelResultat2.destroy()
    LabelResultat3.destroy()
    LabelResultat4.destroy()
    can1.update()
    can1.after(0,fin_du_jeu)
    can1.update()    

def operation():
    global operation1,LabelResultat,LabelResultat2,LabelResultat3,LabelResultat4,pile_button,Champ1
    reset_pile_file(pile_button)
    Bouton_arret=bouton([1028, 34],[1264, 108],"Arreter",None,"kill_label()",None)
    pile_button.empiler(Bouton_arret)
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
    LabelResultat = Label(MaFenetre, textvariable = Text , bg ="white",font=("Courier",40),width=3,height=1)
    Text.set(e)
    LabelResultat.place(x=279,y=435)
       
    Text2 = StringVar()
    LabelResultat2 = Label(MaFenetre, textvariable = Text2 , bg ="white",font=("Courier",40),width=3,height=1)
    Text2.set(f)
    LabelResultat2.place(x=470,y=435)
        
    Text3 = StringVar()
    LabelResultat3 = Label(MaFenetre, textvariable = Text3 , bg ="white",font=("Courier",40),width=3,height=1)
    Text3.set(g)
    LabelResultat3.place(x=713,y=435)
        
    Text4 = StringVar()
    LabelResultat4 = Label(MaFenetre, textvariable = Text4 , bg ="white",font=("Courier",40),width=3,height=1)
    Text4.set(h)
    LabelResultat4.place(x=943,y=435)
        
    #print(operation_afficher)
    #print(operation1)
    
    Nombre1= IntVar()
    Nombre1.set(0)
    Champ1 = Entry(MaFenetre, textvariable= Nombre1, bg ="bisque", fg="maroon",font=("Courier",40),justify="center")
    Champ1.focus_set()
    Champ1.place(x=630,y=528,width=317, height=112)
    
    Bouton_rep=bouton([979, 528],[1201, 639], "Réponse", None, "rep()", None)   
    pile_button.empiler(Bouton_rep)

def rep():
    global Champ1,LabelResultat,LabelResultat2,LabelResultat3,LabelResultat4,Labelscore
    reset_pile_file(pile_button)
    
    
    Res=int(Champ1.get())
    #print(Res)
    LabelResultat.destroy()
    LabelResultat2.destroy()
    LabelResultat3.destroy()
    LabelResultat4.destroy()
    resultat(Res)

def resultat(reponse):
    global operation1,Champ1,pile_button
    #print("bonjour")
    Champ1.destroy()
    Bouton_arret=bouton([1028, 34],[1264, 108],"Arreter",None,"fin_du_jeu()",None)
    pile_button.empiler(Bouton_arret)
    if reponse==operation1:
        #print("Succès vous gagnez 15 points !")
        can1.after(0,affiche_image(quinze))
        can1.update()
        Score.set_score(15)
        actualise_score(Score)
        
    elif reponse<=operation1+15 and reponse>operation1+10:
        #print("Succès vous gagnez 1 points !")
        can1.after(0,affiche_image(unpts))
        can1.update()
        Score.set_score(1)
        actualise_score(Score)

    elif reponse<=operation1+10 and reponse>operation1+5:
        #print("Succès vous gagnez 5 points !")
        can1.after(0,affiche_image(cinqpts))
        can1.update()
        Score.set_score(5)
        actualise_score(Score)

    elif reponse<=operation1+5 and reponse>operation1:
        #print("Succès vous gagnez 10 points !")
        can1.after(0,affiche_image(dix))
        can1.update()
        Score.set_score(10)
        actualise_score(Score)

    elif reponse>=operation1-15 and reponse<operation1-10:
        #print("Succès vous gagnez 1 points !")
        can1.after(0,affiche_image(unpts))
        can1.update()
        Score.set_score(1)
        actualise_score(Score)
    
    elif reponse>=operation1-10 and reponse<operation1-5:
        #print("Succès vous gagnez 5 points !")
        can1.after(0,affiche_image(cinqpts))
        can1.update()
        Score.set_score(5)
        actualise_score(Score)
   
    elif reponse>=operation1-5 and reponse<operation1:
        #print("Succès vous gagnez 10 points !")
        can1.after(0,affiche_image(dix))
        can1.update()
        Score.set_score(10)
        actualise_score(Score)
    
    else:
        #print("Echec vous ne gagnez aucun points !")
        can1.after(1,affiche_image(zeropts))
        can1.update()
        Score.set_score(0)
        actualise_score(Score)


    
# ===================== FIN JEUX 1 / ECRAN AUTRE JEUX==========================

def fin_du_jeu():
    global Champ1,Labelscore,LabelResultat, LabelResultat2, LabelResultat3,LabelResultat4,pile_button,Score
    reset_pile_file(pile_button)
    can1.after(0,affiche_image(final))
    can1.update()
    
    Bouton_menu=bouton([985, 335],[1206, 409],"Menu",None,"menu()",None)
    pile_button.empiler(Bouton_menu)
    
    score1 = StringVar()
    
    Labelscore = Label(MaFenetre, textvariable = score1, bg ="white",font=("Courier",50),width=10,height=2)
    
    score1.set(Score.get_score())
    Labelscore.place(x=775, y=515)
    
    Score.ajouter_score()
    
    can1.update()
    
    set_score_online()
    

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
    

    
def est_bouton(lcoo:list, pile):
    '''On parcours la liste de bouton pour verifier si les axes X et Y où il y a eu le click,
    puis on regarde si cette zone est attribué à un bouton'''
    assert pile.vide() != True
    
    Pile2 = Pile()
    Pile_res = Pile()
    
    while pile.vide() != True :
        n = pile.depiler()
        Pile2.empiler(n)
        Pile_res.empiler(n)
    while Pile_res.vide() != True :
        m = Pile_res.depiler()
        pile_button.empiler(m)
    
    while Pile2.vide() != True:
        #print("taille de pile vaut : ", pile.taille())
        temp_memory = Pile2.depiler()
        #print(temp_memory.get_nom())
        if lcoo[0] > temp_memory.get_coo_min()[0]: #test 1 
            if lcoo[0] < temp_memory.get_coo_max()[0]: #test2
                if lcoo[1] > temp_memory.get_coo_min()[1]: # test 3
                    if lcoo[1] < temp_memory.get_coo_max()[1]: #test 4 
                        ''''puisque tous les test sont réussi, on peut afficher l'image qui est défini au bouton.
                        entre autre, on regarde le bouton que l'on testait, et puisque tout est bon, on prend l'image
                        de ce bouton et on l'affiche.'''
                        #print(temp_memory.get_nom())
                        exec(temp_memory.get_fonction())


def affiche_image(img):
    '''permet d'afficher une image sur la main-loop '''
    global can1, Bouton1, Bouton2, Bouton3, Bouton4, Bouton5, Bouton6, Bouton7,Bouton8, Bouton9, Bouton10, pile_button, bou1
    image_fond=can1.create_image(0,0,image=img,anchor="nw")

def random():
    rand=random.randint(0,1)
    return rand

def ajouter_mail():
    file = open("./doc_txt/mail_joueur.txt", 'w')
    file.write(str(mail_text.get()))
    file.close()
    insert_if_new_user()
    get_score_online()
    menu2()
    
def change_user():
    global mail_text_cu
    reset_pile_file(pile_button)
    
    can1.after(0, affiche_image(adresse_mail_image))

    mail_text_cu = Entry(MaFenetre, bg ="bisque", fg="maroon",font=("Courier",25),justify="center")
    mail_text_cu.focus_set()
    mail_text_cu.place(x=86,y=550,width=727, height=110)
    
    Bouton0 = bouton([909, 549], [1221, 658], "Bouton0", None, "change_user_next()", None)
    pile_button.empiler(Bouton0)

def change_user_next():
    file = open("./doc_txt/mail_joueur.txt", 'r')
    email_save=""
    for elt in file :
        email_save = email_save + elt
    file.close()
    
    file = open("./doc_txt/mail_joueur.txt", 'w')
    file.write(str(mail_text_cu.get()))
    file.close()
    
    if points_new_user(email_save) == True:
        menu2()
    else :
        mauvais_mail_function()

def mauvais_mail_function() :
    can1.after(0, affiche_image(mauvais_mail))
    can1.after(4000, menu2())

def Clique(event):
    '''Dans cette fonction, on récupère les coordonées où a eu lieu le clique puis on les stocks
    dans la liste l, pour pouvoir utilisé ces coordonées pour les comparées ect (#est_bouton)'''
    l=[] # Création de la liste pour tout stocker 
    abscisse=event.x #Récupération de l'abscisse 
    l.append(abscisse) #Ajout de la position en abscisse a la liste 
    ordonnee=event.y #Récupération de l'ordonnee
    l.append(ordonnee) #Ajout de la position en ordonnée a la liste
    est_bouton(l, pile_button) #Ici, on envoie la liste de coordonnéesainsi que la liste des boutons dans #est_boutons
    print(l)
    
# ============================== FONCTION LISTE ===============================

def affiche_but_pile_file(pile):
    '''renvoie le nom des boutons contenus dans une liste'''
    while pile.vide() != True:
        temp_memory = pile.depiler()
        #print(temp_memory.get_nom())

def reset_pile_file(pile):
    '''réinitialise la liste donner'''
    while pile.vide() != True:
        temp_memory = pile.depiler()

def supp_bou_liste(pile, bouton_sbl:str):
    '''supprime un bouton donner dans la liste donner'''
    Pile2 = Pile()
    while pile.vide() != True :
        temp_memory = pile.depiler()
        if temp_memory.get_nom() == str(bouton_sbl) :
            pass
        else:
            Pile2.empiler(temp_memory)
    while Pile2.vide() != True :
        temp_memory = Pile2.depiler()
        pile.empiler(temp_memory)

# ========================== LANCEMENT DU PROGRAMME ===========================


pile_button = Pile()

pile_supp = Pile() #pile supplémentaire
pile_supp_2 = Pile() #pile supplémentaire

# [['t'], ['i'], ['s'], ['f'], ['t'], ['s'], ['a'], ['i'], ['s'], ['a']] : facile 

can1=Canvas(MaFenetre,width=1280,height=720)
can1.place(x=0,y=0)

can1.focus_set()
can1.bind('<ButtonPress-1>', Clique)

menu()

MaFenetre.mainloop()