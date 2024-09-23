import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from LocatorPage.LocatorsPage import LoginLocatorsPage, AddToCartLocatorsPage, ViewCartLocatorsPage, \
    CheckOutLocatorsPage, CheckOutInformationLocatorsPage, FinishedIconLocatorsPage, HomeIconLocatorsPage, \
    AddToCartLocatorsPage1, ViewCartLocatorsPage1, CheckOutLocatorsPage1, CheckOutInformationLocatorsPage1, \
    FinishedIconLocatorsPage1, HomeIconLocatorsPage1, HomeIconLocatorsPage2, FinishedIconLocatorsPage2, \
    CheckOutInformationLocatorsPage2, CheckOutLocatorsPage2, ViewCartLocatorsPage2, AddToCartLocatorsPage2, \
    HomeIconLocatorsPage3, FinishedIconLocatorsPage3, CheckOutInformationLocatorsPage3, CheckOutLocatorsPage3, \
    ViewCartLocatorsPage3, AddToCartLocatorsPage3, HomeIconLocatorsPage5, FinishedIconLocatorsPage5, \
    CheckOutInformationLocatorsPage5, CheckOutLocatorsPage5, ViewCartLocatorsPage5, AddToCartLocatorsPage5, \
    HomeIconLocatorsPage4, FinishedIconLocatorsPage4, CheckOutInformationLocatorsPage4, CheckOutLocatorsPage4, \
    ViewCartLocatorsPage4, AddToCartLocatorsPage4


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
        time.sleep(2)

    # def click_add_cart1(self):
    #     click_add_cart1 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART1))
    #     click_add_cart1.click()
    #     time.sleep(5)

    # def click_add_cart2(self):
    #     click_add_cart2 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART2))
    #     click_add_cart2.click()
    #     time.sleep(5)
    #
    # def click_add_cart3(self):
    #     click_add_cart3 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART3))
    #     click_add_cart3.click()
    #     time.sleep(5)
    #
    # def click_add_cart4(self):
    #     click_add_cart4 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART4))
    #     click_add_cart4.click()
    #     time.sleep(5)
    #
    # def click_add_cart5(self):
    #     click_add_cart5 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART5))
    #     click_add_cart5.click()
    #     time.sleep(5)


class ViewCartActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        click_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ViewCartLocatorsPage.CLICK_CART_ICON))
        click_cart_icon.click()
        time.sleep(2)


class CheckOutActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_icon(self):
        click_checkout_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutLocatorsPage.CLICK_CHECKOUT_ICON))
        click_checkout_icon.click()
        time.sleep(2)


class CheckOutInformationActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_firstname(self, firstname):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.FILL_CHECKOUT_FIRSTNAME))
        fill_checkout_firstname.send_keys(firstname)
        time.sleep(2)

    def fill_checkout_lastname(self, lastname):
        fill_checkout_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.FILL_CHECKOUT_LASTNAME))
        fill_checkout_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_checkout_zipcode(self, zipcode):
        fill_checkout_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.FILL_CHECKOUT_ZIPCODE))
        fill_checkout_zipcode.send_keys(zipcode)
        time.sleep(2)

    def click_checkout_confirmation_icon(self):
        click_checkout_confirmation_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage.CLICK_CHECKOUT_CONTINUE_ICON))
        click_checkout_confirmation_icon.click()
        time.sleep(2)


class FinishedIconActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_finish_icon(self):
        click_on_finish_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FinishedIconLocatorsPage.CLICK_ON_FINISH_ICON))
        click_on_finish_icon.click()
        time.sleep(2)


class HomeIconActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_home_icon(self):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomeIconLocatorsPage.CLICK_ON_HOME_ICON))
        fill_checkout_firstname.click()
        time.sleep(2)


class AddToCartActionsPage1:
    def __init__(self, driver):
        self.driver = driver

    def click_add_cart1(self):
        click_add_cart1 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage1.CLICK_ADD_CART1))
        click_add_cart1.click()
        time.sleep(2)

    # def click_add_cart2(self):
    #     click_add_cart2 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART2))
    #     click_add_cart2.click()
    #     time.sleep(5)
    #
    # def click_add_cart3(self):
    #     click_add_cart3 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART3))
    #     click_add_cart3.click()
    #     time.sleep(5)
    #
    # def click_add_cart4(self):
    #     click_add_cart4 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART4))
    #     click_add_cart4.click()
    #     time.sleep(5)
    #
    # def click_add_cart5(self):
    #     click_add_cart5 = WebDriverWait(self.driver, 20).until(
    #         EC.presence_of_element_located(AddToCartLocatorsPage.CLICK_ADD_CART5))
    #     click_add_cart5.click()
    #     time.sleep(5)


class ViewCartActionsPage1:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        click_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ViewCartLocatorsPage1.CLICK_CART_ICON))
        click_cart_icon.click()
        time.sleep(2)


