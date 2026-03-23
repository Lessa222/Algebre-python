
def multiplier(A, B):
   
    n = len(A) 

    C = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

    
    for i in range(n):

        
        for j in range(n):
            somme = 0
            for k in range(n):
                somme = somme + A[i][k] * B[k][j]
            C[i][j] = somme
    return C
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
P = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
D = multiplier(P, A)
print("\n matrice A")
print(f"{A[0]}\n{A[1]}\n{A[2]}")
print("\n permutation colonne de A")
print(f"{D[0]}\n{D[1]}\n{D[2]}")
F= multiplier(D,P)
print("\n permutation colonne et ligne  de A")
print(f"{F[0]}\n{F[1]}\n{F[2]}")




