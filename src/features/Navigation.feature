Feature: Header navigation

  Scenario Outline: Top navigation menu
    Given I navigate to 'ebay'
    When I click '<link>' in top navigation menu
    Then  I expected to see '<title>' of page
    Examples:
      | link         | title                                               |
      | Daily Deals  | Daily Deals on eBay \| Best deals and Free Shipping |
      | Brand Outlet | Brand Outlet products for sale \| eBay              |


  Scenario Outline: Sub-category navigation
    Given I navigate to 'ebay'
    When I click 'Shop by category' and pick '<category>'
    Then  I expected to see '<title>' of page
    Examples:
      | category           | title                                        |
      | Collectibles & Art | Collectibles & Art products for sale \| eBay |
      | Home & garden      | Home & Garden products for sale \| eBay      |