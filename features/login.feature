Feature: Login on app

  Scenario: Login with wrong password
    Given I am on the login page
    When I input a valid username
    And I input an invalid password
    And I click on login button
    Then I am still on the login page


  Scenario: Login with wrong username
    Given I am on the login page
    When I input a invalid username
    And I input a valid password
    And I click on login button
    Then I am still on the login page


  Scenario: Login success
    Given I am on the login page
    When I input a valid username
    And I input a valid password
    And I click on login button
    Then I am on the main page

