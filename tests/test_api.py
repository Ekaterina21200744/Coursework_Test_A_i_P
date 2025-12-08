import allure
from pages.FS_API import FS_API
from datetime import datetime, timedelta


now = datetime.now()
today = now.strftime('%Y-%m-%d')
in_week = (now + timedelta(days=7)).strftime('%Y-%m-%d')
month_ago = (now - timedelta(days=30)).strftime('%Y-%m-%d')


api = FS_API()


@allure.title("Fun&Sun API тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Поиск тура по стране прибытия через API")
@allure.feature("FS Travel API-тесты")
def test_search_by_country_api():
    """Поиск тура по стране прибытия через API"""

    resp = api.search_by_country("274286", "18498", today, in_week, 7, 7, 2)
    assert resp.status_code == 200


@allure.title("Fun&Sun API тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Сортировка туров по возрастанию цены через API")
@allure.feature("FS Travel API-тесты")
def test_sort_by_ascending_price_api():
    """Сортировка туров по возрастанию цены через API"""

    resp = api.sort_ascending_price("274286", "18498", today, in_week, 7, 7, 2)
    assert resp.status_code == 200


@allure.title("Fun&Sun API тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Сортировка туров по убыванию цены через API")
@allure.feature("FS Travel API-тесты")
def test_sort_by_descending_price_api():
    """Сортировка туров по убыванию цены через API"""

    resp = api.sort_descending_pirce(
        "274286", "18498", today, in_week, 7, 7, 2)
    assert resp.status_code == 200


@allure.title("Fun&Sun API тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Поиск тура с городом, в названии которого есть пробел через API")
@allure.feature("FS Travel API-тесты")
def test_search_city_space_api():
    """Поиск тура с городом, в названии которого есть пробел через API"""

    resp = api.search_tour_city_spase(
        "424885", "18498", today, in_week, 7, 7, 2)
    assert resp.status_code == 200


@allure.title("Fun&Sun API тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Поиск тура с невалидными данными через API")
@allure.feature("FS Travel API-тесты")
def test_search_tour_invalid_data_ui():
    """Поиск тура с невалидными данными через UI"""

    resp = api.sort_descending_pirce(
        "1111", "111111", month_ago, month_ago, 7, 7, 0)
    assert resp.status_code == 200
