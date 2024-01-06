import Collector
import mysql.connector

if __name__ == "__main__":

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM comparateur.supermarche")

    Supermarket = cursor.fetchall()

    cursor.execute("SELECT * FROM comparateur.liste_article")

    ListeArticle = cursor.fetchall()

    print(Supermarket)
    print(ListeArticle)

    for x in Supermarket:

        result = ""

        try :
            result = Collector.Collect(x[0], x[2], x[3], x[4], x[5], ListeArticle)

            for article in result :
                cursor.execute(f"""
                                    INSERT INTO comparateur.article(id_supermarche, id_liste, prixKg, prixUnit, lien, photo)
                                    VALUES("{article[0]}", "{article[1]}", "{article[2]}", "{article[3]}", "{article[4]}", "{article[5]}")
                                """)
                
                mydb.commit()

                print(cursor.rowcount, " record inserted.")
        
        except :
            print("OOPS")