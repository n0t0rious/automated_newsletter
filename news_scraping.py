import selenium.common
from selenium import webdriver
from selenium.webdriver.safari.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PASS = 'kynzo8-sehFib-dotzaw'
EMAIL = 't918mgmt@gmail.com'

# Initialize driver, get news site, & maximize window
driver = webdriver.Safari()
safari_options = Options()
driver.get('https://www.reuters.com/business/')
driver.maximize_window()

# Accept cookie pop-up
cookie_handler = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
cookie_handler.click()

# Sign-into website
sign_in = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/header/div/div/div/div/div[3]/a[1]')))
sign_in.send_keys(Keys.RETURN)

password_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    (By.ID, 'password')))
password_input.send_keys(f'{PASS}')

email_input = driver.find_element(By.ID, 'email')
email_input.send_keys(f'{EMAIL}')
email_input.submit()

# Find Articles on "Business page", loop through each article as WebDriver element and extract first 4 paragraphs
try:
    PARAGRAPH_LENGTH = 4
    news = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/main/div[3]/ul')))
    collections = news.find_elements(By.TAG_NAME, 'a')
    print(collections)
    for collection in collections:
        collection.send_keys(Keys.RETURN)
        try:
            article = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div/main/article/div/div[1]/div[2]/div/div[2]')))
            contents = article.find_elements(By.TAG_NAME, 'p')
            for i in range(PARAGRAPH_LENGTH):
                print(contents[i].text)
                driver.implicitly_wait(1)
            driver.back()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "frameset")))
            driver.switch_to.frame(1)
            time.sleep(1)
        except selenium.common.exceptions.NoSuchElementException and selenium.common.exceptions.TimeoutException:
            print('Error')
            driver.back()
            driver.switch_to.frame(1)
            time.sleep(1)
            continue
except selenium.common.exceptions.NoSuchElementException as e:
    print(e)
