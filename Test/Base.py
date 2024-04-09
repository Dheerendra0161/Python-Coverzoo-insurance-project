import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def launchChrome(url):
    chrome_driver_path = r"C:\Users\Dheerendra\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    serviceObj = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=serviceObj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver


class ExplicitWait:
    pass


def lc():
    url = "https://www.coverzoo.com/"
    driver = launchChrome(url)
    quick_quote_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Quick Online Quote')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", quick_quote_button)
    driver.execute_script("arguments[0].click();", quick_quote_button)
    time.sleep(5)

    # Entering zip code
    zip_code_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='address_zip']"))
    )
    zip_code_input.send_keys('94016')

    start_quote_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start your Quote')]"))
    )
    driver.execute_script("arguments[0].click();", start_quote_button)

    # driver.quit()


lc()
