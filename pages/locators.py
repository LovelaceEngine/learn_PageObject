from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators:
    PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_ADDED = (By.CSS_SELECTOR, ".alert-safe:nth-child(3) .alertinner strong")

class BasketPageLocators:
    BASKET_BUTTON_HEADER = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn.btn-default:nth-child(1)")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")