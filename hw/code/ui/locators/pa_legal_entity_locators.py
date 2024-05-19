from selenium.webdriver.common.by import By

class PALegalEntityLocators:
    LOCATOR_VK_ICO = (By.CLASS_NAME, "header_left__cv9bp")
    LOCATOR_USER_NAME = (By.CLASS_NAME, "AccountSwitch_changeAccountButton__o5T9V")
    LOCATOR_BELL = (By.CLASS_NAME, "header_bellNotifications__vAHeR")
    LOCATOR_USER_ICO = (By.CLASS_NAME, "userMenu_avatar__oCUFq")
    LOCATOR_LOG_OUT = (By.XPATH, "//div[@class='vkuiPopover__in']/div[1]/div[@role='button']")
    LOCATOR_BUDGET = (By.XPATH, "//a[@data-route='budget']/div[2]")
    LOCATOR_ACCESS_RIGHT = (By.XPATH, "//a[@data-route='access_rights']/div[2]")
    LOCATOR_ADD_MANAGER = (By.XPATH, "//div[@data-testid='add-manager']/div[2]")
    LOCATOR_CLIENTS = (By.XPATH, "//a[@data-route='dashboardV2']/div[2]")
    LOCATOR_HELP_BUTTON = (By.CLASS_NAME, "Hint_hintTrigger__ixYRu")
    LOCATOR_SUPPORT_IFRAME = (By.XPATH, "//div[@id='vk_community_messages']/iframe")
    LOCATOR_BELL_NOTIFICATION = (By.XPATH, ".//div[contains(@class, 'vkuiHeader__main')]/h2/span[1]/span[1]")
    LOCATOR_BELL_NOT_NOTIFICATION = (By.XPATH, ".//div[contains(@class, 'EmptyPlaceholder_wrapper__8LcAC')]/div[1]/h2")
    LOCATOR_BELL_TEXT = (By.XPATH, ".//h4/span[1]/span[1]")
    @staticmethod
    def LOCATOR_HELP_BUTTON_REDIRECT(link_num):
        return (By.XPATH, f".//div[@class='Tooltip_tooltipContainer__P1b-O']/section[1]/a[{link_num}]/div[1]")
    LOCATOR_BUDGET_SPECIFY_DETAILS = (By.XPATH, "//div[@class='vkuiPlaceholder__action']")
    LOCATOR_BUDGET_SPECIFY_DETAILS_CLOSE = (By.XPATH, "//div[@aria-label='Закрыть']")
    LOCATOR_ADD_MANAGER_FIO = (By.XPATH, ".//input[@name='managerFio']")
    LOCATOR_ADD_MANAGER_MAIL = (By.XPATH, ".//input[@name='managerEmail']")
    LOCATOR_ADD_MANAGER_NEXT_BUTTON = (By.XPATH, ".//div[@class='ModalFooterSimple_container__rteom']/button[2]")
    LOCATOR_ADD_MANAGER_CLOSE = (By.XPATH, "//div[@aria-label='Закрыть']")
    LOCATOR_IFRAME1 = (By.XPATH, ".//div[@id='vk_community_messages']/iframe")
    LOCATOR_IFRAME2 = (By.XPATH, ".//iframe[@src='https://id.vk.com/messenger?peer_id=-212221031&scheme=bright_light&expanded=false&position=undefined&openSound=false&messageSound=true&mode=default&host_app_id=8077160&superapp_token=kw1gdmywk2Y3IsQesEez_-ZhsPuTUhgLIci5XXpg3rL66BL0apb7ynNglXdYp5rHcthc5DEpuKVH8lxN29obCxU_uQwZ5xFqLvoYkmHdXSThq2UOHNPsgv6SeCctu56qhHznrewwid4r0MtiSUbrVn_T42_xwxR2SZs7Z5H7XUAoYC-3B02oPAozLqbZP69KxbrG_tj1-Bvopa287l01QspQOjz0LwAZopDJJ_-UA9QoPpBH6OevmiSmzpkt-PhHcfrtkTVFaGqGKm83maCdouyP3ZSC_UNjtrGYn1rOdAOwdDGNTdXCyFxIJA_39DiXGfl33_JQ-2Lgm1N7qpf8LQzQpMqHQ5jnroiEOkmWbizzYPJb72HsehrvMzaUbN3EySqPHH2IgLxPI65aw3zbQpP76bowCutIcpalMWI6CnEEjeSIKWwJZmvqEUzJuBxo4mjtEYmnhnKrm2jNQD1_9yVevMMZ9IdKIiL0toIjzFTQCOkXb7euHYar40QRygad&origin=https%3A%2F%2Fvk.com']")