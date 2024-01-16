Feature: Logout from app

  Scenario: Logout from app
    Given I am on the main page
    When I click on account button
    And I click on logout button
    And I confirm logout
    Then I am on the login page