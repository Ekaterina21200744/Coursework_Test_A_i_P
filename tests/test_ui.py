from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from FS_UI import FS_UI 
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 20)

fs_ui = FS_UI(driver)

def test_search_tour_():
    fs_ui.open
    fs_ui.input_departure_city
    fs_ui.input_arrival_country
    fs_ui.get_current_adults_count
    fs_ui.button_find

def test_searc_tour_with_city_hyphen():
    fs_ui.open
    fs_ui.input_departure_city_hyphen
    fs_ui.input_arrival_country
    fs_ui.get_current_adults_count
    fs_ui.button_find

