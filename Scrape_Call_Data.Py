'''This script is inteded to scrape call data from Whatsapp. 
Whatsapp makes accessing the call data very difficult, so this utilizes samsung Dex to
navigate the call menu options in whatsapp, screenshot each individual call, and organize the screenshots.
Then it uses OCR packages to pull the call data from the screenshots, allowing for call analysis '''

import pyautogui as pyag
import os,time
import pygetwindow as gw


def open_dex():
    # Finds and restores the Samsung Dex Window
    samsung_dex = gw.getWindowsWithTitle('Samsung DeX')[0]
    samsung_dex.maximize()
    samsung_dex.restore()


def take_screenshot(img_name):
    #Saves a screenshot to indicated path
    screenshots_path = r'C:\Users\Owner\Documents\Programming\Python\Projects\Kayes Gift\Whatsapp_Analyzer\Call_Screenshots'
    pyag.screenshot(os.path.join(screenshots_path,img_name))


if __name__ == "__main__":
    open_dex()
    pyag.press('down',interval=1)
    for i in range(3):
        # Uses autohotkey to initiate Enter and Escape commands, issues with pyautogui sending these keys
        pyag.hotkey('ctrl', 'j')
        pyag.press('ctrl')
        time.sleep(2)
        img_name = f'Call {i}.png'
        take_screenshot(img_name)
        pyag.hotkey('ctrl', '5')
        pyag.press('ctrl')
        pyag.press('down',interval=2)
