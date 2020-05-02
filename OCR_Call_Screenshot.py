'''This script uses pytesseract to read the data from the whatsapp call log screenshots'''
import image_processing
import glob
from tqdm import tqdm


call_directory = r'C:\Users\Owner\Documents\Programming\Python\Projects\Kayes Gift\Whatsapp_Analyzer\Call_Screenshots'
call_screenshot_list = glob.glob(call_directory + "/*.png")
call_log = {}
for call in tqdm(call_screenshot_list):
    file_name,call_data = image_processing.process_image(call)
    call_log[file_name] = call_data
call_log_txt = call_directory + r"\call_logv2.txt"
outfile = open(call_log_txt, "w")
print(call_log, file=outfile)
outfile.close()