# EXAMEN Selenium WebDriver avec Python

## Auteurs
**Matthéo Coppin ( Zagoki ), Ayoub Fathallah ( Formidabledu59 ), Hugo Bleuzé ( DxrkSquls ), Léa Dequeiros ( LeaDQDCD )**  

**Date de création : 27/02/2025** 

## Description
l'exam : exos visant à utiliser Selenium WebDriver avec Python pour automatiser des tâches sur des sites.

## Consignes
/n

### Exercice 1 : Remplir un formulaire d'inscription
- Sélectionnez un site web proposant un formulaire d'inscription simple (nom, prénom, email, mot de passe, etc.).
- Utilisez Selenium WebDriver pour automatiser le remplissage et la soumission du formulaire.

### Exercice 2 : Extraction d’informations
- Sélectionnez un site web d’actualités ou de e-commerce.
- Utilisez Selenium WebDriver pour récupérer des informations d’une liste d’articles/produits (URL, titre, description, prix, etc.).

### Exercice 3 : Tests et intégration continue
- Transformez les scripts précédents en tests Python.
- Exécutez ces tests dans un workflow GitHub Actions.

### Exercice 4 : Amélioration du workflow GitHub Actions
Ajoutez les améliorations suivantes à votre workflow :
- **Matrice de tests** : Tester votre script sur plusieurs versions de Python.
- **Génération de rapport de test**.
- **Déploiement d’une release**.
- **Envoi d’une notification Discord**.

## Prérequis
- Python
- Selenium WebDriver
- Un navigateur compatible (Chrome, Firefox, Edge)
- Un GitHub pour l'intégration continue

## Installation
Clonez ce dépôt :
   ```sh
   git clone https://github.com/SHREKTOUTNUAYOUBCHANGELELIEN
   ```


## Exécution
- Pour exécuter les scripts Selenium : 
  ```sh
  python script.py
  ```
- Pour exécuter les tests :
  ```sh
  pytest
  ```

## Intégration Continue
- Le workflow GitHub Actions est défini dans `.github/workflows/tests.yml`.
- Les tests sont exécutés automatiquement à chaque push/pull request.


## Contact
Pour toute question, nos mails :

- mattheo.coppin@ecoles-epsi.net
- lea.dequeirosdacunhad@ecoles-epsi.net
- hugo.bleuze@ecoles-epsi.net
- ayoub.fathallah@ecoles-epsi.net
