from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPageFS import MainPage_FS


class FS_UI:

    locators = {
        "locator_city_departure" : ".departure-city-field__pinput_input",
        "locator_who_coming" : ".tourists-field__body_title",
        "locator_increase" : ".tourists-popup__adults_inc",
        "locator_decrease" : ".tourists-popup__adults_dec",
        "locator_arrival" : ".arrival-country-field__pinput_input",
    }
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.previous_adults_count = 2

    def open(self):

        """Открытие главной страницы сайта"""
        self.driver.get("https://fstravel.com/?utm_referrer=https%3A%2F%2Fmy.sky.pro%2F/")
        self.driver.maximize_window()
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".v-logo__img")))


    def input_departure_city(self):
         """Ввод города отправления"""
         locator_city_departure = ".departure-city-field__pinput_input"
         city = self.wait.until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, locator_city_departure))
         )
         city.clear()
         city.send_keys("Москва")
            
    def input_departure_city_hyphen(self):
         """Ввод города с дефисом в названии"""
         locator_city_departure = ".departure-city-field__pinput_input"
         city = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_city_departure)))
         city.clear()
         city.send_keys("Санкт-Петербург")

    def input_arrival_country(self):
        """Ввод страны прибытия"""
        locator_arrival = ".arrival-country-field__pinput_input"
        country_arrival = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_arrival)))
        country_arrival.clear()
        country_arrival.send_keys("Мальдивы")


    def get_current_adults_count(self):
         """Получает текущее количество взрослых"""

         locator_who_coming = ".tourists-field__body_title"
         who_coming = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_who_coming)))
         text = who_coming.text

         import re
         numbers = re.findall(r'\d+', text)
         if numbers:
                number = int(numbers[0])
         else:
                number = 0  # Или выбросить исключение
            
         assert number == self.previous_adults_count
         return number


    def increase_number_adults(self):
         """Увеличивает количество взрослых в форме поиска"""
         locator_increase = ".tourists-popup__adults_inc"

         self.previous_adults_count = self.get_current_adults_count()

         increase_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_increase)))
         increase_button.click()
        
         current_count = self.get_current_adults_count()
         assert current_count > self.previous_adults_count


    def decrease_number_adults(self):
         """Уменьшает количество взрослых в форме поиска"""
         
         locator_decrease = ".tourists-popup__adults_dec"
         self.previous_adults_count = self.get_current_adults_count()
         decrease_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_decrease)))
         decrease_button.click()
         current_count = self.get_current_adults_count()
         assert current_count < self.previous_adults_count
    
    def button_find(self):
         """Нажатие на кнопку 'Найти'"""
         locator_find = "v-btn-yellow.tour-search__button.h-56"

         find_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_find)))
         find_button.click()
    


        