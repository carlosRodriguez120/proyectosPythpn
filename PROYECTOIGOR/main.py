import cv2
import pytesseract
from gtts import gTTS
import numpy as np
import turtle
from turtle import forward, right, onkeypress, listen, bye, done


def iniciar_lab(nivel):
    for fila in range(len(nivel)):
        for columna in range(len(nivel[fila])):

            caracter = nivel[fila][columna]
            ejeX = -288 + (columna * 23)
            ejeY = 288 - (fila * 23)

            if caracter == 3 or caracter == '3':
                bloques.color("yellow")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == 0 or caracter == '0':
                bloques.color("white")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == -1 or caracter == "x":
                bloques.color("green")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == "B":
                bloques.color("red")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()
            elif caracter == 1 or caracter == '1':
                bloques.color("black")
                bloques.goto(ejeX, ejeY)
                bloques.stamp()


wn = turtle.Screen()
wn.bgcolor("blue")  # Agregando color a la pantalla
wn.title("LABERINTO")  # Poniendo titulo
wn.setup(700, 700)  # Creando tamaño a la ventana


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.shape("square")  # Poniendo la forma
        self.color("white")  # Poniendo color al laberinto
        self.color("")  # Poniendo color al laberinto
        self.penup()
        self.speed(0)


bloques = Pen()


def imp(laberinto):
    for x in laberinto:
        for y in x:
            print("", y, "", end="")
        print()


cuadro = 100
anchocam, altocam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, anchocam)
cap.set(4, altocam)

matriz = []


def text(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texto = pytesseract.image_to_string(gris)
    texto = texto.replace('\n\n', '\n')
    texto = texto.replace('1', '1,', )
    texto = texto.replace('0', '0,', )
    texto = texto.replace('3', '3,', )
    texto = texto.replace(',\n', '\n')
    texto = texto.split('\n')

    for t in texto:
        if len(t) > 0:
            print(t.split(','))
            matriz.append(t.split(','))

    print(matriz)
    dire = open('Info.txt', "w")
    dire.write(f'matriz')
    imp(matriz)
    iniciar_lab(matriz)
    pen = Pen()
    dire.close()


while True:
    ret, frame = cap.read()
    if ret == False: break
    cv2.putText(frame, 'Ubique aqui la matriz', (158, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 255, 0), 2)
    cv2.putText(frame, 'Ubique aqui la matriz', (160, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.rectangle(frame, (cuadro, cuadro), (anchocam - cuadro, altocam - cuadro), (0, 0, 0), 2)
    x1, y1 = cuadro, cuadro
    ancho, alto = (anchocam - cuadro) - x1, (altocam - cuadro) - y1
    x2, y2 = x1 + ancho, y1 + alto
    doc = frame[y1:y2, x1:x2]
    cv2.imwrite("Imatext.jpg", doc)

    cv2.imshow("Lector Inteligente", frame)
    t = cv2.waitKey(1)
    if t == 13:
        break

text(doc)
cap.release()
cv2.destroyAllWindows()

print(type(matriz))


def recorrido(i, j):
    if int(matriz[i][j]) == 3:
        return [(i, j)]

    if int(matriz[i][j]) == 1:
        return []

    matriz[i][j] = -1

    if (i > 0) and matriz[i - 1][j] in [0, 3]:  # arriba
        camino = recorrido(i - 1, j)
        if camino: return [(i, j)] + camino

    if j < len(matriz[i]) - 1 and int(matriz[i][j + 1]) in [0, 3]:  # para la derecha
        camino = recorrido(i, j + 1)
        if camino: return [(i, j)] + camino

    if i < len(matriz) - 1 and matriz[i + 1][j] in [0, 3]:  # para abajo
        camino = recorrido(i + 1, j)
        if camino: return [(i, j)] + camino

    if j > 0 and matriz[i][j - 1] in [0, 3]:  # para la izquierda
        camino = recorrido(i, j - 1)
        if camino: return [(i, j)] + camino

    matriz[i][j] = "B"
    return []


for x in recorrido(0, 0):
    print(f" {x} ")

imp(matriz)
iniciar_lab(matriz)
pen1 = Pen()

turtle.onkeypress(bye, 'q')
turtle.listen()
done()
