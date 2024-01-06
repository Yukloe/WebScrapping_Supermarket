from bs4 import BeautifulSoup
import re

def getInfo(htmlCode, articleWeight):

    listArticle = htmlCode.split("<li")
    returnValue = []
    for i in range(len(listArticle)):
        soup = BeautifulSoup("<li"+listArticle[i], "html.parser")

        try :
            weight = soup.find('p', {"class":"pl-text pl-text--size-m pl-text--style-caption"}).get_text()
        except AttributeError :
            try :
                weight = soup.find('span', {"class":"product-attribute"}).get_text()
            except AttributeError :
                weight = "NULL"

        if str(articleWeight) in weight :

            weight = articleWeight

            try: 
                priceUnit = soup.find('span', {"class":"product-price__amount-value"}).get_text()
                try :
                    priceUnit = float(priceUnit)
                except ValueError :
                    priceUnit = float(priceUnit[1:-1].replace(',', '.'))
            except AttributeError :
                try: 
                    priceUnit = soup.find('div', {"class":"product-price bolder text-dark-color"}).get_text()
                    try :
                        priceUnit = float(priceUnit)
                    except ValueError :
                        priceUnit = float(priceUnit.replace(',', '.')[:-1])
                except AttributeError :
                    priceUnit = "NULL"

            try: 
                price = soup.find('p', {"class":"ds-product-card-refonte__perunitlabel pl-text pl-text--size-m pl-text--style-caption"}).get_text()
                try :
                    price = float(price)
                except ValueError :
                    price = float(price[1:-1].replace(',', '.').split()[0])
            except AttributeError :
                try: 
                    price = soup.find('span', {"data-seller-type":"GROCERY"}).get_text()
                    try :
                        price = float(price)
                    except ValueError :
                        price = float(price.replace(',', '.').split()[0][:-1])
                except AttributeError :
                    price = "NULL"

            try:
                href = soup.find('a').get("href")
            except AttributeError :
                href = "NULL"

            try:
                image = soup.find('img').get("src")
            except AttributeError :
                image = "NULL"

            returnValue = [price, priceUnit, href, image]

    return returnValue