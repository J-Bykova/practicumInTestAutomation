@example
Feature: Regression test for eBay.com

  Background:
    Given I navigate to 'ebay'


  @example5
  Scenario: Verify information about Captcha
    When I click 'Sign in' in top navigation menu
    And I click on 'I am human' checkbox
    And I open menu of captcha and click on 'information' button
    Then I validate the 'information' popup
    """
    hCaptcha is a service that reduces bots and spam by asking simple questions.
    Please follow the instructions at the top of the screen for each challenge.
    For more information visit
    """

  @example4
  Scenario: Verify the product’s multiple filters on the result page
    When I search for 'scott bike'
    And I set a few filters
      | filter    | value       |
      | Bike Type | Gravel Bike |
      | Condition | Used        |
    Then I validate that all results are related to 'Gravel Bike' and 'Pre-Owned'


  @example3
  Scenario Outline:  Verify the product’s one filter on the result page
    When I search for 'scott bike'
    And For '<filter>' I set '<value>'
    Then I verify title of product on page result it should contains '<value>'
    Examples:
      | filter    | value        |
      | Bike Type | Gravel Bike  |
      | Color     | Green        |
      | Material  | Carbon Fiber |


  @example2
  Scenario Outline: Verify sub-category navigation leads to right pages
    When I click 'Shop by category' and pick '<category>'
    Then  I expected to see '<title>' of page
    Examples:
      | category           | title                                        |
      | Collectibles & Art | Collectibles & Art products for sale \| eBay |
      | Home & garden      | Home & Garden products for sale \| eBay      |

  @example1
  Scenario Outline: Verify top navigation menu items leads to right pages
    When I click '<link>' in top navigation menu
    Then  I expected to see '<title>' of page
    Examples:
      | link         | title                                               |
      | Daily Deals  | Daily Deals on eBay \| Best deals and Free Shipping |
      | Brand Outlet | Brand Outlet products for sale \| eBay              |
