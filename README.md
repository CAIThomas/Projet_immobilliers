# Projet_immobilliers

## Objectif : 

L’objectif de ce projet est de développer un modèle de Machine Learning permettant de prédire les prix de l’immobilier et des viagers en Île-de-France. Ce modèle reposera sur l’exploration, l’analyse et le nettoyage d’un large volume de données provenant de diverses sources, suivi de la sélection des variables pertinentes pour la prédiction. Ensuite, différents algorithmes de Machine Learning seront testés pour déterminer le modèle le plus performant pour cette tâche.

## étape 1 :

La première étape de notre projet est de choisir un site que nous voulons scrapper pour créer notre base de donnée, nous avons choisi le site :"logic-immo"

![alt text](https://github.com/CAIThomas/Projet_immobilliers/blob/main/images/logic-immo.png?raw=true)

## étape 2 :

Crée un code Python qui nous permet de scraper le site, le but est de gagner du temps. 
Pour la partie code nous avons plusieurs étapes :

-La première partie du code concerne la mise en place de l’environnement nécessaire pour utiliser Selenium, un outil d’automatisation web largement utilisé pour effectuer du web scraping ou des tests automatisés sur des sites internet. Nous avons importé plusieurs bibliothèques :

![alt text](https://github.com/CAIThomas/Projet_immobilliers/blob/main/images/image2.png)
![alt text](https://github.com/CAIThomas/Projet_immobilliers/blob/main/images/image3.png)

-Puis après avoir importé, on peut utiliser les modules comme Webdriver, Services, Options, By, WebDriverWait, expected_conditions : Ces modules permettent de lancer un navigateur, de le configurer, de localiser des éléments sur une page, et d’attendre que certains éléments soient prêts avant d'interagir avec eux.

Notre prochaine étape était de régler les problèmes de cookies car lorsqu'on a atterri au site, la première chose qu'on nous demandait était les cookies, donc pour pouvoir continuer sur la page, on a créé une fonction pour accepter les cookies.
![alt text](https://github.com/CAIThomas/Projet_immobilliers/blob/main/images/image5.png)
![alt text](https://github.com/CAIThomas/Projet_immobilliers/blob/main/images/image4.png)



