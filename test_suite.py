import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPage.Actionspage import LoginActionsPage, ViewCartActionsPage, CheckOutActionsPage, \
    CheckOutInformationActionsPage, FinishedIconActionsPage, HomeIconActionsPage, AddToCartActionsPage, \
    FinishedIconActionsPage1, HomeIconActionsPage1, CheckOutInformationActionsPage1, ViewCartActionsPage1, \
    CheckOutActionsPage1, AddToCartActionsPage1, HomeIconActionsPage2, FinishedIconActionsPage2, \
    CheckOutInformationActionsPage2, CheckOutActionsPage2, ViewCartActionsPage2, AddToCartActionsPage2, \
    HomeIconActionsPage3, FinishedIconActionsPage3, CheckOutInformationActionsPage3, CheckOutActionsPage3, \
    ViewCartActionsPage3, AddToCartActionsPage3, FinishedIconActionsPage5, HomeIconActionsPage5, \
    CheckOutInformationActionsPage5, CheckOutActionsPage5, ViewCartActionsPage5, HomeIconActionsPage4, \
    FinishedIconActionsPage4, CheckOutInformationActionsPage4, CheckOutActionsPage4, ViewCartActionsPage4, \
    AddToCartActionsPage4, AddToCartActionsPage5
from Config.config import Config

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # Uncomment the line below to run in headless mode
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginActionsPage(driver)  # call the login class
    login_page.open_url(Config.BASE_URL)  # call the url
    return login_page


def test_login_page_on_sauce_demo_website(login):
    login.enter_username(Config.USERNAME)
    login.enter_password(Config.PASSWORD)
    login.click_login_button()


def test_add_to_cart(login):
    add_cart = AddToCartActionsPage(login.driver)
    add_cart.click_add_cartBack()
    # add_cart.click_add_cart1()
    # add_cart.click_add_cart2()
    # add_cart.click_add_cart3()
    # add_cart.click_add_cart4()
    # add_cart.click_add_cart5()


def test_view_cart_icon(login):
    add_cart = ViewCartActionsPage(login.driver)
    add_cart.click_cart_icon()


def test_checkout_icon(login):
    add_cart = CheckOutActionsPage(login.driver)
    add_cart.click_checkout_icon()


def test_checkout_information_icon(login):
    add_cart = CheckOutInformationActionsPage(login.driver)
    add_cart.fill_checkout_firstname(Config.FILL_CHECKOUT_FIRSTNAME)
    add_cart.fill_checkout_lastname(Config.FILL_CHECKOUT_LASTNAME)
    add_cart.fill_checkout_zipcode(Config.POSTAL_CODE)
    add_cart.click_checkout_confirmation_icon()


def test_finished_icon(login):
    click_on_finish_icon = FinishedIconActionsPage(login.driver)
    click_on_finish_icon.click_on_finish_icon()


def test_home_icon(login):
    add_cart = HomeIconActionsPage(login.driver)
    add_cart.click_on_home_icon()


def test_add_to_cart1(login):
    add_cart = AddToCartActionsPage1(login.driver)
    # add_cart.click_add_cartBack()
    add_cart.click_add_cart1()


def test_view_cart_icon1(login):
    add_cart = ViewCartActionsPage1(login.driver)
    add_cart.click_cart_icon()


def test_checkout_icon1(login):
    add_cart = CheckOutActionsPage1(login.driver)
    add_cart.click_checkout_icon()


def test_checkout_information_icon1(login):
    add_cart = CheckOutInformationActionsPage1(login.driver)
    add_cart.fill_checkout_firstname(Config.FILL_CHECKOUT_FIRSTNAME)
    add_cart.fill_checkout_lastname(Config.FILL_CHECKOUT_LASTNAME)
    add_cart.fill_checkout_zipcode(Config.POSTAL_CODE)
    add_cart.click_checkout_confirmation_icon()


def test_finished_icon1(login):
    click_on_finish_icon = FinishedIconActionsPage1(login.driver)
    click_on_finish_icon.click_on_finish_icon()


def test_home_icon1(login):
    add_cart = HomeIconActionsPage1(login.driver)
    add_cart.click_on_home_icon()


def test_add_to_cart2(login):
    add_cart = AddToCartActionsPage2(login.driver)
    # add_cart.click_add_cartBack()
    add_cart.click_add_cart2()


def test_view_cart_icon2(login):
    add_cart = ViewCartActionsPage2(login.driver)
    add_cart.click_cart_icon()


