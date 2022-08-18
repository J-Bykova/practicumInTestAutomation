from behave import step
from selenium.webdriver.common.by import By


@step("I search for '{product}'")
def search_for_item(context, product):
    search_field = context.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search for anything']")
    search_button = context.driver.find_element(by=By.XPATH, value="//input[@type='submit' and @value='Search']")

    search_field.send_keys(product)
    search_button.click()


@step("For '{filter_type}' I set '{filter_value}'")
def set_filter(context, filter_type, filter_value):
    context.driver.find_element(
        by=By.XPATH,
        value=f"//li[.//h3[text()='{filter_type}']]//span[text()='{filter_value}']").click()


@step("I verify page result should contains '{expected}'")
def verify_result(context, expected):
    actual_title = context.driver.find_element(
        by=By.XPATH,
        value="(//*[contains(@class,'srp-results')]//h3[@class='s-item__title'])[1]"
    )
    assert expected in actual_title.text, "There is a bug"
