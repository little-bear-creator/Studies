string = "alancurkebenjamin"

print("Le char de 3 à 5 : "+string[3::5])
print("Le char de 3 à 3 : "+string[3::3])
print("Longueur du string : "+str(len(string)))
# string[n::] commence à partir de n, n est donc inclus au string
print("Longueur à partir de 10 : "+str(len(string[10::])))
print("Longueur à partir de 0 : "+str(len(string[0::])))
print("Le char du début avec 3::3 : "+string[3::3])
