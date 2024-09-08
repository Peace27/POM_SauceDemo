import pytest
from selenium import webdriver

from ActionPage.Actionspage import LoginActionsPage, ViewCartActionsPage, CheckOutActionsPage, \
    CheckOutInformationActionsPage, FinishedIconActionsPage, HomeIconActionsPage, AddToCartActionsPage


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginActionsPage(driver)  # call the login class
    login_page.open_url("https://www.saucedemo.com/")  # call the url
    return login_page


def test_login_page_on_sauce_demo_website(login):
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()


def test_add_to_cart(login):
    add_cart = AddToCartActionsPage(login.driver)
    add_cart.click_add_cartBack()
    add_cart.click_add_cart1()
    add_cart.click_add_cart2()
    add_cart.click_add_cart3()
    add_cart.click_add_cart4()
    add_cart.click_add_cart5()


def test_view_cart_icon(login):
    add_cart = ViewCartActionsPage(login.driver)
    add_cart.click_cart_icon()


def test_checkout_icon(login):
    add_cart = CheckOutActionsPage(login.driver)
    add_cart.click_checkout_icon()


def test_checkout_information_icon(login):
    add_cart = CheckOutInformationActionsPage(login.driver)
    add_cart.fill_checkout_firstname("jake")
    add_cart.fill_checkout_lastname("Othniel")
    add_cart.fill_checkout_zipcode("+234")
    add_cart.click_checkout_confirmation_icon()


def test_finished_icon(login):
    click_on_finish_icon = FinishedIconActionsPage(login.driver)
    click_on_finish_icon.click_on_finish_icon()


def test_home_icon(login):
    add_cart = HomeIconActionsPage(login.driver)
    add_cart.click_on_home_icon()



