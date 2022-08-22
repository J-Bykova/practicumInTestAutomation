from behave import step
from selenium.webdriver.common.by import By


@step("I search for '{product}'")
def step_impl(context, product):
    search_field = context.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search for anything']")
    search_button = context.driver.find_element(by=By.XPATH, value="//input[@type='submit' and @value='Search']")

    search_field.send_keys(product)
    search_button.click()


@step("For '{filter_type}' I set '{filter_value}'")
def step_impl(context, filter_type, filter_value):
    context.driver.find_element(
        by=By.XPATH,
        value=f"//li[.//h3[text()='{filter_type}']]//span[text()='{filter_value}']").click()


@step("I verify title of product on page result it should contains '{expected}'")
def step_impl(context, expected):
    actual_title = context.driver.find_element(
        by=By.XPATH,
        value="(//*[contains(@class,'srp-results')]//h3[@class='s-item__title'])[1]"
    )
    assert expected in actual_title.text, f"There is a bug: Title does not contains {expected}"


@step("I print text block")
def step_impl(context):
    print(f"I print text block: \n{context.text}\n")
