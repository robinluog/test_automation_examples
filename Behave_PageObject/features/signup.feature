Feature: Sign Up
    As visitor of Solidopinion.com
    I want to have opportunity for Sign Up
    So that I will have possibility to use all features


@negative @empty_all
Scenario: Sign Up with empty data
    Given I'm on SignUp page
    When  I click SIGNUP_BUTTON
    Then  I see message: All fields are required.

@negative @name
Scenario: Sign Up just with name
    Given I'm on SignUp page
    When  I fill form
        | name       | value |
        | NAME_INPUT | NAME  |

    And   I click SIGNUP_BUTTON
    Then  I see message: All fields are required.

@negative @name
Scenario: Sign Up with empty name
    Given I'm on SignUp page
    When  I fill form
        | name        | value    |
        | EMAIL_INPUT | EMAIL    |
        | PASS_INPUT  | PASSWORD |
        | PASS2_INPUT | PASSWORD |

    And  I click SIGNUP_BUTTON
    Then I see message: Apologies, "Name" allows only alphanumeric characters, hyphen, dash, underscores and spaces.

@negative @email
Scenario: Sign Up with invalid email
    Given I'm on SignUp page
    When  I fill form
        | name        | value     |
        | NAME_INPUT  | NAME      |
        | EMAIL_INPUT | EMAIL_BAD |
        | PASS_INPUT  | PASSWORD  |
        | PASS2_INPUT | PASSWORD  |

    And  I click SIGNUP_BUTTON
    Then I see message: Please enter a valid email address.

@negative @email
Scenario: Sign Up with empty email
    Given I'm on SignUp page
    When  I fill form
        | name        | value     |
        | NAME_INPUT  | NAME      |
        | PASS_INPUT  | PASSWORD  |
        | PASS2_INPUT | PASSWORD  |

    And   I click SIGNUP_BUTTON
    Then  I see message: Please enter a valid email address.

@negative @email
Scenario: Sign Up just with email
    Given I'm on SignUp page
    When  I fill form
        | name        | value |
        | EMAIL_INPUT | EMAIL |

    And  I click SIGNUP_BUTTON
    Then I see message: Apologies, "Name" allows only alphanumeric characters, hyphen, dash, underscores and spaces.

@negative @password
Scenario: Sign Up with invalid short password
    Given I'm on SignUp page
    When  I fill form
         | name        | value    |
         | NAME_INPUT  | NAME     |
         | EMAIL_INPUT | EMAIL    |
         | PASS_INPUT  | PASS_BAD |
         | PASS2_INPUT | PASS_BAD |

    And  I click SIGNUP_BUTTON
    Then I see message: Password must have from 6 to 20 characters

@negative @password
Scenario: Sign Up with empty password
    Given I'm on SignUp page
    When  I fill form
        | name        | value |
        | NAME_INPUT  | NAME  |
        | EMAIL_INPUT | EMAIL |

    And  I click SIGNUP_BUTTON
    Then I see message: Sorry, password can't be blank.

@negative @password
Scenario: Sign Up with different passwords
    Given I'm on SignUp page
    When  I fill form
        | name        | value    |
        | NAME_INPUT  | NAME     |
        | EMAIL_INPUT | EMAIL    |
        | PASS_INPUT  | PASSWORD |
        | PASS2_INPUT | PASS_BAD |

    And  I click SIGNUP_BUTTON
    Then I see message: Oops! Your passwords don’t match, try again.

@positive @full
Scenario: Sign Up with good data
    Given I'm on SignUp page
    When  I fill form
        | name        | value    |
        | NAME_INPUT  | NAME     |
        | EMAIL_INPUT | EMAIL    |
        | PASS_INPUT  | PASSWORD |
        | PASS2_INPUT | PASSWORD |

    And   I click SIGNUP_BUTTON
    Then  I see message: Welcome to SolidOpinion!
