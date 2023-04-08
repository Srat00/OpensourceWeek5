from Week5_902_Module import *
import turtle

inputString = ''
sWidth, sHeight = 300, 300
tX, tY, tAngle, tSize = [0] * 4

turtle.title('TUTEL!!')
turtle.shape('turtle')
turtle.setup(width = sWidth + 50, height = sHeight + 50)
turtle.screensize(sWidth, sHeight)
turtle.penup()
turtle.speed(5)

inputString = getString()

for ch in inputString:
    tX, tY, tAngle, tSize = getXYAS(sWidth, sHeight)
    r, g, b = getRGB()
    
    turtle.goto(tX, tY)
    turtle.setheading(tAngle)
    
    turtle.pencolor(r, g, b)
    turtle.write(ch, font = ('맑은고딕', tSize, 'bold'))

turtle.done()