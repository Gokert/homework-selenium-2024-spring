from selenium.webdriver.common.by import By

class CabinetPageLocators():
    @staticmethod
    def LEFT_MENU(section):
        return By.XPATH, f"//*[@data-testid='left-menu']//span[text()='{section}']"

    NOTIFICATIONS_MODAL_PAGE = (By.XPATH, "//*[(@class, 'vkuiModalPage__in-wrap')]")
    USER_AVATAR = (By.XPATH, "//*[contains(@class, 'userMenu_avatar__')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'userMenu_logoutButton__')]")
    VK_ICON = (By.XPATH, "//*[contains(@class, 'header_logo__')]")
    EDUCATION_BUTTON = (By.XPATH, "//*[contains(@data-route, 'onboarding')]")
    EDUCATION_MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_componentWrapper__')]")
    EDUCATION_EXIT = (By.XPATH, "//*[contains(@class, 'vkuiModalDismissButton')]")
    HELP_MODAL = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer__')]")
    HELP_ICON = (By.XPATH, "//*[@class='vkuiSimpleCell__content']//span[text()='Помощь']")

