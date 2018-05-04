Feature: ROI viewer app

  Scenario: Open the app
    Given ROI viewer is running
    When I open 'http://localhost:3000'
    Then I should see the title 'Welcome to ROI!'
    And I should see a percent-sign logo
