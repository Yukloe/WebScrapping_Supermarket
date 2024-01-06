import time
import Treatment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

def Collect(idMagasin, URL, Recherche, espace, Xpath, listArticle, code = ""):
    
    # Création du driver
    driver = webdriver.Chrome()

    # Positionnement sur le site marchand
    driver.get(URL)

    time.sleep(5)

    # Gestion des Cookies
    try :
        driver.find_element(By.XPATH, '//button[contains(text(), "Continuer sans accepter")]').click()
    except NoSuchElementException :
        try : 
            driver.find_element(By.XPATH, '//span[contains(text(), "Continuer sans accepter")]').click()
        except NoSuchElementException :
            print("No path yet E1")

    # positionnement sur un magasin
    try :
        driver.find_element(By.XPATH, '//a[contains(text(), "Trouver un magasin")]').click()
    except ElementClickInterceptedException:
        try :
            driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[3]/div[2]/button/i').click()
            driver.find_element(By.XPATH, '//a[contains(text(), "Trouver un magasin")]').click()
        except ElementClickInterceptedException :
            try :
                driver.find_element(By.XPATH, '//a[contains(text(), "Trouver un magasin")]').click()
            except ElementClickInterceptedException :
                driver.find_element(By.XPATH, '//a[contains(text(), "Trouver un magasin")]').click()
    except NoSuchElementException :
        print("No path yet E2")

    time.sleep(1)
    try :
        driver.find_element(By.XPATH, '//button/span[contains(text(), "Code postal, ville ...")]').click()
    except NoSuchElementException :
        print("No path yet E3")

    time.sleep(1)
    try :
        driver.find_element(By.XPATH, "/html/body/div[12]/div[1]/main/div[1]/div[1]/div/div[1]/input").send_keys("76800")
    except NoSuchElementException :
        print("No path yet E4")

    time.sleep(1)
    try :
        driver.find_element(By.XPATH, "/html/body/div[12]/div[1]/main/div[1]/div[1]/div/div[2]/ul").click()
    except NoSuchElementException :
        print("No path yet E5")

    time.sleep(1)
    try :
        driver.find_element(By.XPATH, "/html/body/div[12]/div[1]/main/div[1]/div[2]/div[2]/section/div/div/div/div[2]/form/button").click()
        time.sleep(5)
    except NoSuchElementException :
        print("No path yet E6")

    listResult = []

    for Article in listArticle:
        Search = URL + Recherche + espace.join(Article[1].split())
        driver.get(Search)

        time.sleep(5)
        ResultElement = driver.find_element(By.XPATH, Xpath)

        temp = Treatment.getInfo(ResultElement.get_attribute("innerHTML"), Article[2])
        if len(temp) >= 4 :
            listResult.append([idMagasin, Article[0], temp[0], temp[1], URL + temp[2][1:], temp[3]])

    print(listResult)
