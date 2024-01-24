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


  Scenario: Close the popup from the main page
    Given I am on the start page
    When I click the cancel button
    Then The popup is not visible


  Scenario: Add person with first name
    Given I am on the home page
    When I click on add button from menu
    And I click on person button
    And I input first name
    And I click on save button
    Then I click on finish button


  Scenario: Add person with last name
    Given I am on the home page
    When I click on add button from menu
    And I click on person button
    And I input last name
    And I click on save button
    Then I click on finish button


  Scenario: Add person with complete name
    Given I am on the home page
    When I click on add button from menu
    And I click on person button
    And I input again first name
    And I input again last name
    And I click on save button
    Then I click on finish button


  Scenario: See the list of added people
    Given I am on the initial page
    When I click the people button
    Then I see the list of people


  Scenario: Delete the first person added from the people list
    Given I am on the people page
    When I click the people button
    Then The I select the person to delete
    And I click on delete button
    And I confirm delete person