class CheckOutActionsPage1:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_icon(self):
        click_checkout_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutLocatorsPage1.CLICK_CHECKOUT_ICON))
        click_checkout_icon.click()
        time.sleep(2)


class CheckOutInformationActionsPage1:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_firstname(self, firstname):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage1.FILL_CHECKOUT_FIRSTNAME))
        fill_checkout_firstname.send_keys(firstname)
        time.sleep(2)

    def fill_checkout_lastname(self, lastname):
        fill_checkout_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage1.FILL_CHECKOUT_LASTNAME))
        fill_checkout_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_checkout_zipcode(self, zipcode):
        fill_checkout_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage1.FILL_CHECKOUT_ZIPCODE))
        fill_checkout_zipcode.send_keys(zipcode)
        time.sleep(2)

    def click_checkout_confirmation_icon(self):
        click_checkout_confirmation_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage1.CLICK_CHECKOUT_CONTINUE_ICON))
        click_checkout_confirmation_icon.click()
        time.sleep(2)


class FinishedIconActionsPage1:

    def __init__(self, driver):
        self.driver = driver

    def click_on_finish_icon(self):
        click_on_finish_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FinishedIconLocatorsPage1.CLICK_ON_FINISH_ICON))
        click_on_finish_icon.click()
        time.sleep(2)


class HomeIconActionsPage1:
    def __init__(self, driver):
        self.driver = driver

    def click_on_home_icon(self):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomeIconLocatorsPage1.CLICK_ON_HOME_ICON))
        fill_checkout_firstname.click()
        time.sleep(2)


class AddToCartActionsPage2:
    def __init__(self, driver):
        self.driver = driver

    def click_add_cart2(self):
        click_add_cart2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage2.CLICK_ADD_CART2))
        click_add_cart2.click()
        time.sleep(2)


class ViewCartActionsPage2:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        click_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ViewCartLocatorsPage2.CLICK_CART_ICON))
        click_cart_icon.click()
        time.sleep(2)


class CheckOutActionsPage2:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_icon(self):
        click_checkout_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutLocatorsPage2.CLICK_CHECKOUT_ICON))
        click_checkout_icon.click()
        time.sleep(5)


class CheckOutInformationActionsPage2:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_firstname(self, firstname):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage2.FILL_CHECKOUT_FIRSTNAME))
        fill_checkout_firstname.send_keys(firstname)
        time.sleep(1)

    def fill_checkout_lastname(self, lastname):
        fill_checkout_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage2.FILL_CHECKOUT_LASTNAME))
        fill_checkout_lastname.send_keys(lastname)
        time.sleep(1)

    def fill_checkout_zipcode(self, zipcode):
        fill_checkout_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage2.FILL_CHECKOUT_ZIPCODE))
        fill_checkout_zipcode.send_keys(zipcode)
        time.sleep(1)

    def click_checkout_confirmation_icon(self):
        click_checkout_confirmation_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage2.CLICK_CHECKOUT_CONTINUE_ICON))
        click_checkout_confirmation_icon.click()
        time.sleep(1)


class FinishedIconActionsPage2:

    def __init__(self, driver):
        self.driver = driver

    def click_on_finish_icon(self):
        click_on_finish_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FinishedIconLocatorsPage2.CLICK_ON_FINISH_ICON))
        click_on_finish_icon.click()
        time.sleep(2)


class HomeIconActionsPage2:
    def __init__(self, driver):
        self.driver = driver

    def click_on_home_icon(self):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomeIconLocatorsPage2.CLICK_ON_HOME_ICON))
        fill_checkout_firstname.click()
        time.sleep(2)


class AddToCartActionsPage3:
    def __init__(self, driver):
        self.driver = driver

    def click_add_cart3(self):
        click_add_cart3 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage3.CLICK_ADD_CART3))
        click_add_cart3.click()
        time.sleep(2)


class ViewCartActionsPage3:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        click_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ViewCartLocatorsPage3.CLICK_CART_ICON))
        click_cart_icon.click()
        time.sleep(2)


class CheckOutActionsPage3:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_icon(self):
        click_checkout_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutLocatorsPage3.CLICK_CHECKOUT_ICON))
        click_checkout_icon.click()
        time.sleep(2)


class CheckOutInformationActionsPage3:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_firstname(self, firstname):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage3.FILL_CHECKOUT_FIRSTNAME))
        fill_checkout_firstname.send_keys(firstname)
        time.sleep(2)

    def fill_checkout_lastname(self, lastname):
        fill_checkout_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage3.FILL_CHECKOUT_LASTNAME))
        fill_checkout_lastname.send_keys(lastname)
        time.sleep(2)

    def fill_checkout_zipcode(self, zipcode):
        fill_checkout_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage3.FILL_CHECKOUT_ZIPCODE))
        fill_checkout_zipcode.send_keys(zipcode)
        time.sleep(2)

    def click_checkout_confirmation_icon(self):
        click_checkout_confirmation_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage3.CLICK_CHECKOUT_CONTINUE_ICON))
        click_checkout_confirmation_icon.click()
        time.sleep(2)


