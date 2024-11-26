# /****************************************
#  *         CYBER FOCUS SCRIPT          *
#  *       CAPTCHA BYPASS AUTOMATION     *
#  ****************************************/

import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image
import io 

# _____
#|  ___|__   ___ _   _ ___
#| |_ / _ \ / __| | | / __|
#|  _| (_) | (__| |_| \__ \
#|_|  \___/ \___|\__,_|___/

# /****************************************
#  *       CONFIGURATION CHROME OPTIONS  *
#  ****************************************/

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_extension(r".\adblock.crx")  # File Adblock

# /****************************************
#  *            FUNCTION 1               *
#  *           BYPASS CAPTCHA            *
#  ****************************************/


def bypass_captcha():

    driver = webdriver.Chrome(options=chrome_options)

    # ouvrir zefoy ou votre site que vous shouaite
    time.sleep(5)
    driver.get ("https://zefoy.com/")
    time.sleep(40)
    
    #localised class image captcha

    
    captcha_image = driver.find_element(By.CSS_SELECTOR,'img.img-thumbnail.card-img-top.border-0') #remplace la balise du site web 

    # screen captcha stocke l'image
    captcha_image_screen = captcha_image.screenshot_as_png 

    # convert screenshot

    image = Image.open(io.BytesIO(captcha_image_screen))

    captcha_image_path = r"./captcha_image.png"

    image.save(captcha_image_path)

    # Cheak Google New page 

    driver.execute_script("window.open('https://lens.google.com/', 'new tab')")
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(2) 
    try:
        select_all_element = driver.find_element(By.XPATH, '//span[text()="Sélectionner tout le texte"]')
        select_all_element.click()
        print("Clicked on the 'Select all text' element.")
        time.sleep(4)
    except Exception as e:
        print("Error clicking on the 'Select all text' element:", str(e))
    
     # Get the text from the h1 element
    try:
        h1_element = driver.find_element(By.XPATH, '//h1[@jsname="r4nke" and @class="wCgoWb"]')
        captcha_text = h1_element.text
        print("Texte de la balise h1:", captcha_text)
        time.sleep(5)
    except Exception as e:
        print("Erreur lors de la récupération du texte de la balise h1:", str(e))

        # Upload le captcha sur Google lens

    try:
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(captcha_image_path)
        print("Image UPLOAD.")
        time.sleep(4)
    except Exception as e:
        print("Erreur upload file", str(e))

    time.sleep(5)

    driver.switch_to.window(driver.window_handles[0])

    try:
        captcha_input = driver.find_element(By.CSS_SELECTOR, 'input.form-control.form-control-lg.text-center.rounded-0.remove-spaces')
        captcha_input.send_keys(captcha_text)
        print("CAPTCHA text entered.")

        submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg.btn-block.rounded-0.submit-captcha')
        driver.execute_script("arguments[0].click();", submit_button)
        print("CAPTCHA form submitted.")

    except Exception as e :
        print ("Erreur dans le text du captcha")

    time.sleep(4)

    try:
            error_element = driver.find_element(By.XPATH, '//h5[@id="errorcapthca" and text()="Error"]')
            if error_element.is_displayed():
                print("Captcha code is incorrect. Retrying...")
                driver.quit()
                return False
    except Exception as e:
            print("No CAPTCHA error detected:", str(e))
        
        
    driver.quit()
    return True

# Retry until successful
while not bypass_captcha():
    time.sleep(1)  # Wait a bit before retrying
    print("Retrying CAPTCHA...")