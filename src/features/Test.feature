@example
Feature: Regression test for eBay.com

  Background:
    Given I navigate to 'ebay'

  @example4
  Scenario: Verify the product’s multiple filters on the result page
    When I search for 'scott bike'
    And I set a few filters
      | filter    | value       |
      | Bike Type | Gravel Bike |
      | Condition | Used        |
    And I click on first item
    Then I verify product description
      """
      Gravel Bike Used
      """

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
