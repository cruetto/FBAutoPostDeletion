from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random

#
#
#   /path/to/chrome --remote-debugging-port=8989
#
#   https://www.facebook.com/100010719969015/allactivity?activity_history=false&category_key=GROUPPOSTS&manage_mode=false&should_load_landing_page=false&locale=en_EN
#
#

# Specify the debugging address for the already opened Chrome browser
debugger_address = 'localhost:8989'

# Set up ChromeOptions and connect to the existing browser
c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")

# Initialize the WebDriver with the existing Chrome instance
driver = webdriver.Chrome(options=c_options)

# Now, you can interact with the already opened Chrome browser
x = 0

min = float(input("Input minimal value(Recommended 0.2):"))
max = float(input("Input maximum value(Recommended 1):"))

while True:

    try:
        print(x)
        x += 1

        randomnum = random.uniform(min, max)
        # print(randomnum)
        time.sleep(randomnum)

        threedots = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Action options']")
        threedots.click()


        randomnum = random.uniform(min, max)
        # print(randomnum)
        time.sleep(randomnum)

        firstdelete = driver.find_element(By.XPATH, "//span[text()='Delete']")
        firstdelete.click()


        randomnum = random.uniform(min, max)
        # print(randomnum)
        time.sleep(randomnum)

        secondDelete = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Delete']")
        secondDelete.click()
    except:
        print("Waiting to load...")
        time.sleep(2)


# Remember to close the WebDriver when you're done
driver.quit()

print("Program ended")