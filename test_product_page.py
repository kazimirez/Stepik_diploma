import time
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    this_page = ProductPage(browser, link)
    this_page.open()
    this_page.should_disappear()
    this_page.should_not_be_success_message()
    this_page.press_add_to_cart()
    this_page.solve_quiz_and_get_code()
    this_page.should_be_the_right_book()
    this_page.should_be_the_right_sum()
    time.sleep(5)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    this_page = ProductPage(browser, link)
    this_page.open()
    this_page.press_add_to_cart()
    this_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    this_page = ProductPage(browser, link)
    this_page.open()
    this_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    this_page = ProductPage(browser, link)
    this_page.open()
    this_page.press_add_to_cart()
    this_page.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_message_about_empty_basket()


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@mail.com"
        password = "testpassword"
        page = LoginPage(self.browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        this_page = ProductPage(browser, link)
        this_page.open()
        this_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):  # , link
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
        this_page = ProductPage(browser, link)
        this_page.open()
        this_page.should_disappear()
        this_page.should_not_be_success_message()
        this_page.press_add_to_cart()
        this_page.solve_quiz_and_get_code()
        this_page.should_be_the_right_book()
        this_page.should_be_the_right_sum()
        time.sleep(6)