class FinishedIconActionsPage3:

    def __init__(self, driver):
        self.driver = driver

    def click_on_finish_icon(self):
        click_on_finish_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FinishedIconLocatorsPage3.CLICK_ON_FINISH_ICON))
        click_on_finish_icon.click()
        time.sleep(2)


class HomeIconActionsPage3:
    def __init__(self, driver):
        self.driver = driver

    def click_on_home_icon(self):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomeIconLocatorsPage3.CLICK_ON_HOME_ICON))
        fill_checkout_firstname.click()
        time.sleep(2)


class AddToCartActionsPage4:
    def __init__(self, driver):
        self.driver = driver

    def click_add_cart4(self):
        click_add_cart4 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage4.CLICK_ADD_CART4))
        click_add_cart4.click()
        time.sleep(2)


class ViewCartActionsPage4:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        click_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ViewCartLocatorsPage4.CLICK_CART_ICON))
        click_cart_icon.click()
        time.sleep(5)


class CheckOutActionsPage4:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_icon(self):
        click_checkout_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutLocatorsPage4.CLICK_CHECKOUT_ICON))
        click_checkout_icon.click()
        time.sleep(5)


class CheckOutInformationActionsPage4:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_firstname(self, firstname):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage4.FILL_CHECKOUT_FIRSTNAME))
        fill_checkout_firstname.send_keys(firstname)
        time.sleep(5)

    def fill_checkout_lastname(self, lastname):
        fill_checkout_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage4.FILL_CHECKOUT_LASTNAME))
        fill_checkout_lastname.send_keys(lastname)
        time.sleep(5)

    def fill_checkout_zipcode(self, zipcode):
        fill_checkout_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage4.FILL_CHECKOUT_ZIPCODE))
        fill_checkout_zipcode.send_keys(zipcode)
        time.sleep(5)

    def click_checkout_confirmation_icon(self):
        click_checkout_confirmation_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage4.CLICK_CHECKOUT_CONTINUE_ICON))
        click_checkout_confirmation_icon.click()
        time.sleep(5)


class FinishedIconActionsPage4:

    def __init__(self, driver):
        self.driver = driver

    def click_on_finish_icon(self):
        click_on_finish_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FinishedIconLocatorsPage4.CLICK_ON_FINISH_ICON))
        click_on_finish_icon.click()
        time.sleep(5)


class HomeIconActionsPage4:
    def __init__(self, driver):
        self.driver = driver

    def click_on_home_icon(self):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomeIconLocatorsPage4.CLICK_ON_HOME_ICON))
        fill_checkout_firstname.click()
        time.sleep(5)


class AddToCartActionsPage5:
    def __init__(self, driver):
        self.driver = driver

    def click_add_cart5(self):
        click_add_cart5 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocatorsPage5.CLICK_ADD_CART5))
        click_add_cart5.click()
        time.sleep(5)


class ViewCartActionsPage5:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        click_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ViewCartLocatorsPage5.CLICK_CART_ICON))
        click_cart_icon.click()
        time.sleep(5)


class CheckOutActionsPage5:

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_icon(self):
        click_checkout_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutLocatorsPage5.CLICK_CHECKOUT_ICON))
        click_checkout_icon.click()
        time.sleep(5)


class CheckOutInformationActionsPage5:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_firstname(self, firstname):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage5.FILL_CHECKOUT_FIRSTNAME))
        fill_checkout_firstname.send_keys(firstname)
        time.sleep(5)

    def fill_checkout_lastname(self, lastname):
        fill_checkout_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage5.FILL_CHECKOUT_LASTNAME))
        fill_checkout_lastname.send_keys(lastname)
        time.sleep(5)

    def fill_checkout_zipcode(self, zipcode):
        fill_checkout_zipcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage5.FILL_CHECKOUT_ZIPCODE))
        fill_checkout_zipcode.send_keys(zipcode)
        time.sleep(5)

    def click_checkout_confirmation_icon(self):
        click_checkout_confirmation_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOutInformationLocatorsPage5.CLICK_CHECKOUT_CONTINUE_ICON))
        click_checkout_confirmation_icon.click()
        time.sleep(5)


class FinishedIconActionsPage5:

    def __init__(self, driver):
        self.driver = driver

    def click_on_finish_icon(self):
        click_on_finish_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(FinishedIconLocatorsPage5.CLICK_ON_FINISH_ICON))
        click_on_finish_icon.click()
        time.sleep(5)


class HomeIconActionsPage5:
    def __init__(self, driver):
        self.driver = driver

    def click_on_home_icon(self):
        fill_checkout_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(HomeIconLocatorsPage5.CLICK_ON_HOME_ICON))
        fill_checkout_firstname.click()
        time.sleep(5)
