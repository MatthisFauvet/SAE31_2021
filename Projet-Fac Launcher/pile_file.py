# =============================================================================
# MODULE PILE / FILE TERMINAL NSI EX 6 
# =============================================================================

class Pile :
    #Creéation de la classe pile 
    
    def __init__(self):
        self.liste=[]
        
    def vide(self)->bool:
        #renvoie si la liste est vide ou remplie
        if self.liste == [] :
            return (True)
        else :
            return (False)
    
    def depiler(self):
        # c'est la fonction qui va dépiler le sommet si la liste est non vide
        if self.vide() == False :
            return(self.liste.pop())
        else :
            return(None)
    
    def empiler(self,x):
        #Empile x au sommet de la PILE
        self.liste.append(x)
    
    def sommet(self):
        #renvoie le somment de la pile, sans la dépilé
        return(self.liste[-1])
    
    
    def len_pile(self):
        #Affiche le nombre d'élément dans la pile
        return(len(self.liste))
    
    def Affichage(self):
        #Affiche les element de la liste (le sommet en haut) dans la console
        print(chr(8593)+chr(8595))
        for i in range(len(self.liste)):
            print(self.liste[-i-1])
            
                
    def taille(self):
        #renvoie le nombre d'elt que contient la pile
        return len(self.liste)


class File :
    #Creéation de la classe pile 
    
    def __init__(self):
        self.liste=[]
        
    def vide(self)->bool:
        #renvoie si la liste est vide ou remplie
        if self.liste == [] :
            return (True)
        else :
            return (False)
    
    def defiler(self):
        # c'est la fonction qui va dépiler le premier element de la liste si la liste est non vide
        if self.vide() == False :
            return(self.liste.pop(0))
        else :
            return(None)
    
    def enfiler(self,x):
        #Empile x a l'entrée de la file c'est a dire a la fin de la liste
        self.liste.append(x)
    
    def sommet(self):
        #renvoie l'élément rentré en premier 
        return(self.liste[0])
    
    def len_file(self):
        #Affiche le nombre d'élément dans la file
        return(len(self.liste))
    
    def Affichage(self):
        #Affiche les element de la liste de gauche a droite 
        print("-->", end=" ")
        for i in range(len(self.liste)):
            print(self.liste[-i-1], end="")
        print(" -->")