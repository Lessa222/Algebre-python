v1 = [1 ,1 ,3 ,14 ,18 ,21 ,25 ,35 ,55]
v2 = [[1 ],[2] ,[5 ],[12] ,[17 ],[26 ],[29] ,[33] ,[59]]
def norme(u):
    for i in range(len(u)):
        w = (sum(u[i]**2))**(1/2) 
        print("norme du vecteur",u ,"=" , w)

def produit_ligne_colonne(u,v):
    return sum(u[i]* v[i][0] for i in range(len(u)))
resultat1 = produit_ligne_colonne(v1 ,v2)
print ("v1 * v2 =" , resultat1)

def colonne_ligne(u,v):
    matrice = []
    for i in range(len(v)):
            ligne = []
            for j in range(len(u)):
                ligne.append(v[i][0]*u[j])
            matrice.append(ligne)
    return matrice
resultat2 = colonne_ligne(v2 ,v1)
norme(v1)




