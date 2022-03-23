from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def should_be_the_right_book(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_added = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADDED).text
        assert name == name_in_added, 'books are not the same'

    def should_be_the_right_sum(self):
        got_sum = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        actual_sum = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert got_sum == actual_sum, "price of book does not match price added to the cart"


    def press_add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    #def should_be_message_book_added(self):


