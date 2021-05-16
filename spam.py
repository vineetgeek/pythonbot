import pyautogui
import time

time.sleep(10)
for i in range(500):
    pyautogui.write("hello")
    pyautogui.press("enter")
    pyautogui.write("kya haal hai bc")
    pyautogui.press("enter")