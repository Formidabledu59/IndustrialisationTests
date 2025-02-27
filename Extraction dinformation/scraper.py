from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialisation du navigateur
driver = webdriver.Chrome()

# Aller sur la page des jeux populaires
driver.get("https://www.instant-gaming.com/fr/")

# Attendre quelques secondes pour le chargement
time.sleep(3)

# Récupérer les jeux affichés
games = driver.find_elements(By.CLASS_NAME, "item")

# Extraire les infos des 9 premiers jeux
for game in games[:9]:  
    title = game.find_element(By.CLASS_NAME, "title").text
    price = game.find_element(By.CLASS_NAME, "price").text
    discount = game.find_element(By.CLASS_NAME, "discount").text

    print(f"🎮 Jeu : {title}")
    print(f"💰 Prix : {price}")
    print(f"🔻 Remise : {discount}")
    print("-" * 30)

# Fermer le navigateur
driver.quit()
