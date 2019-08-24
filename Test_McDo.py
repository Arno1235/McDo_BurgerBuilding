import numpy as np
import pyautogui
import time

def Mouse_Start():
    pyautogui.click(940, 973)
    #pyautogui.dragTo(200, 307, 0.2, button='left')

def Mouse_End():
    pyautogui.click(1068, 97)

def Swipe(height):
    pyautogui.moveTo(1065, height)
    pyautogui.dragTo(600, height, 0.1, button='left')
    
def Swipe1():
    pyautogui.moveTo(928, 83)
    pyautogui.dragTo(500, 83, 0.1, button='left')
    

if __name__ == "__main__":
    
    time.sleep(5)
    Mouse_Start()
    time.sleep(10.1)
    Mouse_Start()
    Mouse_Start()
    time.sleep(0.7)
    
    Swipe1()
    Swipe(183)
    Swipe(183)
    Swipe(183)
    Swipe(269)
    Swipe(269)
    Swipe(269)
    Swipe(356)
    Swipe(356)
    Swipe(451)
    
    Swipe(644)
    Swipe(735)
    Swipe(819)
    Swipe(819)
    Swipe(920)
    Swipe(1014)
    Swipe(1014)
    Swipe(1014)
    
    Mouse_End()
        
        
        
        
        
        
