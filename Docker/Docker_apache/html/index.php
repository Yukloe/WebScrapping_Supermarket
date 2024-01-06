<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparateur de prix</title>
</head>
<body>
    <h1>Liste des articles</h1>
    <table>
        <tr>
            <th>Phto</th>
            <th>Nom</th>
            <th>Prix Kg</th>
            <th>Prix Unit</th>
            <th>Supermarche</th>
            <th>Lien</th>
        </tr>
        <?php foreach ($data as $item): ?>
            <tr>
                <td><?php echo $item['Photo']; ?></td>
                <td><?php echo $item['Nom']; ?></td>
                <td><?php echo $item['Prix Kg']; ?></td>
                <td><?php echo $item['Prix Unit']; ?></td>
                <td><?php echo $item['Supermarche']; ?></td>
                <td><a href="<?php echo $item['URL']; ?>" target="_blank">Voir sur le site</a></td>
            </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>