Feature: Regression test for eBay.com

  Background:
    Given I navigate to 'ebay'

  @example1
  Scenario Outline: Example using of Scenario Outline
    When I search for 'scott bike'
    And For '<filter>' I set '<value>'
    Then I verify title of product on page result it should contains '<value>'
    Examples:
      | filter    | value        |
      | Bike Type | Gravel Bike  |
      | Color     | Green        |
      | Material  | Carbon Fiber |

  @example2
  Scenario: Example using of text block
    When I click 'Brand Outlet' in top navigation menu
    Then I print text block
    """
    Find it all at
    the Brand Outlet
    Your one-stop shop for home,
    fashion, tech, and more.
    """
    When I click 'Help & Contact' in top navigation menu
    Then I print text block
    """
    To keep eBay a safe place to buy and sell,
    we will occasionally ask you to verify yourself.
    This helps us to block unauthorized users
    from entering our site.
    """

