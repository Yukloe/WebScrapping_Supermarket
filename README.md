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

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Sujet du projet
# Objectif : Faire un « comparateur de prix »
# Description :
➢ Trouvez deux ou trois sites de votre choix vendant des articles similaires,
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


## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
