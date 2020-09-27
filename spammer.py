import pyautogui
import time

time.sleep(10)

with open("textfile.txt", 'r') as f:
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(0.5)