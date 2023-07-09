from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_options = Options()
chrome_options.add_experimental_option("detach",True)#ne pas fermer le browser

driver = webdriver.Chrome(chrome_options)
driver.get("https://facebook.com")

###ValidationCookies
bouton_cookie = driver.find_element(By.CLASS_NAME,'_al65')
bouton_cookie.click()

###Authentification
box_mail = driver.find_element(By.ID,'email')
box_pass = driver.find_element(By.ID,'pass')
box_mail.clear()
box_pass.clear()
box_mail.send_keys('identifiant')
box_pass.send_keys('password')
conn = driver.find_element(By.CLASS_NAME, '_42ft')
conn.click()

#Aller sur MarketPlace
driver.get('https://www.facebook.com/marketplace/?ref=bookmark')

# Fermer le navigateur 

# driver.quit()
