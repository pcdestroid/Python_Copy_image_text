# Purpose: Select an area of ​​the image that has text and copies the text.
# Objetivo: Selecionar uma área da imagem que tenha um texto e copia o texto.
import win32api
import keyboard
from mss import mss
import mss
import mss.tools
import screendraw
import pytesseract
import cv2

#apontar o local onde foi instalado o pytesseract.exe
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

# Transformar números negativos em números positivos
def normaliza(x):
    if x<0:
        x=-x
    return x

# Detecta clique do mouse
def mouseClick():
    if win32api.GetKeyState(0x01) < 0:
        mouse_click = True
    else:
        mouse_click = False
    return mouse_click

state_left = win32api.GetKeyState(0x01)
xStartPosition = 0 #pega posição x do mouse
yStartPosition = 0 #pega posição y do mouse
mouse_click = False
printscreen = False

while True:    
    xCurrentPosition = screendraw.getMousePosition()[0] #pega a nova posição x do mouse
    yCurrentPosition = screendraw.getMousePosition()[1] #pega a nova posição y do mouse

    #Altera a posição inicial do mouse quando clicar
    new_state = win32api.GetKeyState(0x01) #pega status atual do botao esquerdo do mouse
    if new_state != state_left:
            state_left = new_state
            if new_state < 0:
                xStartPosition = xCurrentPosition
                yStartPosition = yCurrentPosition
            else:
                if printscreen == True:
                    with mss.mss() as sct:
                        left = xStartPosition
                        top = yStartPosition
                        if xStartPosition>xCurrentPosition:
                            left = xCurrentPosition
                        if yStartPosition > yCurrentPosition:
                            top = yCurrentPosition
                        monitor = {"top": top, "left": left, "width": normaliza(xCurrentPosition - xStartPosition), "height": normaliza(yCurrentPosition - yStartPosition)}
                        output = "imagem.png".format(**monitor)
                        sct_img = sct.grab(monitor)
                        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                        printscreen = False
                        #ler a imagem com opencv
                        resultado = pytesseract.image_to_string(cv2.imread('imagem.png')).lower()
                        print(resultado)

    if keyboard.is_pressed('ctrl') == True:
        if mouseClick() == True:
            printscreen = True
            screendraw.createRectangle(xStartPosition,yStartPosition)
    
    
