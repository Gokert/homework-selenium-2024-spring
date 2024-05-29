from ui.pages.base_page import BasePage
from ui.locators.pa_legal_entity_locators import PALegalEntityLocators
from selenium.webdriver.support.select import Select

from selenium.common.exceptions import TimeoutException

import allure

from selenium.webdriver.common.by import By
import time

class PALegalEntityPage(BasePage):
    locators = PALegalEntityLocators()

    @allure.step("Нажатие на иконку ВК")
    def click_to_VK_ico(self):
        self.click(self.locators.LOCATOR_VK_ICO)

    @allure.step("Нажатие на имя пользователя в панели сверху")
    def click_to_user_name(self):
        self.click(self.locators.LOCATOR_USER_NAME)

    @allure.step("Нажатие на колокольчик в панели сверху")
    def click_to_bell(self):
        self.click(self.locators.LOCATOR_BELL)
    
    @allure.step("Получение теста полей в форме 'Уведомления'")
    def check_bell_text_field(self):
        text1 = self.get_text(self.locators.LOCATOR_BELL_NOTIFICATION)
        text2 = self.get_text(self.locators.LOCATOR_BELL_NOT_NOTIFICATION)
        text3 = self.get_text(self.locators.LOCATOR_BELL_TEXT)
        return [text1, text2, text3]

    @allure.step("Нажатие на иконку пользователя в панели сверху")
    def click_to_user_ico(self):
        self.click(self.locators.LOCATOR_USER_ICO)

    @allure.step("Выход из аккаунта пользователя")
    def user_log_out(self):
        self.click_to_user_ico()
        self.click(self.locators.LOCATOR_LOG_OUT)

    @allure.step("Нажатие на кнопку 'Помощь' в панели слева")
    def click_to_help_button(self):
        self.click(self.locators.LOCATOR_HELP_BUTTON)
    
    @allure.step("Переход по ссылкам в выпадающем меню 'Помощь' в панели слева")    
    def redirect_to_help_button(self, link_num):
        CURRENT_LOCATOR_HELP_BUTTON_REDIRECT = self.locators.LOCATOR_HELP_BUTTON_REDIRECT(link_num)
        try:
            self.click(CURRENT_LOCATOR_HELP_BUTTON_REDIRECT)
        except TimeoutException:
            self.click_to_help_button()
            self.click(CURRENT_LOCATOR_HELP_BUTTON_REDIRECT)

    @allure.step("Нажатие на кнопку 'Клиенты' в панели слева")
    def click_to_clients(self):
        self.click(self.locators.LOCATOR_CLIENTS)

    @allure.step("Нажатие на кнопку 'Бюджет' в панели слева")
    def click_to_budget(self):
        self.click(self.locators.LOCATOR_BUDGET)
    
    @allure.step("Указание реквизитов в вкладке 'Бюджет' в панели слева")    
    def specify_banking_details(self):
        self.click(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS)
        # self.click(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_CLOSE)

    @allure.step("Нажатие на кнопку 'Права доступа' в панели слева")
    def click_to_access_right(self):
        self.click(self.locators.LOCATOR_ACCESS_RIGHT)
        
    @allure.step("Добавление менеджера в вкладке 'Права доступа' в панели слева")
    def addManager(self, name, acc):
        self.click(self.locators.LOCATOR_ADD_MANAGER)
        self.find_clickable(self.locators.LOCATOR_ADD_MANAGER_FIO).send_keys(name)
        self.find_clickable(self.locators.LOCATOR_ADD_MANAGER_FIO).send_keys(acc)
        self.click(self.locators.LOCATOR_ADD_MANAGER_NEXT_BUTTON)
        self.click(self.locators.LOCATOR_ADD_MANAGER_CLOSE)

    @allure.step("Раскрытие чата с поддержкой")
    def open_support_iframe(self, wait_time):
        self.switch_to_iframe(self.find((By.XPATH, ".//div[@id='vk_community_messages']/iframe"),wait_time))
        self.switch_to_iframe(self.find((By.XPATH, ".//iframe"),wait_time))
        self.click((By.XPATH, ".//div[@id='root']/div/section/div"),wait_time)

    @allure.step("Сворачивание чата с поддержкой")
    def close_support_iframe(self, wait_time):
        self.click((By.XPATH, ".//button[@class='SAKIconButton']"),wait_time)
    
    @allure.step("Заполнение данных компании")
    def set_company(self):
        company_config = {
            'inn': "2141341243",
            'name': "testCompany",
            'kpp': "123456789",
            'ogrn': "1234567890123"
            # 'addressIndex': "124323",
            # 'addressCity': "123423",
            # 'addressStreet': "123423",
            # 'addressHouse': "423",
            # 'contactorName': "AlfaIV",
            # 'phone': "35435345345",
            # 'site': "https://example.ru",
            # 'resp_for_doc': ,
            # 'resp_for_doc_phone': ,
            # 'resp_for_doc_email': "https://example.ru",
        }
        for field in company_config.keys():
            self.type_text(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_COMPANY(field), company_config[field])
        self.click(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_NEXT)
        self.click(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_DROPBOX_CLICK)
        time.sleep(5)

        select = Select(self.find((By.XPATH, ".//select[@name='addressRegion']")))
        select.select_by_index(0)
        # self.dropbox_select(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_DROPBOX,2)
        # time.sleep(10)
        # self.click(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_NEXT)
        # self.click(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_NEXT)
        