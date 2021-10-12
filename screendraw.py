
# install library - https://pypi.org/project/win32gui/
# pip install win32gui

import win32gui
import pyautogui

#Function to return mouse positions
def getMousePosition():
    x, y = pyautogui.position()
    return x,y

#Function to draw a rectangle on the screen as the mouse moves
def createRectangle(xStartPosition,yStartPosition): #put mouse position
    #Get the graphical context to the Desktop
    xCurrentPosition, yCurrentPosition = pyautogui.position()
    dc = win32gui.GetDC(0)
    #draw top line
    win32gui.MoveToEx(dc,xStartPosition,yStartPosition)
    win32gui.LineTo(dc,xCurrentPosition,yStartPosition)
    #draw left line
    win32gui.MoveToEx(dc,xStartPosition,yStartPosition)
    win32gui.LineTo(dc,xStartPosition,yCurrentPosition)
    #draw bottom line
    win32gui.MoveToEx(dc,xCurrentPosition,yCurrentPosition)
    win32gui.LineTo(dc,xStartPosition,yCurrentPosition)
    #draw right line
    win32gui.MoveToEx(dc,xCurrentPosition,yCurrentPosition)
    win32gui.LineTo(dc,xCurrentPosition,yStartPosition)