Feature: Regression test for eBay.com

  Scenario: User could filter results
    Given I navigate to 'ebay'
    When I search for 'scott bike'
    And For 'Bike Type' I set 'Gravel Bike'
    And For 'Material' I set 'Carbon Fiber'
    And For 'Color' I set 'Green'
    Then I verify page result should contains 'scott bike'




