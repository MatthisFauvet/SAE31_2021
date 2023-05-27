class bouton :
    
    def __init__(self, coo_min, coo_max, nom, image, fonction, lettre):
        '''Fonction qui défini tous les arguments requis pour creer un objet de type #bouton '''
        self.coo_max = coo_max #coordonnées max en x et y, soit le côté gauche en haut du bouton 
        self.coo_min = coo_min #de meme pour côté droite bas
        self.image = image #On stock l'image du bouton, ce qu'il devra afficher à son activation
        self.nom = nom #On definit a qu'elle jeu il appartient pour bienn se souvenir 
        self.fonction = fonction #Permettera d'attribuer une fonction
        self.lettre = lettre
    
    def get_zone(self):
        '''renvoie la zone dans la quelle le boutton est actif '''
        return(str(self.coo_min)+ str(self.coo_max))
    
    def get_coo_min(self):
        '''renvoie les coo minimal, le coin supérieur gauche'''
        return(self.coo_min)
    
    def get_coo_max(self):
        '''Renvoie les coos du coin inférieurs bas'''
        return(self.coo_max)
    
    
    
    def get_nom(self):
        return(self.nom)
    
    def get_image(self):
        '''Renvoie l'image du bouton, ce qu'il affichera quand on appuiera dessus '''
        return(self.image)
    
    def get_lettre(self):
        return (self.lettre)
    
    
    
    def get_fonction(self):
        '''Renvoie la fonction du bouton, celle qu'il lancera quand on cliquera dessus' '''
        return(self.fonction)
    
    

    def str(self):
        '''commande magique de texte'''
        print("JEUX :" + str(self.jeux) + '\n' + "ZONE D'ACTION :" + str(self.get_zone()))
