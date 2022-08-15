import time

from behave import step
from selenium.webdriver.common.by import By


@step("search for the item -> scott bike")
def search_for_item(context):
    search_field = context.driver.find_element(by=By.XPATH, value="//input[@id='gh-ac']")
    search_field.send_keys("scott bike")
    time.sleep(2)


@step("click the search button")
def click_search_button(context):
    search_button = context.driver.find_element(by=By.XPATH, value="//input[@id='gh-btn']")
    search_button.click()
    time.sleep(2)


@step("click first available item from result list")
def click_first_available_item(context):
    first_item = context.driver.find_element(by=By.XPATH,
                                             value="//li[@class='s-item s-item__pl-on-bottom s-item--watch-at-corner']")
    first_item.click()
    time.sleep(2)


# @step('click "Add to the cart"')
# def click_add_to_cart(context):
#     # context.driver.window_handles ????
#     add_to_cart_button = context.driver.find_element(by=By.XPATH, value="//a[@id='atcRedesignId_btn']")
#     add_to_cart_button.click()
#     time.sleep(2)
