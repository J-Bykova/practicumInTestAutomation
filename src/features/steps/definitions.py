import warnings

from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait


@step("I verify product description")
def step_impl(context):
    # TODO
    warnings.warn(f"I print text block: \n{context.text}\n")


@step("I click on first item")
def step_impl(context):
    if len(context.driver.window_handles) != 1:
        raise Exception("There is more then one windows open")

    original_window = context.driver.current_window_handle
    product_title = context.driver.find_element(
        by=By.XPATH,
        value="(//*[contains(@class,'srp-results')]//h3[@class='s-item__title'])[1]"
    )

    product_title.click()
    WebDriverWait(context.driver, timeout=10).until(expected_conditions.number_of_windows_to_be(2))

    for window_handle in context.driver.window_handles:
        if window_handle != original_window:
            context.driver.switch_to.window(window_handle)
            break


@step("I verify title of product on page result it should contains '{expected}'")
def step_impl(context, expected):
    actual_title = context.driver.find_element(
        by=By.XPATH,
        value="(//*[contains(@class,'srp-results')]//h3[@class='s-item__title'])[1]"
    )
    assert expected in actual_title.text, f"There is a bug: Title does not contains {expected}"


@step("For '{filter_type}' I set '{filter_value}'")
def step_impl(context, filter_type, filter_value):
    context.driver.find_element(
        by=By.XPATH,
        value=f"//li[.//h3[text()='{filter_type}']]//span[text()='{filter_value}']").click()


@step("I search for '{product}'")
def step_impl(context, product):
    search_field = context.driver.find_element(by=By.XPATH, value="//input[@placeholder='Search for anything']")
    search_button = context.driver.find_element(by=By.XPATH, value="//input[@type='submit' and @value='Search']")

    search_field.send_keys(product)
    search_button.click()


@step("I set a few filters")
def step_impl(context):
    table_filters = context.table

    for row in table_filters:
        filter_type = row['filter']
        filter_value = row['value']

        filter_option = context.driver.find_element(
            by=By.XPATH,
            value=f"//li[.//h3[text()='{filter_type}']]//span[text()='{filter_value}']")
        filter_option.click()


@step("I print text block")
def step_impl(context):
    print(f"I print text block: \n{context.text}\n")


@step("I expected to see '{expected}' of page")
def step_impl(context, expected):
    WebDriverWait(context.driver, timeout=3).until(title_is(expected))


@step("I click '{shop_by}' and pick '{category}'")
def step_impl(context, shop_by, category):
    menu_button = context.driver.find_element(
        by=By.XPATH,
        value=f"//button[contains(text(), '{shop_by}')]"
    )
    menu_button.click()

    category_item = context.driver.find_element(
        by=By.XPATH,
        value=f"//div[./h2[text()='{shop_by}']]//a[text()='{category}']"
    )
    category_item.click()


@step("I click '{link}' in top navigation menu")
def step_impl(context, link):
    item = context.driver.find_element(
        by=By.XPATH,
        value=f"//header//a[contains(text(), '{link}')]"
    )
    item.click()
    WebDriverWait(context.driver, timeout=3).until(title_is("Security Measure"))


@step("I navigate to '{page}'")
def step_impl(context, page):
    context.driver = webdriver.Chrome(executable_path="/Users/jenny/bin/webdriver/chromedriver")
    if page == "google":
        return context.driver.get("https://www.google.com/")
    elif page == "ebay":
        return context.driver.get("https://www.ebay.com/")
    else:
        print(f"'{page}' is unexpected page")
