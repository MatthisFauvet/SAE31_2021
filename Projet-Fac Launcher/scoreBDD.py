# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:43:08 2022

@author: Matthis
"""

""" Programme qui permet d'envoyer des informations concernant le score des joueurs a un base de données """


import mysql.connector as mc

def insert_if_new_user():
    '''Fonction qui permet d'insérer une ligne dans la table resultats de la bdd
    si l'utilisateur est nouveau'''
    
    file = open("./doc_txt/mail_joueur.txt", 'r')
    email = ""
    for elt in file :
        email = email + elt
    file.close()
    
    try :
        set_coo = mc.connect(host = 'sql11.freemysqlhosting.net', database = 'sql11495727', user = 'sql11495727', password = 'Gs3xDigIDv')
        cursor = set_coo.cursor()
        
        req = 'SELECT mail_joueur FROM resultats WHERE mail_joueur = "'+str(email)+'";'
        rep = cursor.execute(req)
        
        mail = cursor.fetchall()
        
        if mail == [] :
            req2 = 'INSERT INTO resultats (id_score, mail_joueur, score) VALUES (0,"'+str(email)+'", 0);'
            cursor.execute(req2)
            
            
    except mc.Error as err:
        print(err)




def set_score_online() :
    
    file = open("./doc_txt/mail_joueur.txt", 'r')
    email = ""
    for elt in file :
        email = email + elt
    file.close()
    
    file = open("./doc_txt/score.txt", 'r')
    score = ""
    for elt in file :
        score = score + elt  
    
    try :
        set_coo = mc.connect(host = 'sql11.freemysqlhosting.net', database = 'sql11495727', user = 'sql11495727', password = 'Gs3xDigIDv')
        cursor = set_coo.cursor()
        
        req = 'SELECT mail_joueur FROM resultats WHERE mail_joueur = "'+str(email)+'";'
        rep = cursor.execute(req)
        
        mail = cursor.fetchall()
        
        if mail == "[]" :
    
            req = 'INSERT INTO resultats (id_score, mail_joueur, score) VALUES (0,"'+email+'", 0);'
            cursor.execute(req)
            
        else :
            req = 'UPDATE resultats SET score = "'+str(score)+'" WHERE mail_joueur = "'+email+'";'
            cursor.execute(req)
        
        file.close()
            
    except mc.Error as err:
     	print(err)
         
         
         
def get_score_online() :
    file = open("./doc_txt/mail_joueur.txt", 'r')
    email=''
    for elt in file :
        email = email + elt
    file.close()
    
    file = open("./doc_txt/score.txt", 'r')
    file_score = ""
    for elt in file :
        file_score = file_score + elt
    file.close()
    
    try :
        set_coo = mc.connect(host = 'sql11.freemysqlhosting.net', database = 'sql11495727', user = 'sql11495727', password = 'Gs3xDigIDv')
        cursor = set_coo.cursor()
        
        req = 'SELECT score FROM resultats WHERE mail_joueur = "'+str(email)+'";'
        rep = cursor.execute(req)
        
        online_score = cursor.fetchall()
        online_score_integer = online_score[0][0]
        # print(online_score_integer)
        
        if int(online_score_integer) > int(file_score) :
            file = open("./doc_txt/score.txt", 'w')
            file.write(str(online_score_integer))
        
        else :
            pass
        
    except mc.Error as err :
        print(err)

def points_new_user(n:str) :
    file = open("./doc_txt/mail_joueur.txt", 'r')
    email=''
    for elt in file :
        email = email + elt
    file.close()
    
    file = open("./doc_txt/score.txt", 'r')
    file_score = ""
    for elt in file :
        file_score = file_score + elt
    file.close()
    
    try :
        set_coo = mc.connect(host = 'sql11.freemysqlhosting.net', database = 'sql11495727', user = 'sql11495727', password = 'Gs3xDigIDv')
        cursor = set_coo.cursor()
        
        req0 = 'SELECT mail FROM compte WHERE mail = "'+str(email)+'";'
        rep0 = cursor.execute(req0)
        
        answ0 = cursor.fetchall()
        
        if answ0 == [] :
            file = open("./doc_txt/mail_joueur.txt", 'w')
            file.write(n)
            file.close()
            return False
        
        else :
            req = 'SELECT score FROM resultats WHERE mail_joueur = "'+str(email)+'";'
            rep = cursor.execute(req)
            
            online_score = cursor.fetchall()
            online_score_integer = online_score[0][0]
            
            file = open("./doc_txt/score.txt", 'w')
            file.write(str(online_score_integer))
            return True
                
        
    except mc.Error as err :  
        print(err)
    
    