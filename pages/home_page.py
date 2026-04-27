from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

import pytest

class HomePagePOM:
    """Page object for the Crypto Finance home page.
    
    Provides methods for navigation, language switching,
    and interaction with the home page widgets.
    """

    URL = "https://www.crypto-finance.com/"
    EXPECTED_TITLE_CONTAINS = "Crypto Finance"
    MAIN_NAV = ".elementor-sticky--active .elementor-nav-menu--main > ul > li > a"

    LOGO = (By.CSS_SELECTOR,".elementor-sticky--active [data-id='881ad7a'] a")
    NAV_SOLUTIONS = (By.CSS_SELECTOR, f"{MAIN_NAV}[href*='/solutions/']")
    NAV_NEWS = (By.CSS_SELECTOR, f"{MAIN_NAV}[href*='/news/']")
    NAV_ABOUT = (By.CSS_SELECTOR, f"{MAIN_NAV}[href*='/about-us/']")
    NAV_CAREER = (By.CSS_SELECTOR, f"{MAIN_NAV}[href*='/life-at-crypto-finance/']")
    NAV_CONTACT = (By.CSS_SELECTOR, f"{MAIN_NAV}[href*='/contact/']")
    LOGIN_BUTTON = (By.CSS_SELECTOR,".elementor-sticky--active [data-id='0edea8f'] a")
    LANGUAGE_SWITCHER = (By.CSS_SELECTOR, ".elementor-sticky--active .languageSwitchHeader")
    LANG_EN = (By.CSS_SELECTOR,".elementor-sticky--active .languageSwitchHeader a[hreflang='en']")
    LANG_DE = (By.CSS_SELECTOR,".elementor-sticky--active .languageSwitchHeader a[hreflang='de']")
    LANG_PT = (By.CSS_SELECTOR,".elementor-sticky--active .languageSwitchHeader a[hreflang='pt-pt']")
    LANG_ES = (By.CSS_SELECTOR,".elementor-sticky--active .languageSwitchHeader a[hreflang='es']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def goto(self):
        # navigates to URL
        self.driver.get(self.URL)

    def click_solutions(self):
        self.click(self.NAV_SOLUTIONS)
        #also valid
        #self.driver.find_element(*self.NAV_SOLUTIONS)
        return self

    def click_news(self):
        self.click(self.NAV_NEWS)
        return self

    def click_about(self):
        self.click(self.NAV_ABOUT)
        return self

    def click_career(self):
        self.click(self.NAV_CAREER)
        return self

    def click_contact(self):
        self.click(self.NAV_CONTACT)
        return self

    def change_language(self,lang_code): # changes language with the codes (en/de/pt-pt/es)
        languages = {
            "en": self.LANG_EN,
            "de": self.LANG_DE,
            "pt-pt": self.LANG_PT,
            "es": self.LANG_ES,
        }
        
        if lang_code not in languages:
            raise ValueError(
                f"Unsupported language code: '{lang_code}'. "
                f"Available: {list(languages.keys())}"
            )
        
        self.click(languages[lang_code])
        return self
        
    def is_login_button_visible(self): # returns boolean
        return self.is_visible(self.LOGIN_BUTTON)
    
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False