
entraîneurs = {
    'Abdullah': [1, 1, 0, 0, 1],
    'Aamnah': [1, 1, 0, 1, 1],
    'Ibrahim': [1, 1, 1, 1, 0],
    'Amada': [1, 1, 1, 1, 1]
}
v = [1, 1, 1, 1, 1]

def selection(nom, v1, v):
    produit_scalaire = sum(a * b for a, b in zip(v1, v))
    if produit_scalaire < 4:
        print(nom, '- entraineur non selectionné')
    else:
        print(nom, "- entraineur preselectionné, qualité=", produit_scalaire, "/5")
for nom, vecteur in entraîneurs.items():
    selection(nom, vecteur, v)
