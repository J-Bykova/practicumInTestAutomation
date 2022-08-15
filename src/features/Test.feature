#Feature: Hello world
#
#  Scenario: Test
#    Given Navigate to Google

Feature:   Regression test for eBay.com

  Scenario: User could add item to the cart
    Given Navigate to 'ebay'
    When search for the item -> scott bike
    And click the search button
    Then click first available item from result list
    And click "Add to the cart"
    And In pop-up window click "go to the cart"
    Then verify test




