from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()


browser.get("http://suninjuly.github.io/math.html")
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of people radio: ", robots_radio)

price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))

button = browser.find_element(By.ID, "book")

button.click()


el1 = browser.find_element(By.XPATH, "/html/body/form/div/div/div/label/span[2]")
el1text = el1.text
output = calc(el1text)

el2 = browser.find_element(By.XPATH, "/html/body/form/div/div/div/input")
el2.send_keys(output)

el3 = browser.find_element(By.CSS_SELECTOR,"#solve")

el3.click()






