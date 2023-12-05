# DockerWebscrapping_supermarket


## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/h_test1/dockerwebscrapping_supermarket.git
git branch -M main
git push -uf origin main
```


## Sujet du projet
# Objectif : Faire un « comparateur de prix »
# Description :
➢ Trouvez deux ou trois sites de votre choix vendant des articles similaires : dans notre cas les supermarchés.
➢ Utilisez scrapy pour récupérer les informations pertinentes des articles (nom, prix, lien vers
le site, …)
➢ Ces informations seront conservées dans une base de données (MySQL par exemple),
➢ Cette base de données devra être dans un conteneur Docker,
➢ Un conteneur avec un serveur web de votre choix permettra de visualiser les informations de
la base de données,
➢ L’affichage permettra de voir pour chaque article quel site à le prix le moins cher,
➢ Les articles sont cliquables (pour aller vers la page où ils sont en vente),
➢ Tout autre conteneur utile peut être ajouté (PhpMyAdmin ou équivalent par exemple)
Important :
➢ Le travail peut être fait à 2 ou 3,
➢ Vous créerez un dépôt privé sur gitlab.com,
➢ Vous m’ajouterez en tant que Reporter à votre dépôt (VincentD ou derrien@esigelec.fr),
➢ Vous devez utiliser « docker compose »,
➢ Vous devez avoir un fichier Dockerfile pour chaque image que vous utilisez,
➢ Idéalement, il suffit de lancer un script pour voir les résultats quelques secondes plus tard.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.


## Authors of the project
Arthur Conte
Hugo Patry
Jules Levasseur


## Project status

In progress.
