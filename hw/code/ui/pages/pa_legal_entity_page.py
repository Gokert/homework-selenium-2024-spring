from ui.pages.base_page import BasePage
from ui.locators.pa_legal_entity_locators import PALegalEntityLocators

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
import time

class PALegalEntityPage(BasePage):
    locators = PALegalEntityLocators()

    def click_to_VK_ico(self):
        self.click(self.locators.LOCATOR_VK_ICO)

    def click_to_user_name(self):
        self.click(self.locators.LOCATOR_USER_NAME)

    def click_to_bell(self):
        self.click(self.locators.LOCATOR_BELL)
    
    # def check_bell_text_field(self):
    #     assert self.get_text((By.XPATH, ".//div[contains(@class, 'vkuiHeader__main')]/h2/span[1]/span[1]")) == "Уведомления"
    #     assert self.get_text((By.XPATH, ".//div[contains(@class, 'EmptyPlaceholder_wrapper__8LcAC')]/div[1]/h2")) == "Нет уведомлений"
    #     assert self.get_text((By.XPATH, ".//h4/span[1]/span[1]")) == "Как только у вас появятся уведомления, они отобразятся здесь"

    def click_to_user_ico(self):
        self.click(self.locators.LOCATOR_USER_ICO)

    def user_log_out(self):
        self.click_to_user_ico()
        self.click(self.locators.LOCATOR_LOG_OUT)

    def click_to_help_button(self):
        self.click(self.locators.LOCATOR_HELP_BUTTON)
    
    def redirect_to_help_button(self, link_num):
        REDIRECT_LOCATOR = (By.XPATH, f".//div[@class='Tooltip_tooltipContainer__P1b-O']/section[1]/a[{link_num}]/div[1]")
        try:
            self.click(REDIRECT_LOCATOR)
        except TimeoutException:
            self.click_to_help_button()
            self.click(REDIRECT_LOCATOR)

    def click_to_clients(self):
        self.click(self.locators.LOCATOR_CLIENTS)

    def click_to_budget(self):
        self.click(self.locators.LOCATOR_BUDGET)
    
    def specify_banking_details(self):
        self.click((By.XPATH, "//div[@class='vkuiPlaceholder__action']"))
        self.click((By.XPATH, "//div[@aria-label='Закрыть']"))

    def click_to_access_right(self):
        self.click(self.locators.LOCATOR_ACCESS_RIGHT)
    
    def addManager(self, name, acc):
        self.click(self.locators.LOCATOR_ADD_MANAGER)
        self.find_clickable((By.XPATH, ".//input[@name='managerFio']")).send_keys(name)
        self.find_clickable((By.XPATH, ".//input[@name='managerEmail']")).send_keys(acc)
        self.click((By.XPATH, ".//div[@class='ModalFooterSimple_container__rteom']/button[2]"))
        self.click((By.XPATH, "//div[@aria-label='Закрыть']"))

    # def open_support_iframe(self, wait_time):
    #     time.sleep(wait_time)
    #     self.click((By.XPATH, "//div[@id='vk_community_messages']"))
    #     self.switch_to_iframe(self.locators.LOCATOR_SUPPORT_IFRAME)