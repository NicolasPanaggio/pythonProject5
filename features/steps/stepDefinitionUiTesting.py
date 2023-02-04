import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjectModel.all_pages import allPages


@given('Launch browser')
def launch_browser(context):
    """
        This function launch browser
    """
    context.driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")


@Step('Open home page of Saucedemo')
def open_home_page(context):
    """
        This function go to Saucedemo login page
    """
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(2)


@Step('Enter credentials "{user}" and "{pwd}"')
def login_with_the_test_user(context, user, pwd):
    """
        This function insert credentials
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
        This function click in login button
    """
    context.driver.find_element(By.ID, allPages.login_button).click()
    time.sleep(1)


@Step('Add product to the cart')
def add_product_to_cart(context):
    """
        This function add product to the cart
    """
    context.driver.find_element(By.ID, allPages.add_to_cart_first_product_of_the_list).click()
    time.sleep(2)


@Step('Go to cart')
def go_to_cart(context):
    """
        This function click and go to cart
    """
    context.driver.find_element(By.ID, allPages.button_cart).click()
    time.sleep(1)


@Step('Click in Checkout')
def click_checkout(context):
    """
        This function click and go tu checkout
    """
    context.driver.find_element(By.ID, allPages.button_checkout).click()
    time.sleep(1)


@Step('Assert that im in "{page}"')
def close_browser(context, page):
    """
        This function assert diferentes pages are displayed
    """

    if page == "Login page":
        context.driver.find_element(By.XPATH, allPages.icon_swag_labs_center_screen).is_displayed()
    if page == "Product page":
        context.driver.find_element(By.ID, allPages.burger_menu_button).is_displayed()
    if page == "Cart page":
        context.driver.find_element(By.ID, allPages.button_continue_shopping).is_displayed()
    if page == "Checkout page":
        context.driver.find_element(By.ID, allPages.button_cancel).is_displayed()
    if page == "Checkout overview page":
        context.driver.find_element(By.ID, allPages.button_finish).is_displayed()
    if page == "Final page":
        context.driver.find_element(By.CLASS_NAME, allPages.pony_express_final_page).is_displayed()


@Step('Assert that the product was added and the icon with the number of products added in cart')
def assert_product_added(context):
    """
        This function assert that the product was added to the cart and the change of the icon of the cart
    """
    context.driver.find_element(By.ID, allPages.button_remove_product).is_displayed()
    time.sleep(0.3)
    context.driver.find_element(By.CLASS_NAME, allPages.shopping_cart_num_of_products_added).is_displayed()


@Step('Enter first name "{name}" and last name "{lastname}" and zip code "{zipcode}"')
def insert_data_in_checkout_form(context, name, lastname, zipcode):
    """
        This function insert data in checkout form
    """
    context.driver.find_element(By.ID, allPages.tbx_name).send_keys(name)
    time.sleep(0.3)
    context.driver.find_element(By.ID, allPages.tbx_lastname).send_keys(lastname)
    time.sleep(0.3)
    context.driver.find_element(By.ID, allPages.tbx_zip_code).send_keys(zipcode)
    time.sleep(0.3)


@Step('Click in button continue in checkout page')
def click_button_continue_checkout_page(context):
    """
        This function click in continue button in checkout page
    """
    context.driver.find_element(By.ID, allPages.button_continue_checkout_page).click()
    time.sleep(1)


@Step('Assert the details of the product in checkout overview label')
def assert_checkout_overivew_details(context):
    """
        This function assert the information of the product in checkout overview
    """
    price_of_product_variable = context.driver.find_element(By.CLASS_NAME, allPages.price_of_product).text
    price_total_of_product_in_product_page_variable = context.driver.find_element(By.CLASS_NAME, allPages.price_total_of_product_in_product_page).text
    assertion_variable_price = "Item total: " + price_of_product_variable
    assert price_total_of_product_in_product_page_variable == assertion_variable_price, "Product is not valid, the price is different"


@Step('Click in finish button checkout page')
def click_in_finish_button_checkout_page(context):
    """
        This function assert the information of the product in checkout overview
    """
    context.driver.find_element(By.ID, allPages.button_finish).click()
    time.sleep(1)

@Step('Close the browser')
def close_browser(context):
    """
        This function close the browser
    """
    context.driver.close()
