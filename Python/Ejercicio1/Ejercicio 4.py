#Vamos a crear un código que realice  por pantalla un calculo de variables, que nos permita sumar
#restar y hacer operaciones para mostrar al final un resultado de cada operacion y a su vez crear una tabla de
#la verdad y cada una de las operaciones usando "bool o usando and y or"

print ("Este programa no se puede hacer por chat gpt el que lo haga le bajo nota")

d = input ("Deme un número en pantalla     ")
l = input ("Inserte un número mayor al anterior       ")


d = int(d)
l = int(l)

print (d+l)
print (d-l)
print (d*l)
print (d/l)
print (d%l)
#conjuncion
print ("Tabla de la verdad todo lo relacionado con and o Y")
print ((str(d==d)) + "and" + str (d==d) + "--->" + str (d==d))
print ((str(d==d)) + "and" + str (d==l) + "--->" + str (d==l))

print ((str(l==d))+ "and" + str (d==d) + "--->" + str (d==l))
print ((str (d==l))+ "and" + str (l==d) + "--->" + str (l==d))

#Disyuncion
print ((str(d==d)) + "o" + str (d==d) + "--->" + str (d==d))
print ((str(d==d)) + "o" + str (d==l) + "--->" + str (d==d))

print ((str(l==d))+ "o" + str (d==d) + "--->" + str (l==l))
print ((str (l==d))+ "o" + str (d==l) + "--->" + str (d==l))