import turtle

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("white")
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

# Paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("white")
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(40)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.3
pelota.dy = 0.3

# Funciones para mover las paletas hacia arriba y abajo
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    if y < 250:
        y += 20
    paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    if y > -240:
        y -= 20
    paleta_izquierda.sety(y)

def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    if y < 250:
        y += 20
    paleta_derecha.sety(y)

def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    if y > -240:
        y -= 20
    paleta_derecha.sety(y)

# Teclado
wn.listen()
wn.onkeypress(paleta_izquierda_arriba, "w")
wn.onkeypress(paleta_izquierda_abajo, "s")
wn.onkeypress(paleta_derecha_arriba, "Up")
wn.onkeypress(paleta_derecha_abajo, "Down")

# Función para detener el juego
def detener_juego():
    global juego_activo
    juego_activo = False

# Tecla para detener el juego
wn.onkeypress(detener_juego, "q")

# Marcador
marcador_izquierda = 0
marcador_derecha = 0

marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador 1: 0 Jugador 2: 0", align="center", font=("Courier", 24, "normal"))

# Bucle principal del juego
juego_activo = True
while juego_activo:
    wn.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Comprobar colisiones con los bordes superior e inferior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Comprobar colisiones con las paletas
    if (pelota.dx > 0) and (350 > pelota.xcor() > 340) and (paleta_derecha.ycor() + 50 > pelota.ycor() > paleta_derecha.ycor() - 50):
        pelota.color("blue")
        pelota.setx(340)
        pelota.dx *= -1

    elif (pelota.dx < 0) and (-350 < pelota.xcor() < -340) and (paleta_izquierda.ycor() + 50 > pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.color("red")
        pelota.setx(-340)
        pelota.dx *= -1

    # Comprobar si la pelota sale de la pantalla
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador_izquierda += 1
        marcador.clear()
        marcador.write("Jugador 1: {} Jugador 2: {}".format(marcador_izquierda, marcador_derecha), align="center", font=("Courier", 24, "normal"))

    elif pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador_derecha += 1
        marcador.clear()
        marcador.write("Jugador 1: {} Jugador 2: {}".format(marcador_izquierda, marcador_derecha), align="center", font=("Courier", 24, "normal"))

# Mostrar el resultado final
marcador.goto(0, 0)
marcador.write("¡Fin del juego!", align="center", font=("Courier", 36, "normal"))
turtle.done()