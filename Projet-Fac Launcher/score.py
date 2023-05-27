class SCORE :
    
    def __init__(self, score):
        '''Création de score'''
        self.score = score 
    
    def set_score(self, n):
        '''On change la valeur de score'''
        self.score = self.score + n 
    
    def get_score(self):
        '''Renvoie la valeur de Score'''
        return(self.score)
    
    def ajouter_score(self):
        '''Ajoute le score dans un fichier texte'''
        
        file = open("./doc_txt/score.txt", 'r')
        score = ""
        for elt in file :
            score = score + elt
        if score == '' :
            file.close()
            file = open("./doc_txt/score.txt", 'w')
            file.write(str(0))
            file.close()
            self.ajouter_score()
        else :
            file.close()
            file = open("./doc_txt/score.txt", 'w')
            file.write(str(int(score)+int(self.get_score())))
            file.close()
        return True
