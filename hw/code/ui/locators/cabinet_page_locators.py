from selenium.webdriver.common.by import By

class CabinetPageLocators():
    @staticmethod
    def LEFT_MENU(section):
        return By.XPATH, f"//*[@data-testid='left-menu']//span[text()='{section}']"

    NOTIFICATIONS_MODAL_PAGE = (By.XPATH, "//*[(@class, 'vkuiModalPage__in-wrap')]")

