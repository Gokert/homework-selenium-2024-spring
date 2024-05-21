import os
import time
from selenium.webdriver.support import expected_conditions as EC

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.auth_page import AuthPage

from ui.pages.cabinet_page import CabinetPage
from ui.pages.settings_page import SettingsPage
from ui.pages.main_page import MainPage
from ui.pages.pa_legal_entity_page import PALegalEntityPage


@pytest.fixture
def main_page(driver):
    driver.get(MainPage.url)
    return MainPage(driver=driver)

@pytest.fixture
def driver(config):
    browser = config.get('browser')
    url = config.get('url')
    selenoid = config.get('selenoid')
    vnc = config.get('vnc')
    options = Options()

    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def credentials_with_cabinet():
    load_dotenv()
    return os.getenv("LOGIN_NAME"), os.getenv("PASSWORD")


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture
def cabinet_page(driver, credentials_with_cabinet, auth_page):
    auth_page.login(*credentials_with_cabinet)
    return CabinetPage(driver=driver)

@pytest.fixture
def settings_page(driver, cabinet_page):
    driver.get(SettingsPage.url)
    return SettingsPage(driver=driver)


@pytest.fixture(scope='session')
def credentials_legal_entity():
    load_dotenv()
    return os.getenv("LOGIN_NAME_LEGAL_ENTITY"), os.getenv("PASSWORD_LEGAL_ENTITY")

@pytest.fixture
def legal_entity_page(driver, credentials_legal_entity, auth_page):
    # driver.get(SettingsPage.url)
    auth_page.login(*credentials_legal_entity)
    return PALegalEntityPage(driver=driver)
