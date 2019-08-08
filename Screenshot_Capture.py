import pyautogui
import time

index = 1

while index <= 5:
    pyautogui.screenshot(str(index)+".png")
    index+=1
    time.sleep(3)
