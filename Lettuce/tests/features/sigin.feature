Feature: Sign In
    As visitor of solidopinion.com
    I should have possibility
    For sign in on site

    Scenario: Sign In with empty data
        Given I go to "sign up" page
        When I click on "button signup" in "sign up"
        And I see "alert all empty" in "sign up"
        Then I click on "button close alert" in "sign up"

    Scenario: Sign In just with name
        Given I go to "sign up" page
        When I fill "input name" by "name" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert all empty" in "sign up"

    Scenario: Sign In with empty name
        Given I go to "sign up" page
        When I fill "input email" by "email" in "sign up"
        And I fill "input password" by "password" in "sign up"
        And I fill "input re-password" by "password" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert empty name" in "sign up"

    Scenario: Sign In with invalid email
        Given I go to "sign up" page
        When I fill "input name" by "name" in "sign up"
        And I fill "input email" by "bad email" in "sign up"
        And I fill "input password" by "password" in "sign up"
        And I fill "input re-password" by "password" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert invalid email" in "sign up"

    Scenario: Sign In with empty email
        Given I go to "sign up" page
        When I fill "input name" by "name" in "sign up"
        And I fill "input password" by "password" in "sign up"
        And I fill "input re-password" by "password" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert invalid email" in "sign up"

    Scenario: Sign In just with email
        Given I go to "sign up" page
        When I fill "input email" by "email" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert empty name" in "sign up"

    Scenario: Sign In with invalid short password
        Given I go to "sign up" page
        When I fill "input name" by "name" in "sign up"
        And I fill "input email" by "email" in "sign up"
        And I fill "input password" by "short password" in "sign up"
        And I fill "input re-password" by "short password" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert short password" in "sign up"

    Scenario: Sign In with empty password
        Given I go to "sign up" page
        When I fill "input name" by "name" in "sign up"
        And I fill "input email" by "email" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert empty password" in "sign up"

    Scenario: Sign In with different passwords
        Given I go to "sign up" page
        When I fill "input name" by "name" in "sign up"
        And I fill "input email" by "email" in "sign up"
        And I fill "input password" by "short password" in "sign up"
        And I fill "input re-password" by "password" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "alert don't match passwords" in "sign up"

    Scenario: Sign In with good data
        Given I go to "sign up" page
        When I fill "input name" by "true name" in "sign up"
        And I fill "input email" by "email" in "sign up"
        And I fill "input password" by "password" in "sign up"
        And I fill "input re-password" by "password" in "sign up"
        And I click on "button signup" in "sign up"
        Then I see "welcome title" in "welcome"
        And I see "user name" in "header"