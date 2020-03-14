'''This script is inteded to scrape call data from Whatsapp. 
Whatsapp makes accessing the call data very difficult, so this utilizes samsung Dex to
navigate the call menu options in whatsapp, screenshot each individual call, and organize the screenshots.
Then it uses OCR packages to pull the call data from the screenshots, allowing for call analysis '''

import pyautogui as pyag
import os,time
import pygetwindow as gw
from pynput.keyboard import Key, Controller

def open_dex():
    samsung_dex = gw.getWindowsWithTitle('Samsung DeX')[0]
    samsung_dex.maximize()
    samsung_dex.restore()


def take_screenshot(img_name):
    call_screenshots = r'C:\Users\Owner\Documents\Programming\Python\Projects\Kayes Gift\Whatsapp_Analyzer\Call_Screenshots'
    pyag.screenshot(os.path.join(call_screenshots,img_name))

    
if __name__ == "__main__":
    open_dex()
    keyboard = Controller()
    pyag.press('down',interval=1)
    for i in range(3):
        pyag.hotkey('ctrl', 'j')
        pyag.press('ctrl')
        time.sleep(2)
        img_name = f'Call {i}.png'
        take_screenshot(img_name)
        pyag.hotkey('ctrl', '5')
        pyag.press('ctrl')
        pyag.press('down',interval=2)
