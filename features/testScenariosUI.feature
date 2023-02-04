Feature: Test Cases for GIG Test - UI

  Scenario: Test 4 - Login, Buy item and checkout of Saucedemo page
    Given Launch browser
    When Open home page of Saucedemo
    And Assert that im in "Login page"
    Then Enter credentials "standard_user" and "secret_sauce"
    When Click login button
    And Assert that im in "Product page"
    And Add product to the cart
    When Go to cart
    And Assert that im in "Cart page"
    When Click in Checkout
    And Assert that im in "Checkout page"
    Then Close the browser