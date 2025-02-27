# Exercice 1 : Remplir un formulaire d'inscription avec Selenium

## Objectif
L'objectif de cet exercice est d'utiliser Selenium WebDriver pour automatiser le remplissage et la soumission d'un formulaire d'inscription sur un site web.

## Installation des dépendances
Avant d'exécuter le script, assurez-vous d'installer Selenium avec la commande suivante :

```sh
pip install selenium
```

## Exécution du script
Exécutez le script Python avec la commande suivante :

```sh
python exo1.py
```

## Explication du code

### 1. Initialisation du WebDriver
Le script utilise **webdriver.ChromeOptions()** pour configurer le navigateur. Par exemple, il positionne la fenêtre à une certaine position sur l'écran.

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-position=2000")

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
```

### 2. Accès au site et remplissage du formulaire
Le script charge la page du formulaire et remplit les champs nécessaires, tels que l'email, le mot de passe, et les informations personnelles.

```python
driver.get("https://espace-abonnement.lavoixdunord.fr/essentielle")

email = driver.find_element(By.ID, "edit-submitted-user-email")
email.send_keys("test@gmail.com")
```

### 3. Sélection de la date de naissance
L'utilisation de **Select** permet de choisir une date de naissance dans un menu déroulant.

```python
day_select = Select(driver.find_element(By.ID, "edit-submitted-user-profil-naissance-day"))
day_select.select_by_value("15")
```

### 4. Soumission du formulaire
Le bouton de soumission est cliqué après un délai pour garantir que toutes les actions précédentes sont bien effectuées.

```python
submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView();", submit)
time.sleep(100)
submit.click()
```
