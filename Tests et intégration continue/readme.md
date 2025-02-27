Tests et Intégration Continue
Objectif
Automatiser des tâches sur des sites web avec Selenium WebDriver, transformer ces scripts en tests Python, et les exécuter dans un workflow GitHub Actions.


Étapes Suivies
1. Transformer les Scripts en Tests Python
Les scripts d'automatisation ont été transformés en tests unitaires en utilisant la bibliothèque unittest.

2. Configurer un Workflow GitHub Actions
Un fichier de workflow GitHub Actions a été créé pour :

Configurer l'environnement Python.
Installer les dépendances nécessaires.
Télécharger et configurer ChromeDriver.
Exécuter les tests unitaires.
3. Vérification
Pour vérifier que tout fonctionne :

Exécutez les tests localement avec python -m unittest discover.
Poussez les changements sur GitHub et vérifiez l'onglet "Actions" pour les résultats du workflow.


Conclusion
Ces étapes permettent de garantir la qualité et la fiabilité des scripts à chaque modification du code.