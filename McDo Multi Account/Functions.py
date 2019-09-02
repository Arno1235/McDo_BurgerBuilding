#@

import pyautogui
import time

Accounts = ["yeus2","yeus2"]
Passwords = ["Yeusyeus1"]

def LogIn(Acc):
    global Accounts
    global Passwords
    
    pyautogui.click(693, 118)
    time.sleep(1)
    pyautogui.click(784, 542)
    time.sleep(1)
    pyautogui.click(755, 212)
    time.sleep(1)
    pyautogui.typewrite(Accounts[Acc])
    pyautogui.hotkey('ctrl','v')
    pyautogui.typewrite("gmail.com")
    time.sleep(1)
    pyautogui.click(806, 302)
    time.sleep(1)
    pyautogui.typewrite(Passwords[0])
    time.sleep(1)
    pyautogui.click(938, 438)
    time.sleep(2)
    pyautogui.click(695, 125)

def LogUit():
    pyautogui.click(693, 118)
    time.sleep(1)
    pyautogui.click(784, 542)
    time.sleep(2)
    pyautogui.click(957, 987)
    time.sleep(1)
    pyautogui.click(1114, 722)
    time.sleep(3)
    pyautogui.click(693, 118)
    time.sleep(3)
    
def Prepare():
    pyautogui.click(949, 442)
    time.sleep(6)
    pyautogui.click(933, 853)
    time.sleep(4)
    pyautogui.click(695, 719)
    time.sleep(1)
    pyautogui.click(926, 891)
    time.sleep(4)

def End():
    pyautogui.click(690, 90)
    time.sleep(1)
    pyautogui.click(697, 120)

def Mouse_Start():
    pyautogui.click(940, 973)

def Mouse_End():
    pyautogui.click(1068, 97)

def Swipe(height):
    pyautogui.moveTo(1065, height)
    pyautogui.dragTo(600, height, 0.08, button='left')
    
def Swipe1():
    pyautogui.moveTo(928, 83)
    pyautogui.dragTo(500, 83, 0.08, button='left')

def Build():
    time.sleep(5)
    Mouse_Start()
    time.sleep(10.4)
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
    Swipe(356)
    Swipe(356)
    Swipe(451)
    
    Swipe(644)
    Swipe(735)
    Swipe(830)
    Swipe(830)
    Swipe(920)
    Swipe(1014)
    Swipe(1014)
    Swipe(1014)
    
    Mouse_End()
    
if __name__ == "__main__":
    time.sleep(5)
    for i in range(0,1):
        LogIn(i)
        time.sleep(5)
        Prepare()
        time.sleep(2)
        Build()
        time.sleep(2)
        End()
        time.sleep(5)
        LogUit()
        time.sleep(3)
    
    
    
    
    