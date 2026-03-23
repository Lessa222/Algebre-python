vecteur1 = []
vecteur2 = []
for i in range(10):
    val = float(input(f"valeur {i+1} :"))
    vecteur1.append(val)
for i in range(10):
    val = float(input(f"valeur {i+1} :"))
    vecteur2.append(val)
p = 0
for i in range(10):
    p=vecteur1[i]*vecteur2[i]+p
print("\n A * B =" , p)
