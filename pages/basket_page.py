from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_button_click(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON_HEADER)
        button.click()

    def is_basket_empty(self):
        inner = self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY)
        inner_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        print(f"Текст корзины: '{inner_text.text}'")
        assert not inner, "В корзине что-то есть"


