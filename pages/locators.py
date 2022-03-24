from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_INPUT_PASSWORD_CONFIRM = (
    By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON_REGISTER = (
    By.CSS_SELECTOR, "button[name=registration_submit]")


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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items h3")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
