#Los ciclos para la programacion son secuenciales que permiten la realizacion o ejecucion de
#funciones para poder abreviar o automatizar codigo, esta el cilo for que sifnifica
#ciclo while que significa mientras que

print ("Tipo de programa que incluya un ciclo")

print ("----- Inicio del ciclo -----")

for i in range (10):
    print (i**2)

print ("finalize el ciclo")

#el programa que vamos a realizar tiene como fianlidad realizar un ciclo donde le pida al usuario 
#ingresar hasta tres numeros, es este caso la edad, y cuando genere la variable correcta
#ejecute en pantalla la siguiente accion, por ejemplo: digita tu numero de cedula, 3 digite si desea
#saber el numero de silla donde fue asignado
print ("admision de entrar")

Nombre = str (input ("Su Nombre:   "))
Edad = input ("Su edad:    ")

for Edad in range (18, 40):
    print (Edad-7)
print ("Esos son los asientos disponibles")

Edad = 18
if Edad > 18:
    print ("su asiento esta en la cuarta fila del numero 11 al 32")
else:
    print ("ubiquese en la primera fila o en los asientos sobrantes por ser un invitado especial")


Identifiacion = input ("Numero de identificacion:    ")



#listaEdades = [15, 16, 17, 18]


