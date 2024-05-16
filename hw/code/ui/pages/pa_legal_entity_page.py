from ui.pages.base_page import BasePage
from ui.locators.pa_legal_entity_locators import PALegalEntityLocators

from selenium.common.exceptions import TimeoutException

import allure

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
        self.click(self.locators.LOCATOR_BUDGET_SPECIFY_DETAILS_CLOSE)

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

    # def open_support_iframe(self, wait_time):
    #     time.sleep(wait_time)
    #     self.click((By.XPATH, "//div[@id='vk_community_messages']"))
    #     self.switch_to_iframe(self.locators.LOCATOR_SUPPORT_IFRAME)