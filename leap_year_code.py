#Code pyhton challenge
def is_leap(year):
    leap = False
    
    # Write your logic here
    #Si year modulo 4 rend 0 c'est une leap year
    if(year%4 == 0):
        #Si year modulo 100 rend 0 ce n'est pas une leap year
        if(year%100 == 0):
            #Si year modulo 400 rend 0 c'est une leap year
            if(year%400 == 0):
                leap = True
        else:
            leap = True
        
    

    return leap

year = int(raw_input())
print is_leap(year)

#Découverte des fonctions liés aux listes :
#Affiche toutes les coordonées [i,j,k] possibles jusqu'à i+j+k !=n et avec i<x etc.


if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    i = j = k = 0
    ma_liste = []
    #list comprehensive function 
    ma_liste = [ 
        [ i, j, k] 
        for i in range( x + 1) 
        for j in range( y + 1)
        for k in range ( z + 1) 
        if ( ( i + j + k ) != n )
    ] 

    
    print ma_liste
    
