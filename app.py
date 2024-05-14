#****************************************************

#learning selenium automation

#****************************************************

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# s=Service("C:/Users/user/Desktop/chromedriver-win64/chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver= webdriver.Chrome(options=options , service=s)
# driver.get("https://www.google.com")
# time.sleep(2)

# user_input= driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
# user_input.send_keys("suyog")
# time.sleep(2)

# user_input.send_keys(Keys.ENTER)
# time.sleep(2)

# link=driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
# link.click()
# time.sleep(2)

# link2= driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/section[2]/a[1]')
# link2.click()



#****************************************************

#learning infinite scroll  without clicking on the button

#****************************************************


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# s=Service("C:/Users/user/Desktop/chromedriver-win64/chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver= webdriver.Chrome(options=options , service=s)
# driver.get("https://www.ajio.com/s/table-napkins-4720-51871")
# time.sleep(2)
# old_height=driver.execute_script('return document.body.scrollHeight')

# while True:
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)
#     new_height=driver.execute_script('return document.body.scrollHeight')
#     if new_height==old_height:
#         break
#     old_height=new_height
#     time.sleep(2)

# html= driver.page_source
# with open('ajio.html','w',encoding='utf-8') as f:
#     f.write(html)

#****************************************************


#****************************************************
# learning infinite scroll with clicking on the button
#****************************************************

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s=Service("C:/Users/user/Desktop/chromedriver-win64/chromedriver.exe")


#options.add_experimental_option("detach", True)
#driver= webdriver.Chrome(options=options , service=s)

# options = webdriver.ChromeOptions() 

# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data/Default")
# options.add_argument("--profile-directory=Default")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
driver= uc.Chrome(  service=s)
driver.get("https://www.smartprix.com/mobiles")
# time.sleep(3)
# driver.find_element(by=By.XPATH, value='//*[@id="challenge-stage"]/div/label/input').click()
time.sleep(5)
#WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='Widget containing a Cloudflare security challenge']")))
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ctp-checkbox-label"))).click()
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(3)
old_height =driver.execute_script('return document.body.scrollHeight')

while True:
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)
    new_height=driver.execute_script('return document.body.scrollHeight')

    print(old_height)   
    print(new_height)

    if new_height==old_height:
        break
    old_height=new_height
    time.sleep(2)
html =driver.page_source
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import undetected_chromedriver as uc

# # Removed detach option and updated user data directory path
# options = webdriver.ChromeOptions()
# options.add_argument("--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data/")
# #options.add_experimental_option("excludeSwitches", ["enable-logging"])

# # Using undetected_chromedriver instead of the standard ChromeDriver
# driver = uc.Chrome(options=options)

# # Navigate to the website
# driver.get("https://www.smartprix.com/mobiles")
# time.sleep(2)

# # Click on the element with the specified XPath
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[6]/div[2]/label[1]/span').click()
# time.sleep(2)


#chatgpt

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# import undetected_chromedriver as uc

# # Specify the path to your chromedriver executable
# s = Service("C:/Users/user/Desktop/chromedriver-win64/chromedriver.exe")

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data/Default")
# options.add_argument("--profile-directory=Default")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# driver = webdriver.Chrome(options=options, service=s)
# driver.get("https://www.smartprix.com/mobiles")

# try:
#     # Wait for the iframe to be available and switch to it
#     iframe = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='Widget containing a Cloudflare security challenge']"))
#     )
#     driver.switch_to.frame(iframe)
    
#     # Wait for the checkbox to be clickable and click it
#     checkbox = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ctp-checkbox-label"))
#     )
#     checkbox.click()
    
#     # Switch back to the main content
#     driver.switch_to.default_content()
    
#     # Wait for the specific element and click it
#     element_to_click = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/aside/div/div[6]/div[2]/label[1]/span'))
#     )
#     element_to_click.click()
    
#     time.sleep(2)  # Additional wait time if needed

# except selenium.common.exceptions.TimeoutException:
#     print("Element not found within the given time")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     driver.quit()
