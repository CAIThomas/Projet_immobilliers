# Support vector regression

* Définition
* Types de noyaux
* Différence entre les noyaux 

## Définition

La Support Vector Regression (SVR) est une variante des machines à vecteurs de support (SVM) adaptée aux problèmes de régression. Son objectif est de trouver une fonction capable de prédire une valeur continue à partir de données d'entrée, en gérant aussi bien les relations linéaires que non linéaires grâce à l'utilisation de fonctions noyau (kernels).

La SVR utilise différentes fonctions noyau (kernels) pour modéliser des relations complexes dans les données. Ces noyaux permettent de transformer l'espace des caractéristiques (feature space) sans calcul explicite des coordonnées dans un espace de plus haute dimension (grâce à l'astuce du noyau, kernel trick).

## Types de noyaux 

Nous allons citer ici 3 types de noyaux qui sont très courants en SVR :
- Noyau linéaire (Linear Kernel)  
- Noyau polynomial (Polynomial Kernel)
- Noyau RBF (Radial Basis Function Kernel, ou Gaussian Kernel)

## Différence entre les noyaux 

Le noyau linénaire est conçue pour des données, des relations linéraires très simple, elle rapide et résistant au surapprentissage mais échoue à capturer les non-linéarités. 

Le noyau polynomial, quant à lui, arrive à capturer des relations non linéaires de degré modéré. Cependant, elle peut surajuster si le degré de polynôme est trop élevé.

Le noyau RBF est adapaté aux relations hautement non linéaires.
![alt text]([images/image7.png](https://github.com/CAIThomas/Projet_immobilliers/blob/main/images/image7.png?raw=true)
