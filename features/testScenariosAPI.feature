Feature: Test Cases for GIG Test - API

  Scenario: TEST 1 - Verify at least one user return and fail when a response is not returned
    Given Get API
    When Assert code response is 200
    Then Assert that exist an user

  Scenario: TEST 2 - Verify one user name have letter C and fail when response is not returned
    Given Get API
    When Assert code response is 200
    Then Assert one user name have letter C

  Scenario: TEST 3 - Show user list in console and fail when response is not returned or the list contain zero users
    Given Get API
    When Assert code response is 200
    Then Retrieve list of users and show in console and assert user count