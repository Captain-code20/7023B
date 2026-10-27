import turtle

try:
	screen = turtle.Screen()
	screen.bgcolor("black")

	pen = turtle.Turtle()
	pen.speed(0)
	pen.pensize(2)
	pen.hideturtle()

	turtle.colormode(255)

	length = 50

	for i in range(36):
    
		r = (i * 7) % 255
		g = (i * 5) % 255
		b = 255 - (i * 5) % 255
		pen.color(r, g, b)

		for _ in range(3):
			pen.forward(length)
			pen.left(120)

		length = length + 5
		pen.left(10)

	turtle.done()

except Exception as e:
	print("ERRO")

    
