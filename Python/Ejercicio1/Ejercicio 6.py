#Este programa va tener como finalidad mezclar varios elementos que pueda solicitar el usuario o
#Vamos a colo diferentes  metodos para poder realizar actividades simples o secuenciales
#del mismo modo perimitira realizar salidas de informacion sujetas a condiciones logicas

print ("----------------------------------------------Inicio del programa----------------------------------------------")

Edad1 = int (input ("¿Cual es su edad?"))

if Edad1 < 18:
    print ("Eres menor de edad")
else:
    print ("Eres mayor de edad")

print ("---------------------------Modulo de seguridad---------------------------------")

#Aca el usuario una vez se establece si es mayor de edad, le vamos a solicitar una contraseña


print("Su contraseña fue enviada exitoasametne en su correo")

ClaveMayorEdad = "contraseña1"
password = input ("Ingrese la contraseña que fue enviada a su correo")
if ClaveMayorEdad == password.lower ():
    print ("Contraseña o password correcto")
else:
    print ("Contraseña incorrecta")

    print ("Revise su contraseña e intente de nuevo")

print ("----------------------------------------------- modulo 3v de interaccion----------------------------------------------------")

print ("Escriba una frase o palabra para seguir adelante en la autenticacion")

frase = input ("Introduce")

#Si se desea reemplzar la contraseña, solicite al usuario escribir en diuferentes letras o numeros
#la nueva contraseña o simplemente o simplemente solicite un parametro de validacion

vocal = input ("Introduzca una vocal en minuscula")
#Escriba animal para ingresar su animal favorito
if frase.lower() == "animal":
    animal = input ("Agregue su animal favorito    ")
    print ("buena eleccion")

print ("Usted a completado los tres modulos de autencticacion")