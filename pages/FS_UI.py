import allure
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("FS Travel UI Tests")
class FS_UI:

    locators = {
        "locator_city_departure": ".departure-city-field__pinput_input",
        "locator_who_coming": ".tourists-field__body_tourists",
        "locator_increase": ".tourists-popup__adults_inc",
        "locator_decrease": ".tourists-popup__adults_dec",
        "locator_arrival": ".arrival-country-field__pinput_input",
        "locator_find": ".v-btn-yellow.tour-search__button.h-64",
        "locator_recommend": ".img-arrow-down",
        "locator_ascending_pricemodal": "//*[contains(@class, 'modal-text') and normalize-space()='По возрастанию цены']",
        "locator_popup": ".popmechanic-close",
        "locator_popup_luck": "button.close"
    }

    @allure.step("Инициализация FS_UI")
    def __init__(self, driver):
        """Инициализация класса FS_UI, выставление ожидания и значения количества взрослых по умолчанию"""

        with allure.step("Инициализация класса FS_UI"):
            self.driver = driver
        with allure.step("Выставление ожидания"):
            self.wait = WebDriverWait(driver, 20)
        # with allure.step("Установка значения количества взрослых по умолчанию"):
        #     self.previous_adults_count = 2

    @allure.step("Открытие главной страницы Fun&Sun")
    def open(self):
        """Открытие главной страницы сайта"""

        with allure.step("Открытие главной страницы Fun&Sun"):
            self.driver.get(
                "https://fstravel.com/?utm_referrer=https%3A%2F%2Fmy.sky.pro%2F/")

        with allure.step("Максимизация окна браузера"):
            self.driver.maximize_window()

        with allure.step("Ожидание загрузки логотипа"):
            logo = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".v-logo__img")))

    @allure.step("Ввод города отправления")
    def input_departure_city(self):
        """Ввод города отправления"""

        with allure.step("Получение локатора для города отправления"):
            locator_city_departure = self.locators["locator_city_departure"]

        with allure.step("Ввод города отправления"):
            city = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, locator_city_departure)))

        with allure.step("Очистка поля ввода города отправления"):
            city.clear()

        with allure.step("Ввод значения 'Москва' в поле города отправления"):
            city.send_keys("Москва")

    @allure.step("Ввод города отправления с дефисом")
    def input_departure_city_hyphen(self):
        """Ввод города с дефисом в названии"""

        with allure.step("Получение локатора для города отправления"):
            locator_city_departure = self.locators["locator_city_departure"]

        with allure.step("Ввод города отправления с дефисом"):
            city = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, locator_city_departure)))

        with allure.step("Очистка поля ввода города отправления"):
            city.clear()

        with allure.step("Ввод значения 'Санкт-Петербург' в поле города отправления"):
            city.send_keys("Санкт-Петербург")

    @allure.step("Ввод страны прибытия")
    def input_arrival_country(self):
        """Ввод страны прибытия"""

        with allure.step("Получение локатора для страны прибытия"):
            locator_arrival = self.locators["locator_arrival"]

        with allure.step("Ввод страны прибытия"):
            country_arrival = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, locator_arrival)))

        with allure.step("Очистка поля ввода страны прибытия"):
            country_arrival.clear()

        with allure.step("Ввод значения 'Мальдивы' в поле страны прибытия"):
            country_arrival.send_keys("Мальдивы")

    @allure.step("Получение текущего количества взрослых")
    def get_current_adults_count(self):
         """Получает текущее количество взрослых"""

         with allure.step("Получение локатора для количества взрослых"):
             locator_who_coming = self.locators["locator_who_coming"]

         with allure.step("Получение текста с количеством взрослых"):
             who_coming = self.wait.until(
                 EC.element_to_be_clickable(
                     (By.CSS_SELECTOR, locator_who_coming)))
             text = who_coming.text

             import re
             numbers = re.findall(r'\d+', text)
             if numbers:
                 number = int(numbers[0])
             else:
                 number = 0  # Или выбросить исключение

             with allure.step("Возврат количества взрослых"):
                 return number      
            
    @allure.step("Нажатие на кнопку 'Кто едет'")
    def click_button_who_coming(self):
            """Нажатие на кнопку 'Кто едет'"""

            with allure.step("Получение локатора для кнопки 'Кто едет'"):
                locator_who_coming = self.locators["locator_who_coming"]

            with allure.step("Нажатие на кнопку 'Кто едет'"):
                who_coming = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, locator_who_coming)))
                who_coming.click()            

            

    @allure.step("Увеличение количества взрослых")
    def increase_number_adults(self):
        """Увеличивает количество взрослых в форме поиска"""

        with allure.step("Получение локатора для увеличения количества взрослых"):
            locator_increase = self.locators["locator_increase"]

        with allure.step("Получение предыдущего количества взрослых"):
            self.previous_adults_count = self.get_current_adults_count()

        with allure.step("Нажатие на кнопку увеличения количества взрослых"):
            increase_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, locator_increase)))
            increase_button.click()

    @allure.step("Уменьшение количества взрослых")
    def decrease_number_adults(self):
        """Уменьшает количество взрослых в форме поиска"""

        with allure.step("Получение локатора для уменьшения количества взрослых"):
            locator_decrease = self.locators["locator_decrease"]

        with allure.step("Получение предыдущего количества взрослых"):
            self.previous_adults_count = self.get_current_adults_count()

        with allure.step("Нажатие на кнопку уменьшения количества взрослых"):
            decrease_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, locator_decrease)))
            decrease_button.click()

    @allure.step("Нажатие на кнопку 'Найти'")
    def button_find(self):
        """Нажатие на кнопку 'Найти'"""

        with allure.step("Получение локатора для кнопки 'Найти'"):
            locator_find = self.locators["locator_find"]

        with allure.step("Нажатие на кнопку 'Найти'"):
            find_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, locator_find)))
            find_button.click()

    @allure.step("Закрытие всплывающих окон")
    def close_popups(self):
        """Закрытие всплывающих окон"""

        with allure.step("Ожидание появления и закрытие всплывающего окна"):
            locator_popup = self.locators["locator_popup"]
        with allure.step("Закрытие всплывающего окна"):
            popup_close = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, locator_popup)))
            popup_close.click()

        with allure.step("Ожидание появления и закрытие всплывающего окна 'Испытайте вашу удачу'"):
            locator_popup_luck = self.locators["locator_popup_luck"]
        with allure.step("Закрытие всплывающего окна 'Испытайте вашу удачу'"):
             popup_close_luck = self.wait.until(
                 EC.element_to_be_clickable((By.CSS_SELECTOR, locator_popup_luck)))
             popup_close_luck.click()

    @allure.step("Нажатие на кнопку 'Рекомендации для вас'")
    def button_recommend(self):
        """Нажатие на кнопку 'Рекомендации для вас'"""

        with allure.step("Получение локатора для кнопки 'Рекомендации для вас'"):
            locator_recommend = self.locators["locator_recommend"]

        with allure.step("Нажатие на кнопку 'Рекомендации для вас'"):
            recommend_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, locator_recommend)))
            recommend_button.click

    @allure.step("Нажатие на кнопку 'По возрастанию цены'")
    def button_ascending_pricemodal(self):
        """Нажатие на кнопку 'По возрастанию цены'"""

        with allure.step("Получение локатора для кнопки 'По возрастанию цены'"):
            locator_ascending_pricemodal = self.locators["locator_ascending_pricemodal"]

        with allure.step("Нажатие на кнопку 'По возрастанию цены'"):
            button_ascending_pricemodal = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator_ascending_pricemodal)))
            button_ascending_pricemodal.click

    def close_driver(self):
        """Закрытие драйвера"""

        with allure.step("Закрытие драйвера"):
            self.driver.quit()
       
