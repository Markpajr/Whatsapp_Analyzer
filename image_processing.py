import cv2
import os
import pytesseract

def process_image(image_path):
    #Read the image
    img = cv2.imread(image_path)
    
    #Get image filename and output directory
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_dir = r"C:\Users\Owner\Documents\Programming\Python\Projects\Kayes Gift\Whatsapp_Analyzer\Call_Screenshots\Processed"
    
    #Rescale the image
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    
    # Convert image to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Convert image to Black and White through Binary thresholds
    img = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)[1]
    
    # Apply bilateral filtering to maintain text edges
    img = cv2.bilateralFilter(img,9,75,75)
    
    # Saves processed image
    save_path = os.path.join(output_dir,f'{file_name}_processed_.jpg')
    if not cv2.imwrite(save_path, img):
        raise Exception("Could not save image")
    
    # Convert image to Text with Pytesseract
    img_text = pytesseract.image_to_string(img, lang="eng")
    return (file_name,img_text)

if __name__ == "__main__":
    test_image = r"C:\Users\Owner\Documents\Programming\Python\Projects\Kayes Gift\Whatsapp_Analyzer\Call_Screenshots\Call 200.png"
    print(process_image(test_image))