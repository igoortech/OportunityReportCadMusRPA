from typing import List 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from Libs.LocalStorage import LocalStorage
from Libs.SendEmail import *
from Libs.LocalStorage import *
import pandas as pd
import json

def OPEN_PAGE()->webdriver:
    driver = webdriver.Chrome()
    driver.get("https://cadmus.com.br/vagas-tecnologia/")

    #WAITING  FOR THE PAGE LOAD ELEMENTS
    wdw = WebDriverWait(driver, 30)
    locator = (By.CSS_SELECTOR, '#pfolio')
    wdw.until(
        presence_of_element_located(locator)
        )  
    #WHEN PAGE IS LOEADED RETURN  DRIVER
    return driver


def GET_OPORTUNITIES(driver:webdriver)->List:

    storage = LocalStorage(driver) #LOCAL STORAGE 
    STORAGE_DETAILS = json.loads(storage.get("vagas")) # GET ALL OPORTUNITIES STORED ON LOCALSTORAGE

    # GET ONLY NECESSARY FIELDS FROM EACH OPORTUNITY
    DATA = [
        {
            "Oportunity": box['name'],
            "Locale": box['cidade_Regi_o__c'],
            "Detail": box['descricao_da_vaga__c'].replace("<br>", "")
        }

        for box in STORAGE_DETAILS
    ]
    return DATA


def EXPORT_TO_EXCEL(DATA:List):
    DF = pd.DataFrame(DATA)
    DF.to_excel("Output/ReportOportunities.xlsx",index=False)


def SEND_EMAIL_TO_AREA(driver:webdriver):

    # SUBJECT FROM THE EMAIL
    Subject = "Relatório de Vagas Disponíveis CadMus"
    SetSubject(Subject)

    #BODY HTML 
    Body = "<h2>Relatório de vagas disponíveis Cadmus</h2><p>Segue Excel com  vagas disponíveis do portal da CadMus para análise<p>"
    SetBody(Body)

    # WHO MUST RECIEVE   E-MAIL
    To = "email_must_recieve@gmail.com"
    SetTo(To)

    #PATH FROM EXCEL FILE GENERATE
    Excel = "Output/ReportOportunities.xlsx"
    SetPdf(Excel)
    
    #SENDING E-MAIL WITH THE
    Send()

    #WHEN COMPLETED CLOSES 
    driver.quit()



#============================== VARIABLES

driver:         webdriver
OPORTUNITIES:   List

#============================== METHODS

driver          = OPEN_PAGE()
OPORTUNITIES    = GET_OPORTUNITIES(driver)
EXPORT_TO_EXCEL = EXPORT_TO_EXCEL(OPORTUNITIES)
SEND_EMAIL      = SEND_EMAIL_TO_AREA(driver)


