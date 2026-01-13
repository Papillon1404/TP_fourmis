class AntColony:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=2):
        """
        Initialise la colonie de fourmis.
        
        Paramètres :
        - distances : matrice des distances entre les villes
        - n_ants : nombre de fourmis par itération
        - n_best : nombre de meilleurs chemins qui déposent des phéromones
        - n_iterations : nombre d'itérations de l'algorithme
        - decay : taux d'évaporation des phéromones (entre 0 et 1)
        - alpha : importance des phéromones (α)
        - beta : importance de l'heuristique (β)
        """
        self.distances = distances
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

        self.meilleur_chemin = None
        self.meilleure_distance = m.inf

        n = len(distances)

        def calculer_distance_chemin(self, chemin) :

            d = 0
            for i in range(len(chemin)-1) :

                d +=  distances[chemin[i]][chemin[i+1]]

            return d
        
        def generer_tous_chemins(self) :

            chemin = [random.randint(0, len(self.distances) - 1)]
            while len(chemin) < len(self.distances):
                prochaines_probas = self.calculer_probabilites_mouvement(chemin)
                prochaine_ville = self.choisir_prochaine_ville(prochaines_probas)
                chemin.append(prochaine_ville)
        
            return (chemin, self.calculer_distance_chemin(chemin))

                    
        def calculer_probabilites_mouvement(self, chemin) :
            proba = []
            for i in range(n) :

                if n in chemin :
                    p = float(0)
                else :
                    pheromone = self.pheromones[i][chemin[-1]]
                    distance = self.distances[i][chemin[-1]]
                    
                    p = (pheromone**alpha)/(distance**beta)
                
                proba.append(p)
            return proba
        
        def choisir_ville_suivante(self, probabilites) :

            poid = probabilites
            
            return random.choices(range(n),weights = poid,k =1)[0]