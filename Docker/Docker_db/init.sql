CREATE DATABASE comparateur;
USE comparateur;

CREATE TABLE supermarche (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    domaine VARCHAR(255),
    recherche  VARCHAR(255),
    code VARCHAR(255),
    espace VARCHAR(10)
);

CREATE TABLE liste_article (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    poids FLOAT
);

CREATE TABLE article (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_supermarche FOREIGN KEY,
    id_liste FOREIGN KEY,
    prixKg FLOAT,
    prixUnit FLOAT,
    lien VARCHAR(255),
    photo VARCHAR(255)
);


INSERT INTO supermarche(nom, domaine, recherche, espace)
VALUES("intermarche", "https://www.intermarche.com/", "recherche/", "%20");

INSERT INTO supermarche(nom, domaine, recherche, espace)
VALUES("carrefour", "https://www.carrefour.fr/", "s?q=", "+");

INSERT INTO supermarche(nom, domaine, recherche, code, espace)
VALUES("auchan", "https://www.auchan.fr/", "recherche?text=", "ca-n0701", "+");