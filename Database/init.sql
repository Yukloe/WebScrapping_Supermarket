CREATE DATABASE articles;
use articles;

CREATE TABLE articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prix FLOAT,
    lien VARCHAR(255),
    supermarche VARCHAR(10),
    photo VARCHAR(255)
);

INSERT INTO articles(nom, prix, lien, supermarche)
VALUES("test", 69.3, "test", "leclerc");

