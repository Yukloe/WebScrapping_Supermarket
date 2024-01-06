from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration de la base de données
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'comparateur'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT liste_article.nom AS 'Nom', article.photo AS 'Photo', article.prixKg AS 'Prix Kg', article.prixUnit AS 'Prix Unit', article.lien AS 'URL', supermarche.nom AS 'Supermarche' FROM liste_article INNER JOIN article ON article.id_liste = liste_article.id INNER JOIN supermarche ON supermarche.id = article.id_supermarche")
    data = cur.fetchall()
    cur.close()
    return render_template('index.php', data=data)

if __name__ == '__main__':
    app.run(debug=True)
