def sont_orthogonaux(v1, v2):
    if len(v1) != len(v2):
        return "Erreur : les vecteurs doivent avoir la même taille."
   
    produit_scalaire = sum(a * b for a, b in zip(v1, v2))
    return produit_scalaire == 0   

v1 = list(map(float, input("Entrez les coordonnées du premier vecteur (séparées par des espaces) : ").split()))
v2 = list(map(float, input("Entrez les coordonnées du deuxième vecteur : ").split()))


resultat = sont_orthogonaux(v1, v2)
print(resultat)

                           

