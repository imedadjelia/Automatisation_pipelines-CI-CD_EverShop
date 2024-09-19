# Automatisation des tests pour l'application Evershop avec GitHub Actions

Ce projet a pour objectif d'automatiser les tests de l'application Evershop en utilisant les pipelines CI/CD de GitHub Actions. L'intégration continue et le déploiement continu (CI/CD) sont mis en place afin d'assurer une exécution automatique des tests à chaque modification du code.

## Principales étapes du projet :

* Installation d'Evershop : Mise en place de l'application Evershop pour tester ses fonctionnalités.
* Création d'un dépôt GitHub : Un dépôt dédié a été créé pour héberger tout le code du projet.
* Automatisation des tests avec Selenium et Pytest : Les tests fonctionnels de l'application ont été automatisés en utilisant Selenium WebDriver et Pytest. Ces tests permettent de vérifier la validité des fonctionnalités critiques d'Evershop.
* Configuration des pipelines CI/CD avec GitHub Actions : Mise en place de pipelines GitHub Actions pour exécuter automatiquement les tests à chaque push ou pull request. Cela garantit que toute modification du code est immédiatement testée, assurant la stabilité et la qualité continue du projet.

## Mes réalisations 

### Stratégie de Test pour l'application Evershop

Pour assurer une couverture optimale et la qualité des tests de l'application Evershop, une approche structurée a été adoptée :

1. [Test exploratoire et élaboration d'un diagramme de changement d'état](https://app.diagrams.net/#G1hKHVGMZ6pRezyrZE_FsnIPSJkIVJ6ei0#%7B%22pageId%22%3A%22RVhPdQc17Uw-xQleVsTr%22%7D) : Une première phase de tests exploratoires a permis de mieux comprendre les différentes fonctionnalités de l'application. Cela a conduit à la création d'un diagramme de changement d'état, permettant de visualiser les transitions critiques et d'aider à prioriser les tests.
* Aperçu :
  
![Capture d'écran 2024-09-19 114315](https://github.com/user-attachments/assets/b55f9c8b-4502-48cf-ba7d-5409ef066210)   

2. [Rédaction de scénarios de tests](https://github.com/imedadjelia/EverShop-Automatisation-Pipelines-CI-CD/blob/main/Sc%C3%A9narios%20de%20test) : Des scénarios de tests détaillés ont été rédigés en fonction des flux et fonctionnalités les plus importants identifiés lors de la phase exploratoire. Ces scénarios couvrent les cas d'usage les plus critiques et assurent une couverture fonctionnelle pertinente.
* Aperçu :
  
![Capture d'écran 2024-09-19 122721](https://github.com/user-attachments/assets/55a3e8e7-662a-43b1-a2c5-a30661c447b0)

3. [Automatisation des tests avec Selenium et Pytest](https://github.com/imedadjelia/EverShop-Automatisation-Pipelines-CI-CD/blob/main/Test/test_CESA.py) : Les scénarios de tests ont été automatisés à l'aide de Selenium pour l'interaction avec l'interface utilisateur, et Pytest pour la gestion des assertions et l'exécution des tests. Cette approche garantit une exécution répétée et fiable des tests, tout en optimisant l'efficacité des validations.
* Aperçu :

![ezgif-6-356edd7ddb](https://github.com/user-attachments/assets/a98daed5-3c55-44af-9862-e1b0e41b257a)


4. [Configuration des pipelines CI/CD avec GitHub Actions ](https://github.com/imedadjelia/EverShop-Automatisation-Pipelines-CI-CD/blob/main/.github/workflows/test.yml): Pour assurer une intégration continue, des pipelines GitHub Actions ont été configurés. Ils exécutent automatiquement les tests à chaque modification du code source (push ou pull request), garantissant que tout changement est testé immédiatement dans un environnement isolé.

* Aperçu :
  
![ezgif-1-fdc14fbeac](https://github.com/user-attachments/assets/8f3b8d9a-4fb1-4ae5-aaa5-8bfcc77d51ba)

