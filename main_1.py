import pywhatkit
import pyautogui
import time

pywhatkit.sendwhatmsg("+6285368612568", "Hello World", 9, 38)
pywhatkit.sendwhatmsg("+6283122819125", "Hello World", 9, 39)
pywhatkit.sendwhatmsg("+6285837502368", "Hello World", 9, 40)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press("enter")

