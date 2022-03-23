from selenium.webdriver.common.by import By


class MainPageLocators:
    pass



class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_IN_ADDED = (By.CSS_SELECTOR, '.in:nth-child(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_CART = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")


