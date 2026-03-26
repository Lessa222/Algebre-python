import random
S = [[1, 2, 3, 4, 5],
     [5, 6, 8, 7, 4],
     [5, 7, 9, 9, 8],
     [8, 9, 7, 5, 4]]
v1 = [S[i][0] for i in range(4)]
v2 = [S[i][1] for i in range(4)]
v3 = [S[i][2] for i in range(4)]
v4 = [S[i][3] for i in range(4)]
v5 = [S[i][4] for i in range(4)]
print(v1)
def aleatoire(indices):
    colonne=random.sample(indices, 4)
    vecteurs=[[S[i][j] for i in range(4)] for j in colonne]
    return [[vecteurs[j][i] for j in range(4)] for i in range(4)]  # transpose to make it rows

def det(mat):
    if len(mat)==2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    determinant =0
    for c in range(len(mat)):
        smat=[d[:c]+ d[c+1:] for d in mat[1:]]
        determinant += ((-1)**c)*mat[0][c] * det(smat)
    return determinant

indices = list(range(5))
A = None
while True:
    A = aleatoire(indices)
    F = det(A)
    if F != 0:
        break
print("Matrice trouvée avec déterminant non nul:", F)
print(A)

import numpy as np

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Valeurs propres:")
print(eigenvalues)

print("Vecteurs propres:")
print(eigenvectors)

# Décomposition spectrale
print("\nDécomposition spectrale de la matrice A:")
print("A = P * D * P^(-1)")
print("où P est la matrice des vecteurs propres (colonnes),")
print("et D est la matrice diagonale des valeurs propres.")

P = eigenvectors
D = np.diag(eigenvalues)
P_inv = np.linalg.inv(P)

print("\nMatrice P (vecteurs propres en colonnes):")
print(P)
print("\nMatrice D (diagonale des valeurs propres):")
print(D)
print("\nMatrice P^(-1):")
print(P_inv)

# Vérification
A_reconstructed = P @ D @ P_inv
print("\nVérification: P * D * P^(-1) ≈ A")
print("Différence maximale avec A originale:", np.max(np.abs(A_reconstructed - np.array(A))))








