import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjectModel.all_pages import allPages


@given('Launch browser')
def launch_browser(context):
    """
        This function retrieved data from the specific API Request
    """
    context.driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")


@Step('Open home page of Saucedemo')
def open_home_page(context):
    """
        This function assert that the code response is 200
    """
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(2)


@Step('Enter credentials "{user}" and "{pwd}"')
def login_with_the_test_user(context, user, pwd):
    """
        This function assert that the code response is 200
    """
    context.driver.find_element(By.ID, allPages.user_name).click()
    time.sleep(0.3)
    context.driver.find_element(By.ID, allPages.user_name).send_keys(user)
    time.sleep(0.3)
    context.driver.find_element(By.ID, allPages.password).send_keys(pwd)
    time.sleep(0.5)


@Step('Click login button')
def login_with_the_test_user(context):
    """
        This function assert that the code response is 200
    """
    context.driver.find_element(By.ID, allPages.login_button).click()
    time.sleep(1)


@Step('Add product to the cart')
def add_product_to_cart(context):
    """
        This function assert that the code response is 200
    """
    context.driver.find_element(By.ID, allPages.add_to_cart_first_product_of_the_list).click()
    time.sleep(1)


@Step('Go to cart')
def go_to_cart(context):
    """
        This function assert that the code response is 200
    """
    context.driver.find_element(By.ID, allPages.button_cart).click()
    time.sleep(1)


@Step('Click in Checkout')
def click_checkout(context):
    """
        This function assert that the code response is 200
    """
    context.driver.find_element(By.ID, allPages.button_checkout).click()
    time.sleep(1)


@Step('Assert that im in "{page}"')
def close_browser(context, page):
    """
        This function assert that exist at least one user
    """

    if page == "Login page":
        context.driver.find_element(By.XPATH, allPages.icon_swag_labs_center_screen).is_displayed()
    if page == "Product page":
        context.driver.find_element(By.ID, allPages.burger_menu_button).is_displayed()
    if page == "Cart page":
        context.driver.find_element(By.ID, allPages.button_continue_shopping).is_displayed()
    if page == "Checkout page":
        context.driver.find_element(By.ID, allPages.button_cancel).is_displayed()


@Step('Close the browser')
def close_browser(context):
    """
        This function assert that exist at least one user
    """
    context.driver.close()
