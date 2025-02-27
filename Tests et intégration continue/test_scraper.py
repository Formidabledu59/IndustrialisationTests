import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instant-gaming.com/fr/")
        time.sleep(3)

    def test_scrape_games(self):
        driver = self.driver
        games = driver.find_elements(By.CLASS_NAME, "item")

        for game in games[:9]:  
            title = game.find_element(By.CLASS_NAME, "title").text
            price = game.find_element(By.CLASS_NAME, "price").text
            discount = game.find_element(By.CLASS_NAME, "discount").text

            print(f"🎮 Jeu : {title}")
            print(f"💰 Prix : {price}")
            print(f"🔻 Remise : {discount}")
            print("-" * 30)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()