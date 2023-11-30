import turtle

tu = turtle.Turtle()
tu.screen.bgcolor("black")
tu.pensize(2)
tu.color("green")
tu.left(90)
tu.backward(100)
tu.shape('turtle')

def tree(i):
    tu.speed(50)
    if i < 10:
        return
    else:
        tu.forward(i)
        tu.color("orange")
        tu.circle(2)
        tu.color("brown")
        tu.left(30)
        tree(3 * i / 4)
        tu.right(60)
        tree(3 * i / 4)
        tu.left(30)
        tu.backward(i)

tree(100)

# Dibujar mensaje letra por letra
tu.shape('classic')
tu.left(270)
tu.speed(1)
tu.penup()
tu.goto(-215, -150)
tu.color("white")

mensaje = "Čestitke za tvoj uspjeh, Tea:)"

# Puedes ajustar estos valores según tus necesidades
ancho_letras = {"t":9,"j":6, "i": 6, "l": 6, "o": 12, "default": 10}
espacio_entre_letras = 1.5

for letra in mensaje:
    ancho = ancho_letras.get(letra.lower(), ancho_letras["default"])
    tu.write(letra, align="left", font=("Arial", 16, "normal"))
    tu.forward(ancho * espacio_entre_letras)
turtle.done()