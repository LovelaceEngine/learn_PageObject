from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def product_button_should_be_click(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON)
        button.click()

    def check_product_parameter(self, what, where, what_added, where_added):
        find = self.browser.find_element(what, where)
        find_added = self.browser.find_element(what_added, where_added)

        print (f"Полученное значение - '{find_added.text}', должно быть - '{find.text}'")
        assert find_added.text in find.text, "Значение после добавления в корзину не соответствует требуемому"
