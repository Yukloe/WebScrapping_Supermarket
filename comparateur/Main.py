import Collector
import mysql.connector

if __name__ == "__main__":
    print("GO")

    mydb = mysql.connector.connect(
        host="localhost:3306",
        user="root",
        password="root"
    )
    
    #Collector.Collect(1,"https://www.intermarche.com/", "recherche/", "%20","/html/body/div[3]/div[1]/main/div/div[2]/div[2]/div[2]/div", [], "")
    Collector.Collect(2,"https://www.carrefour.fr/", "s?q=", "+", "/html/body/main/div/div[3]/section/div/div[2]/ul", [[1,"St Moret", 400]], "")
    Collector.Collect(3,"https://www.auchan.fr/", "recherche?text=", "+", "/html/body/div[3]/div[2]/div[2]/div[4]", [[1,"St Moret", 400]], "")