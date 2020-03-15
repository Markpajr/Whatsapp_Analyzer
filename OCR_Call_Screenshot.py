'''This script uses pytesseract to read the data from the whatsapp call log screenshots'''
import pytesseract
import glob
from tqdm import tqdm

def scrape_image(image_file):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    return pytesseract.image_to_string(image_file)


if __name__ == "__main__":
    call_directory = r'C:\Users\Owner\Documents\Programming\Python\Projects\Kayes Gift\Whatsapp_Analyzer\Call_Screenshots'
    call_screenshot_list = glob.glob(call_directory + "/*.png")
    call_log = {}
    for call in tqdm(call_screenshot_list):
        call_data = scrape_image(call)
        call_log[call] = call_data
    call_log_txt = call_directory + r"\call_log.txt"
    outfile = open(call_log_txt, "w")
    print(call_log, file=outfile)
    outfile.close()