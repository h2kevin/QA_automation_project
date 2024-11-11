Feature: User can test out the market page
  Scenario: user can be able to see three options: market, agencies, and developers
    Given Open reelly page
    When Enter email and password
    And Click on Continue button
    And Click on market
    Then verify user be able to see three options that available
