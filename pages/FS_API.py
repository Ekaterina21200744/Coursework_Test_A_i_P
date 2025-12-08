from config import BASE_API_URL
import requests
import allure
from pages.config import BASE_API_URL


class FS_API:
    @allure.step("Инициализация FS_API")
    def __init__(self):
        """Инициализация класса FS_API и установка базового URL для API"""

        self.url = BASE_API_URL

    @allure.step("Поиск тура по стране прибытия через API")
    def search_by_country(self, departureCityId, arrivalCountryId,
                          minStartDate, maxStartDate, minNightsCount, maxNightsCount, adults):
        """Поиск тура по стране прибытия через API"""

        with allure.step("Формирование параметров запроса и заголовков"):
            params = {
                "departureCityId": departureCityId,
                "arrivalCountryId": arrivalCountryId,
                "minStartDate": minStartDate,
                "maxStartDate": maxStartDate,
                "minNightsCount": minNightsCount,
                "maxNightsCount": maxNightsCount,
                "adults": adults,
                "flightTypes": "all",
                "sort": "recommendations_FS"

            }

            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            }
        with allure.step("Выполнение GET-запроса к API с заданными параметрами и заголовками"):
            response = requests.get(
                self.url + "get-by-country",
                params=params,
                headers=headers)
            return response

    def sort_ascending_pricemodal(self):
        import requests


class FS_API:
    @allure.step("Инициализация FS_API")
    def __init__(self):
        """Инициализация класса FS_API и установка базового URL для API"""

        self.url = BASE_API_URL

    @allure.step("Поиск тура по стране прибытия через API")
    def search_by_country(self, departureCityId, arrivalCountryId,
                          minStartDate, maxStartDate, minNightsCount, maxNightsCount, adults):
        """Поиск тура по стране прибытия через API"""

        with allure.step("Формирование параметров запроса и заголовков"):
            params = {
                "departureCityId": departureCityId,
                "arrivalCountryId": arrivalCountryId,
                "minStartDate": minStartDate,
                "maxStartDate": maxStartDate,
                "minNightsCount": minNightsCount,
                "maxNightsCount": maxNightsCount,
                "adults": adults,
                "flightTypes": "all",
                "sort": "recommendations_FS"

            }

            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            }
        with allure.step("Выполнение GET-запроса к API с заданными параметрами и заголовками"):
            response = requests.get(
                self.url + "get-by-country",
                params=params,
                headers=headers)
            return response

    @allure.step("Сортировка туров по возрастанию цены через API")
    def sort_ascending_price(self, departureCityId, arrivalCountryId,
                             minStartDate, maxStartDate, minNightsCount, maxNightsCount, adults):
        """Сортировка туров по возрастанию цены через API"""

        with allure.step("Формирование параметров запроса для сортировки по возрастанию цены"):
            params_sorted_max = {
                "departureCityId": departureCityId,
                "arrivalCountryId": arrivalCountryId,
                "minStartDate": minStartDate,
                "maxStartDate": maxStartDate,
                "minNightsCount": minNightsCount,
                "maxNightsCount": maxNightsCount,
                "adults": adults,
                "flightTypes": "all",
                "sort": "max"
            }

            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "x-requested-with": "XMLHttpRequest"
            }
        with allure.step("Выполнение GET-запроса к API для получения отсортированных туров"):
            response_sorted = requests.get(
                self.url + "get-by-country",
                params=params_sorted_max,
                headers=headers)
            return response_sorted

    def sort_descending_pirce(self, departureCityId, arrivalCountryId,
                              minStartDate, maxStartDate, minNightsCount, maxNightsCount, adults):
        """Сортировка туров по убыванию цены через API"""

        with allure.step("Формирование параметров запроса для сортировки по возрастанию цены"):
            params_sorted_min = {
                "departureCityId": departureCityId,
                "arrivalCountryId": arrivalCountryId,
                "minStartDate": minStartDate,
                "maxStartDate": maxStartDate,
                "minNightsCount": minNightsCount,
                "maxNightsCount": maxNightsCount,
                "adults": adults,
                "flightTypes": "all",
                "sort": "min"
            }

            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "x-requested-with": "XMLHttpRequest"
            }
        with allure.step("Выполнение GET-запроса к API для получения отсортированных туров"):
            response_sorted = requests.get(
                self.url + "get-by-country",
                params=params_sorted_min,
                headers=headers)
            return response_sorted

    def search_tour_city_spase(self, departureCityId, arrivalCountryId,
                               minStartDate, maxStartDate, minNightsCount, maxNightsCount, adults):
        """Поиск тура с городом, в названии которого есть пробел через API"""

        with allure.step("Формирование параметров запроса и заголовков"):
            params = {
                "departureCityId": departureCityId,
                "arrivalCountryId": arrivalCountryId,
                "minStartDate": minStartDate,
                "maxStartDate": maxStartDate,
                "minNightsCount": minNightsCount,
                "maxNightsCount": maxNightsCount,
                "adults": adults,
                "flightTypes": "all",
                "sort": "recommendations_FS"

            }

            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "x-requested-with": "XMLHttpRequest"
            }

        with allure.step("Выполнение GET-запроса к API с заданными параметрами и заголовками (город в названии которого есть пробел)"):
            response = requests.get(
                self.url + "get-by-country",
                params=params,
                headers=headers)
            return response
