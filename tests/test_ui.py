import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from pages.FS_UI import FS_UI

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

wait = WebDriverWait(driver, 20)

fs_ui = FS_UI(driver)


@allure.title("Fun&Sun UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Поиск тура с городом на кириллице")
@allure.feature("FS Travel UI-тесты")
def test_search_tour_ui():
    """Поиск тура с городом на кириллице"""

    fs_ui.open()
    fs_ui.input_departure_city()
    fs_ui.input_arrival_country()
    fs_ui.get_current_adults_count()
    assert fs_ui.get_current_adults_count == 2
    fs_ui.button_find()


@allure.title("Fun&Sun UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Поиск тура с городом, в названии которого есть деифис")
@allure.feature("FS Travel UI-тесты")
def test_search_tour_with_city_hyphen_ui():
    """Поиск тура с городом, в названии которого есть деифис"""

    fs_ui.open()
    fs_ui.input_departure_city_hyphen()
    fs_ui.input_arrival_country()
    fs_ui.get_current_adults_count()
    assert fs_ui.get_current_adults_count == 2
    fs_ui.button_find()


@allure.title("Fun&Sun UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Поиск тура с увеличением количества взрослых")
@allure.feature("FS Travel UI-тесты")
def test_search_tour_with_increase_number_ui():
    """Поиск тура с увеличением количества взрослых"""

    fs_ui.open()
    fs_ui.input_departure_city()
    fs_ui.input_arrival_country()
    initial_count = fs_ui.get_current_adults_count()
    fs_ui.increase_number_adults()
    new_count = fs_ui.get_current_adults_count()
    assert new_count == initial_count + 1
    fs_ui.button_find()


@allure.title("Fun&Sun UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Поиск тура с уменьшением количества взрослых")
@allure.feature("FS Travel UI-тесты")
def test_search_tour_with_decrease_number_ui():
    """Поиск тура с уменьшением количества взрослых"""

    fs_ui.open()
    fs_ui.input_departure_city()
    fs_ui.input_arrival_country()
    initial_count = fs_ui.get_current_adults_count()
    fs_ui.decrease_number_adults()
    new_count = fs_ui.get_current_adults_count()
    assert new_count == initial_count + 1
    fs_ui.button_find()


@allure.title("Fun&Sun UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Сортировка туров по возрастанию цены")
@allure.feature("FS Travel UI-тесты")
def test_sort_by_ascending_price_ui():
    """Сортировка туров по возрастанию цены"""

    fs_ui.open()
    fs_ui.input_departure_city()
    fs_ui.input_arrival_country()
    fs_ui.get_current_adults_count()
    assert fs_ui.get_current_adults_count == 2
    fs_ui.button_find()
    fs_ui.button_recommend()
    fs_ui.button_ascending_pricemodal
