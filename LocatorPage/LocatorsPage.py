from selenium.webdriver.common.by import By


class LoginLocatorsPage:
    ENTER_USERNAME = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
    CLICK_LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")


class AddToCartLocatorsPage:
    CLICK_ADD_CART_BACK = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
    CLICK_ADD_CART1 = (By.XPATH, "/ html / body / div / div / div / div[2] / div / div / div / div[2] / div[2] / div[2] / button")
    CLICK_ADD_CART2 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button")
    CLICK_ADD_CART3 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button")
    CLICK_ADD_CART4 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/button")
    CLICK_ADD_CART5 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button")


class ViewCartLocatorsPage:
    CLICK_CART_ICON = (By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")


class CheckOutLocatorsPage:
    CLICK_CHECKOUT_ICON = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]")


class CheckOutInformationLocatorsPage:
    FILL_CHECKOUT_FIRSTNAME = (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")
    FILL_CHECKOUT_LASTNAME = (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")
    FILL_CHECKOUT_ZIPCODE = (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input")
    CLICK_CHECKOUT_CONTINUE_ICON = (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input")


class FinishedIconLocatorsPage:
    CLICK_ON_FINISH_ICON = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]")


class HomeIconLocatorsPage:
    CLICK_ON_HOME_ICON = (By.XPATH, "/html/body/div/div/div/div[2]/button")
