import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from LocatorPage.LocatorsPage import LoginLocatorsPage, AddToCartLocatorsPage, ViewCartLocatorsPage, \
    CheckOutLocatorsPage, CheckOutInformationLocatorsPage, FinishedIconLocatorsPage, HomeIconLocatorsPage


class LoginActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    # To set up Login Page (Username,Password and SubmitButton)
    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorsPage.ENTER_USERNAME))
        enter_username.send_keys(username)
        time.sleep(2)

    def enter_password(self, username):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorsPage.ENTER_PASSWORD))
        enter_password.send_keys(username)
        time.sleep(2)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorsPage.CLICK_LOGIN_BUTTON))
        click_login_button.click()
        time.sleep(2)


class AddToCartActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_cartBack(self):
        click_add_cartBack = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART_BACK))
        click_add_cartBack.click()
        time.sleep(5)

    def click_add_cart1(self):
        click_add_cart1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART1))
        click_add_cart1.click()
        time.sleep(5)

    def click_add_cart2(self):
        click_add_cart2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART2))
        click_add_cart2.click()
        time.sleep(5)

    def click_add_cart3(self):
        click_add_cart3 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART3))
        click_add_cart3.click()
        time.sleep(5)

    def click_add_cart4(self):
        click_add_cart4 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART4))
        click_add_cart4.click()
        time.sleep(5)

    def click_add_cart5(self):
        click_add_cart5 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART5))
        click_add_cart5.click()
        time.sleep(5)


class ViewCartActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        click_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ViewCartLocatorsPage.CLICK_CART_ICON))
        click_cart_icon.click()
        time.sleep(5)


class CheckOutActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_icon(self):
        click_checkout_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutLocatorsPage.CLICK_CHECKOUT_ICON))
        click_checkout_icon.click()
        time.sleep(5)


class CheckOutInformationActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_firstname(self, firstname):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.FILL_CHECKOUT_FIRSTNAME))
        fill_checkout_firstname.send_keys(firstname)
        time.sleep(5)

    def fill_checkout_lastname(self, lastname):
        fill_checkout_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.FILL_CHECKOUT_LASTNAME))
        fill_checkout_lastname.send_keys(lastname)
        time.sleep(5)

    def fill_checkout_zipcode(self, zipcode):
        fill_checkout_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.FILL_CHECKOUT_ZIPCODE))
        fill_checkout_zipcode.send_keys(zipcode)
        time.sleep(5)

    def click_checkout_confirmation_icon(self):
        click_checkout_confirmation_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.CLICK_CHECKOUT_CONTINUE_ICON))
        click_checkout_confirmation_icon.click()
        time.sleep(5)


class FinishedIconActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_finish_icon(self):
        click_on_finish_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FinishedIconLocatorsPage.CLICK_ON_FINISH_ICON))
        click_on_finish_icon.click()
        time.sleep(5)


class HomeIconActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_home_icon(self):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomeIconLocatorsPage.CLICK_ON_HOME_ICON))
        fill_checkout_firstname.click()
        time.sleep(5)
