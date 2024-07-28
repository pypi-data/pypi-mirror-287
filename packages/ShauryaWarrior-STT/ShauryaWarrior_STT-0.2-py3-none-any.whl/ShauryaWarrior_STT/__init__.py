# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
import time

# Setting up Chrome options with specific arguments
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--allow-file-access-from-files")  # Add this line
chrome_options.add_argument("--enable-features=WebAudio,Microphone")  # Add this line

# Setting up the Chrome driver with WebDriverManager and options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Creating the URL for the website using the current work directory
website = "https://allorizenproject1.netlify.app/"

# Opening the website
driver.get(website)

rec_file = f"{getcwd()}\\input.txt"

def listen():
    try:
        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening...")
        output_text = ""
        while True:
            output_element = driver.find_element(By.ID, 'output')
            current_text = output_element.text.strip()
            if current_text != output_text:
                output_text = current_text
                with open(rec_file, "w") as file: 
                    file.write(output_text.lower())
                    print("User : " + output_text)
            time.sleep(0.1)  # Wait for 0.1 seconds before checking again
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

listen()