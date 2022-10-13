import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
from allure_commons.types import AttachmentType


class TestAll:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")

    def teardown(self):
        self.driver.quit()

    @allure.feature('Open Pages')
    @allure.story("Open Google ")
    @allure.severity('block')
    def test_google_find(self):
        self.driver.get('https://www.google.com/')
        with allure.step('Took Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Open Pages')
    @allure.story("Open Yandex ")
    @allure.severity('block')
    def test_yandex_find(self):
        self.driver.get('https://yandex.kz/')
        with allure.step('Took Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('Open Pages')
    @allure.story("Open youtube ")
    @allure.severity('block')
    def test_youtube_find(self):
        self.driver.get('https://www.youtube.com/')
        with allure.step('Took Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    
    @allure.feature('Open Pages')
    @allure.story("Open youtube ")
    @allure.severity('block')
    def test_youtube_find(self):
        self.driver.get('https://www.youtubedasdas.com/')
        with allure.step('Took Screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)