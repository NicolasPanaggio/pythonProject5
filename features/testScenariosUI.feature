Feature: Test Cases for GIG Test - UI

  Scenario: Test 4 - Login, Buy item and checkout of Saucedemo page
    Given Launch browser
    When Open home page of Saucedemo
    And Assert that im in "Login page"
    Then Enter credentials "standard_user" and "secret_sauce"
    When Click login button
    And Assert that im in "Product page"
    And Add product to the cart
    Then Assert that the product was added and the icon with the number of products added in cart
    When Go to cart
    And Assert that im in "Cart page"
    When Click in Checkout
    And Assert that im in "Checkout page"
    And Enter first name "Nicolas" and last name "Panaggio" and zip code "9999"
    When Click in button continue in checkout page
    And Assert that im in "Checkout overview page"
    And Assert the details of the product in checkout overview label
    And Click in finish button checkout page
    And Assert that im in "Final page"
    Then Close the browser