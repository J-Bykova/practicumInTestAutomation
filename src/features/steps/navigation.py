from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains, title_is
from selenium.webdriver.support.wait import WebDriverWait


@step("I navigate to '{page}'")
def test(context, page):
    context.driver = webdriver.Chrome(executable_path="/Users/jenny/bin/webdriver/chromedriver")
    if page == "google":
        return context.driver.get("https://www.google.com/")
    elif page == "ebay":
        return context.driver.get("https://www.ebay.com/")
    else:
        print(f"'{page}' is unexpected page")


@step("I click '{link}' in top navigation menu")
def click_header_navigation_menu_item(context, link):
    item = context.driver.find_element(
        by=By.XPATH,
        value=f"//header//a[contains(text(), '{link}')]"
    )
    item.click()


@step("I click '{shop_by}' and pick '{category}'")
def click_header_navigation_menu_item(context, shop_by, category):
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


@step("I expected to see '{expected}' of page")
def step_impl(context, expected):
    WebDriverWait(context.driver, timeout=3).until(title_is(expected))
