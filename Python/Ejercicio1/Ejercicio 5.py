#Vamos a realizar secuencias con condiciones basadas en ciclos
x = ("d")
y = ("l")
z = ("p")
a= ("agua")
g = ("gato")
o = 2*2+4 
f = ("5")
c = ("0")
s = ("1+1")
t = ("7")
#list [ "10", "B", "gato", "casa", x, y, z, ]
#print (list)


#list = [ "x", "y", "z", "a", "g", "o", "f", "c", "s", "t" ]
#print (list [0:3])

#list = [ "x", "y", "z", "a", "g", "o", "f", "c", "s", "t" ]
#print (list *2)

       
#list = [ "x", "y", "z", "a", "g", "o", "f", "c", "s", "t" ]
#print (list [0:3] *2)

#list = [ "x", "y", "z", "a", "1", "o", "5", "0", "s", "t", ]
#list.append ("EAN")
#list.index ("EAN")
#list.remove ("y")
#list.sort ()
#list.reverse ()
#list.copy ("0", "1", "5")
#print (list )

lista1 = str ()
list = [ "a", "b", "c", "d", "e", "0", "1", "4", "5", "7", "l", "d", "j", "p", "g", "9", "EAN"]
list.append ("EAN")
list.index ("EAN")
list.remove ("e")
list.sort ()
list.reverse ()
list.copy ()

print (list )

print ("elementos de 0 a 10")

list2 = list.copy () 
list.append ("EAN")
list.index ("EAN")
list.remove ("e")
list.sort ()
list.reverse ()
list.copy ()
print (list2 [0:10] )
print ("multiplicado")

list2 = list.copy () 
list.append ("")
list.index ("EAN")
list.remove ("e")
list.sort ()
list.reverse ()
list.copy ()
print (list2 *2 )