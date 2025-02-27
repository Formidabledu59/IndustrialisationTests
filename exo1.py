from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-position=2000")

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://espace-abonnement.lavoixdunord.fr/essentielle")

inputEmail = "test@gmail.com"
inputPassword = "passwordTest"
inputPasswordConfirm = "passwordTest"
inputName = "NomDeFamille"
inputFirstname = "Prenom"
inputPhoneNumber = "0660066006"
inputZipCode = "46 rue du Ketchup"



consentement_button = driver.find_element(By.ID, "didomi-notice-agree-button")
driver.execute_script("arguments[0].click();", consentement_button)
    
email = driver.find_element(By.ID, "edit-submitted-user-email")
email.send_keys(inputEmail)

password = driver.find_element(By.ID, "edit-submitted-user-password")
password.send_keys(inputPassword)

passwordConfirm = driver.find_element(By.ID, "edit-submitted-user-password-confirm")
passwordConfirm.send_keys(inputPasswordConfirm)

civiliteMonsieur = driver.find_element(By.ID, "edit-submitted-user-profil-civilite-2")
driver.execute_script("arguments[0].click();", civiliteMonsieur)

name = driver.find_element(By.ID, "edit-submitted-user-profil-nom")
name.send_keys(inputName)

firstname = driver.find_element(By.ID, "edit-submitted-user-profil-prenom")
firstname.send_keys(inputFirstname)

day_select = Select(driver.find_element(By.ID, "edit-submitted-user-profil-naissance-day"))
month_select = Select(driver.find_element(By.ID, "edit-submitted-user-profil-naissance-month"))
year_select = Select(driver.find_element(By.ID, "edit-submitted-user-profil-naissance-year"))

day_select.select_by_value("15") 
month_select.select_by_value("3")
year_select.select_by_value("1995")

# //////////////////////////////////////////////////////

phoneNumber = driver.find_element(By.ID, "edit-submitted-numero-de-portable")
phoneNumber.send_keys(inputPhoneNumber)

zipCode = driver.find_element(By.ID, "edit-submitted-adresse-livraison-zipcode-francais-code-et-ville")
zipCode.send_keys(inputZipCode)

acceptContrat = driver.find_element(By.ID, "edit-submitted-demarrage-immediat-abo-1")
driver.execute_script("arguments[0].click();", acceptContrat)

submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView();", submit)
time.sleep(100)

submit.click

submitted_name = driver.find_element(By.ID, "name")
assert inputName in submitted_name.text

driver.quit()