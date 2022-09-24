import pyautogui
import time

time.sleep(3)
x, y = pyautogui.position()

#print ("x = "+str(x)+" y = "+str(y))

loop = 0
foodClick = 0

while (loop < 1):
    #pyautogui.click(x = 587, y = 364)
    ##time.sleep(150)
    #pyautogui.click(x = 634, y = 400)
    time.sleep(80)
    while(foodClick < 6):
        pyautogui.click(x = 357, y = 636)
        time.sleep(2)
        pyautogui.click(x = 432, y = 627)
        time.sleep(2)
        foodClick = foodClick + 1
    foodClick = 0