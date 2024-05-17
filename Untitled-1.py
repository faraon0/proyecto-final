


c = 1

asiento = [None] * 2
for i in range(0, 2):
    asiento[i] = [None] * 40

while( c <= 80): 
    
    fila = int(input("Favor ingr1esar el numero de fila (1-2)"))
    columna = int(input("Favor ingresar el numero de columna (1-40)"))

    if(asiento[fila - 1][columna -1]==0):
        asiento[fila - 1][columna -1] = 1
        c = c + 1
        print ("Reserva exitosa")
    else:
        print ("Asiento Ocupado")

print (asiento)