def test_checkout_icon2(login):
    add_cart = CheckOutActionsPage2(login.driver)
    add_cart.click_checkout_icon()


def test_checkout_information_icon2(login):
    add_cart = CheckOutInformationActionsPage2(login.driver)
    add_cart.fill_checkout_firstname(Config.FILL_CHECKOUT_FIRSTNAME)
    add_cart.fill_checkout_lastname(Config.FILL_CHECKOUT_LASTNAME)
    add_cart.fill_checkout_zipcode(Config.POSTAL_CODE)
    add_cart.click_checkout_confirmation_icon()


def test_finished_icon2(login):
    click_on_finish_icon = FinishedIconActionsPage2(login.driver)
    click_on_finish_icon.click_on_finish_icon()


def test_home_icon2(login):
    add_cart = HomeIconActionsPage2(login.driver)
    add_cart.click_on_home_icon()


def test_add_to_cart3(login):
    add_cart = AddToCartActionsPage3(login.driver)
    # add_cart.click_add_cartBack()
    add_cart.click_add_cart3()


def test_view_cart_icon3(login):
    add_cart = ViewCartActionsPage3(login.driver)
    add_cart.click_cart_icon()


def test_checkout_icon3(login):
    add_cart = CheckOutActionsPage3(login.driver)
    add_cart.click_checkout_icon()


def test_checkout_information_icon3(login):
    add_cart = CheckOutInformationActionsPage3(login.driver)
    add_cart.fill_checkout_firstname(Config.FILL_CHECKOUT_FIRSTNAME)
    add_cart.fill_checkout_lastname(Config.FILL_CHECKOUT_LASTNAME)
    add_cart.fill_checkout_zipcode(Config.POSTAL_CODE)
    add_cart.click_checkout_confirmation_icon()


def test_finished_icon3(login):
    click_on_finish_icon = FinishedIconActionsPage3(login.driver)
    click_on_finish_icon.click_on_finish_icon()


def test_home_icon3(login):
    add_cart = HomeIconActionsPage3(login.driver)
    add_cart.click_on_home_icon()


def test_add_to_cart4(login):
    add_cart = AddToCartActionsPage4(login.driver)
    # add_cart.click_add_cartBack()
    add_cart.click_add_cart4()


def test_view_cart_icon4(login):
    add_cart = ViewCartActionsPage4(login.driver)
    add_cart.click_cart_icon()


def test_checkout_icon4(login):
    add_cart = CheckOutActionsPage4(login.driver)
    add_cart.click_checkout_icon()


def test_checkout_information_icon4(login):
    add_cart = CheckOutInformationActionsPage4(login.driver)
    add_cart.fill_checkout_firstname(Config.FILL_CHECKOUT_FIRSTNAME)
    add_cart.fill_checkout_lastname(Config.FILL_CHECKOUT_LASTNAME)
    add_cart.fill_checkout_zipcode(Config.POSTAL_CODE)
    add_cart.click_checkout_confirmation_icon()


def test_finished_icon4(login):
    click_on_finish_icon = FinishedIconActionsPage4(login.driver)
    click_on_finish_icon.click_on_finish_icon()


def test_home_icon4(login):
    add_cart = HomeIconActionsPage4(login.driver)
    add_cart.click_on_home_icon()


def test_add_to_cart5(login):
    add_cart = AddToCartActionsPage5(login.driver)
    # add_cart.click_add_cartBack()
    add_cart.click_add_cart5()


def test_view_cart_icon5(login):
    add_cart = ViewCartActionsPage5(login.driver)
    add_cart.click_cart_icon()


def test_checkout_icon5(login):
    add_cart = CheckOutActionsPage5(login.driver)
    add_cart.click_checkout_icon()


def test_checkout_information_icon5(login):
    add_cart = CheckOutInformationActionsPage5(login.driver)
    add_cart.fill_checkout_firstname(Config.FILL_CHECKOUT_FIRSTNAME)
    add_cart.fill_checkout_lastname(Config.FILL_CHECKOUT_LASTNAME)
    add_cart.fill_checkout_zipcode(Config.POSTAL_CODE)
    add_cart.click_checkout_confirmation_icon()


def test_finished_icon5(login):
    click_on_finish_icon = FinishedIconActionsPage5(login.driver)
    click_on_finish_icon.click_on_finish_icon()


def test_home_icon5(login):
    add_cart = HomeIconActionsPage5(login.driver)
    add_cart.click_on_home_icon()
