import time
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    #link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    this_page = ProductPage(browser, link)
    this_page.open()
    this_page.press_add_to_cart()
    this_page.solve_quiz_and_get_code()
    this_page.should_be_the_right_book()
    this_page.should_be_the_right_sum()
    time.sleep(5)

