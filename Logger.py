import logging
from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('logfile.log')
formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler) 
logger.setLevel(logging.INFO)
logger.debug("A debug statement is executed")

def info(string):
    logger.info(string)
def warning(string):
    logger.warning(string)  
def error(string):
    logger.error(string)
def critical(string):
    logger.critical(string)

driver = webdriver.Chrome(executable_path="./chromedriver")
def test_log():
    driver.get('https://bilet.railways.kz/login')
    driver.maximize_window()
    driver.find_element(By.ID, "username").send_keys('dbdduman@gmail.com')
    driver.find_element(By.ID, "password").send_keys('Duk@nuk@2003!')
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[1]/form/button").click()

    info('Login with selenium login button is working')
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[1]/div[2]/a[3]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/a[5]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/div[3]/div[1]/div[1]/div/button[2]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div/div/div[3]/form/button").click()
    info('Finding flights with selenium search button is working')
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[4]/table/tbody/tr[1]/td[5]/table/tfoot/tr/td/button").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[4]/div/table/tbody/tr[1]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[4]/div/table/tbody/tr[2]/td/div[2]/div/div[1]/div[2]/div/div[3]/div[4]").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[4]/div/table/tbody/tr[2]/td/button").click()
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/div/div/div[3]/div[3]/input').send_keys('047928976')#D
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/div/div/div[4]/div[1]/input').send_keys('Думан')#S
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/div/div/div[4]/div[2]/input').send_keys('Дыбысбай')#N
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/div/div/div[4]/div[3]/input').send_keys('Дулатжанулы')#F
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/div/div/div[5]/div[1]/input').send_keys('030925551170')#iin
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/div/div/div[6]/div[1]/input').send_keys('7777777777')
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[5]/div[2]/div/div/label').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[5]/div[3]/div/button').click()
    info('An information statement is executed')
    warning('A warning message is executed')


