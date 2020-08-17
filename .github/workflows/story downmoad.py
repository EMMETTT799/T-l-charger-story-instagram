from selenium import webdriver

from selenium.webdriver.common.keys import Keys#Pour pouvoir utiliser le clavier

import time #Le module time va nous permettre de mettre des délais pour temporiser les chargements des pages

from PIL import Image

img = Image.open('tenor.gif')

navigateur = webdriver.Chrome() #Definit le driver qui va etre utlisé

navigateur.set_window_size(1080,800) #(largeur,hauteur)

navigateur.get("https://storiesig.com/") #Le navigateur va s'ouvrir et va charger cette page

img.show()

time.sleep(5) #On met en pause le programme 5 secondes pour être sûr que la page charge correctement

barre_rechercher = navigateur.find_element_by_xpath('//*[@id="username"]')

barre_rechercher.send_keys("arianagrande")

time.sleep(5)

barre_rechercher.send_keys(Keys.ENTER)

time.sleep(5)

barre_rechercher = navigateur.find_element_by_xpath('//*[@id="__next"]/div/main/section/div/div[1]/a').click()

time.sleep(5)

barre_rechercher = navigateur.find_element_by_xpath('//*[@id="__next"]/div/section/div/article[1]/div[3]/a').click() # 1er boutton download

time.sleep(5)

barre_rechercher = navigateur.find_element_by_xpath('//*[@id="__next"]/div/section/div/article[2]/div[3]/a').click() #2eme boutton download

time.sleep(5)

barre_rechercher = navigateur.find_element_by_xpath('//*[@id="__next"]/div/section/div/article[3]/div[3]/a').click() # 3 eme boutton download

time.sleep(5)

barre_rechercher = navigateur.find_element_by_xpath('//*[@id="__next"]/div/section/div/article[4]/div[3]/a').click() # 4eme boutton donwload

time.sleep(5)

barre_rechercher = navigateur.find_element_by_xpath('//*[@id="__next"]/div/section/div/article[5]/div[3]/a').click() # 5eme boutton download

time.sleep(5)
