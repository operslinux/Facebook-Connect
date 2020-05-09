# -*- coding: utf-8 -*-

from form.logo import LogoTwo, LogoCero, LogoOne
from selenium import webdriver
from colorama import Back, Fore, init
from tqdm import tqdm
from selenium.webdriver.common.alert import Alert
import os

init()
def Carga():
    loop = tqdm(total=50000, position=0, leave=False)
    for k in range(50000):
        loop.set_description(Fore.BLUE + "Loading .....".format(k) + Fore.RESET)
        loop.update(1)
    loop.close()

def verify():
    if os.path.isfile("/usr/bin/geckodriver") == True:
        LogoCero()
        print("{} El archivo si existe {} <Ejecutando Script> {}".format(Fore.BLUE, Fore.GREEN, Fore.RESET))
    else:
        LogoCero()
        print("{} el archivo no existe, {} comenzando DESCARGA.... {}".format(Fore.RED, Fore.WHITE, Fore.RESET))
        Carga()
        os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz")
        os.system("sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver'")
        os.system("sudo chmod +x /usr/bin/geckodriver")
        os.system("rm geckodriver-v0.26.0-linux64.tar.gz")


def main():
    LogoCero()
    Carga()
    verify()

    try:
        txt = open("list.txt", "r")
        for i, linea in enumerate(txt):
            #print("La linea seleccionada es", linea)
            datos = linea.split(" ")
            #print(datos)
            correo = str(datos[0])
            contraseña = str(datos[1])
            #print("correo", correo)
            #print("contraseña", contraseña)
            LogoTwo()
            print(Fore.WHITE+ "El numero es", i, Fore.RESET)
            driver = webdriver.Firefox(executable_path="geckodriver")
            #driver.maximize_window()
            driver.get('https://facebook.com')
            alert = Alert(driver)
            # alert.accept()
            alert.dismiss()
            Carga()
            Carga()
            email = driver.find_element_by_xpath('//*[@id="email"]')
            email.send_keys(str(correo))
            passcon = driver.find_element_by_xpath('//*[@id="pass"]')
            passcon.send_keys(str(contraseña))
            cli = driver.find_element_by_xpath('//*[@id="loginbutton"]')
            cli.click()
            Carga()
            Carga()

            driver.close()









        txt.close()



    except:
        
        print(Fore.RED + "Algo salio mal o termino el proceso")






if __name__ == '__main__':
    main()
