CREATE DATABASE comparateur;
USE comparateur;

CREATE TABLE supermarche (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    domaine VARCHAR(255),
    recherche  VARCHAR(255),
    espace VARCHAR(10),
    Xpath VARCHAR(255)
);

CREATE TABLE liste_article (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    poids INT
);

CREATE TABLE article (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_supermarche INT,
    id_liste INT,
    FOREIGN KEY (id_supermarche) REFERENCES supermarche(id),
    FOREIGN KEY (id_liste) REFERENCES liste_article(id),
    prixKg FLOAT,
    prixUnit FLOAT,
    lien VARCHAR(255),
    photo VARCHAR(255)
);


INSERT INTO comparateur.supermarche(nom, domaine, recherche, espace, Xpath)
VALUES("intermarche", "https://www.intermarche.com/", "recherche/", "%20","/html/body/div[3]/div[1]/main/div/div[2]/div[2]/div[2]/div"),
("carrefour", "https://www.carrefour.fr/", "s?q=", "+", "/html/body/main/div/div[3]/section/div/div[2]/ul"),
("auchan", "https://www.auchan.fr/", "recherche?text=", "+", "/html/body/div[3]/div[2]/div[2]/div[4]");

-- INSERT INTO comparateur.liste_article(nom, poids)
-- VALUES("St Moret", 400), ("Camembert President", 250), ("Camembert President", 145);

-- Chargement des données du CSV
LOAD DATA INFILE '/docker-entrypoint-initdb.d/list_product.csv'
INTO TABLE liste_article
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(nom, poids);
