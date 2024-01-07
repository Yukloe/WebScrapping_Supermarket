<?php
// Remplacez ces informations par vos propres paramètres de base de données
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "comparateur";

// Connexion à la base de données
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier la connexion
if ($conn->connect_error) {
    die("La connexion à la base de données a échoué : " . $conn->connect_error);
}

// Requête SQL pour récupérer l'article le moins cher de chaque liste d'articles avec les détails du magasin
$sql = "
    SELECT DISTINCT
        la.nom AS liste_nom,
        a.photo as photo,
        s.nom AS supermarche_nom,
        a.prixKg AS prix_kg,
        a.prixUnit AS prix_unitaire,
        a.lien AS lien
    FROM
        liste_article la
    INNER JOIN
        article a ON la.id = a.id_liste
    INNER JOIN
        supermarche s ON a.id_supermarche = s.id
    LEFT JOIN
        (
            SELECT
                id_liste,
                MIN(prixKg) AS min_prixKg
            FROM
                article
            GROUP BY
                id_liste
        ) min_prices ON a.id_liste = min_prices.id_liste AND a.prixKg = min_prices.min_prixKg
    WHERE
        min_prices.id_liste IS NOT NULL
";

$result = $conn->query($sql);

// Vérifiez si la requête a réussi
if (!$result) {
    die("Erreur dans la requête SQL : " . $conn->error);
}

// Récupérez tous les résultats sous forme de tableau associatif
$rows = $result->fetch_all(MYSQLI_ASSOC);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Articles les moins chers par liste</title>
</head>
<body>
    <h1>Liste des articles</h1>
    <table>
        <tr>
            <th style="font-size: 26px">Image</th>
            <th style="font-size: 26px">Nom de la liste</th>
            <th style="font-size: 26px">Nom du supermarche</th>
            <th style="font-size: 26px">Prix au Kg</th>
            <th style="font-size: 26px">Prix à l'unité</th>
            <th style="font-size: 26px">URL</th>
        </tr>
        <?php foreach ($rows as $item): ?>
            <tr>
                <td><img src="<?php echo $item['photo']; ?>" alt="Photo"></td>
                <td style="font-size: 26px"><?php echo $item['liste_nom']; ?></td>
                <td style="font-size: 26px"><?php echo $item['supermarche_nom']; ?></td>
                <td style="font-size: 26px"><?php echo $item['prix_kg']; ?></td>
                <td style="font-size: 26px"><?php echo $item['prix_unitaire']; ?></td>
                <td style="font-size: 26px"><a href="<?php echo $item['lien']; ?>" target="_blank">Voir sur le site</a></td>
            </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>