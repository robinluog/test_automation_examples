Feature: Sign Up
    As visitor of Solidopinion.com
    I want to have opportunity for Sign Up
    So that I will have possibility to use all features


@negative @empty_all
Scenario: Sign Up with empty data
    Given I'm on SignUp page
    When  I click on button signup
    Then  I see All fields are required.

@negative @name
Scenario: Sign Up just with name
    Given I'm on SignUp page
    When  I fill form
        | name       | value |
        | input name | name  |

    And  I click on button signup
    Then   I see All fields are required.

@negative @name
Scenario: Sign Up with empty name
    Given I'm on SignUp page
    When  I fill form
        | name              | value    |
        | input email       | email    |
        | input password    | password |
        | input re-password | password |

    And  I click on button signup
    Then   I see Apologies, "Name" allows only alphanumeric characters, hyphen, dash, underscores and spaces.

@negative @email
Scenario: Sign Up with invalid email
    Given I'm on SignUp page
    When  I fill form
        | name              | value     |
        | input name        | name      |
        | input email       | bad email |
        | input password    | password  |
        | input re-password | password  |

    And  I click on button signup
    Then   I see Please enter a valid email address.

@negative @email
Scenario: Sign Up with empty email
    Given I'm on SignUp page
    When  I fill form
        | name              | value    |
        | input name        | name     |
        | input password    | password |
        | input re-password | password |

    And  I click on button signup
    Then   I see Please enter a valid email address.

@negative @email
Scenario: Sign Up just with email
    Given I'm on SignUp page
    When  I fill form
        | name        | value |
        | input email | email |

    And  I click on button signup
    Then   I see Apologies, "Name" allows only alphanumeric characters, hyphen, dash, underscores and spaces.

@negative @password
Scenario: Sign Up with invalid short password
    Given I'm on SignUp page
    When  I fill form
        | name              | value          |
        | input name        | name           |
        | input email       | email          |
        | input password    | short password |
        | input re-password | short password |

    And  I click on button signup
    Then   I see Password must have from 6 to 20 characters

@negative @password
Scenario: Sign Up with empty password
    Given I'm on SignUp page
    When  I fill form
        | name              | value |
        | input name        | name  |
        | input email       | email |

    And  I click on button signup
    Then   I see Sorry, password can't be blank.

@negative @password
Scenario: Sign Up with different passwords
    Given I'm on SignUp page
    When  I fill form
        | name              | value          |
        | input name        | name           |
        | input email       | email          |
        | input password    | short password |
        | input re-password | password       |

    And  I click on button signup
    Then   I see Oops! Your passwords don’t match, try again.

@positive @full
Scenario: Sign Up with good data
    Given I'm on SignUp page
    When  I fill form
        | name              | value     |
        | input name        | name      |
        | input email       | email     |
        | input password    | password  |
        | input re-password | password  |

    And   I click on button signup
    Then  I see Welcome to SolidOpinion!
