import pytest
from pages.home_page import HomePagePOM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# TEST 1 — Title page correct
def test_title_correct(driver):
    home = HomePagePOM(driver)
    home.goto()
    # contains "Crypto Finance"
    home.wait.until(EC.title_contains("Crypto Finance"))
    assert "Crypto Finance" in home.driver.title

# TEST 2 — Logo is visible
def test_logo_visible(driver):
    home = HomePagePOM(driver)
    home.goto()
    # logo (link to home) is visible
    home.wait.until(EC.visibility_of_element_located(home.LOGO))

# TEST 3 — button Login visible and destiny correct 
def test_login_visible(driver):
    home = HomePagePOM(driver)
    home.goto()
    # button is visible
    login = home.wait.until(EC.visibility_of_element_located(home.LOGIN_BUTTON))
    assert home.is_login_button_visible()
    #  href contains lynx.crypto-finance.com
    assert "lynx.crypto-finance.com" in login.get_attribute("href")
    
    # Store the ID of the original window
    original_window = home.driver.current_window_handle

    login.click()
    home.wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in home.driver.window_handles:
        if window_handle != original_window:
            home.driver.switch_to.window(window_handle)
            break

    home.wait.until(EC.url_contains("lynx.crypto-finance.com"))



# TEST 5 — Language switcher has 4 languages
@pytest.mark.parametrize("lang", [
        HomePagePOM.LANG_DE,
        HomePagePOM.LANG_EN,
        HomePagePOM.LANG_PT,
        HomePagePOM.LANG_ES,
    ])
def test_languages_visible(driver, lang):
    home = HomePagePOM(driver)
    home.goto()
    
    #  4 elements language are visible (EN, DE, PT, ES)
    home.wait.until(EC.visibility_of_element_located(lang))
    

