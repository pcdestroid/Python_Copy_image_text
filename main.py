# Purpose: Select an area of ​​the image that has text and copies the text.
# Objetivo: Selecionar uma área da imagem que tenha um texto e copia o texto.
import win32api, keyboard, mss, pytesseract, screendraw, cv2
import mss.tools

#point to the location where pytesseract.exe was installed
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

#Turning negative numbers into positive numbers

def abs(x):
    if x < 0 : x = -x
    return x

#Detects mouse click
def mouseClick():
    if win32api.GetKeyState(0x01) < 0 : mouse_click = True
    else : mouse_click = False
    return mouse_click

old_state = win32api.GetKeyState(0x01)
xStartPosition = 0 #pega posição x do mouse
yStartPosition = 0 #pega posição y do mouse
mouse_click = False
printscreen = False

while True:
    xCurrentPosition = screendraw.getMousePosition()[0] #pega a nova posição x do mouse
    yCurrentPosition = screendraw.getMousePosition()[1] #pega a nova posição y do mouse

    #Altera a posição inicial do mouse quando clicar
    new_state = win32api.GetKeyState(0x01) #pega status atual do botao esquerdo do mouse
    if new_state != old_state:
            old_state = new_state
            if new_state < 0:
                xStartPosition = xCurrentPosition
                yStartPosition = yCurrentPosition
            else:
                if printscreen:
                    with mss.mss() as sct:
                        left = xStartPosition
                        top = yStartPosition
                        if xStartPosition>xCurrentPosition:
                            left = xCurrentPosition
                        if yStartPosition > yCurrentPosition:
                            top = yCurrentPosition
                        monitor = {"top": top, "left": left, "width": abs(xCurrentPosition - xStartPosition), "height": abs(yCurrentPosition - yStartPosition)}
                        output = "imagem.png".format(**monitor)
                        sct_img = sct.grab(monitor)
                        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                        #Recognize text from image
                        resultado = pytesseract.image_to_string(cv2.imread('imagem.png')).lower()
                        print(resultado)
    
    printscreen = keyboard.is_pressed('ctrl') and mouseClick()
    if printscreen:
        screendraw.createRectangle(xStartPosition,yStartPosition)

    
    
