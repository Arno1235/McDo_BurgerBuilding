import pyautogui
import time

def Mouse_Start():
    pyautogui.click(940, 973)
    #pyautogui.dragTo(200, 307, 0.2, button='left')

def Mouse_End():
    pyautogui.click(1068, 97)

def Swipe(height):
    pyautogui.moveTo(1065, height)
    pyautogui.dragTo(600, height, 0.02, button='left')
    
def Swipe1():
    pyautogui.moveTo(928, 83)
    pyautogui.dragTo(500, 83, 0.02, button='left')
    #Die 0.11 is de tijd in sec dat die swipe duurt, als ge sneller wilt gaan kunt ge dit dus aanpassen.
    #Maar als ik hem sneller zet werkt het niet meer.
    

if __name__ == "__main__":
    
    time.sleep(5)
    Mouse_Start()
    time.sleep(10.3)
    Mouse_Start()
    Mouse_Start()
    time.sleep(1.2)
    
    Swipe1()
    Swipe(183)
    Swipe(183)
    Swipe(183)
    Swipe(269)
    Swipe(269)
    Swipe(269)
    time.sleep(delay)
    Swipe(356)
    time.sleep(delay)
    Swipe(356)
    time.sleep(delay)
    Swipe(451)
    
    time.sleep(delay)
    
    Swipe(644)
    time.sleep(delay)
    Swipe(735)
    time.sleep(delay)
    Swipe(830)
    time.sleep(delay)
    Swipe(830)
    time.sleep(delay)
    Swipe(920)
    time.sleep(delay)
    Swipe(1014)
    time.sleep(delay)
    Swipe(1014)
    time.sleep(delay)
    Swipe(1014)
    
    Mouse_End()
        
        
        
        
        
        
