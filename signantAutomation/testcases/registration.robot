*** Settings ***
Documentation  To Validate Registration Scenarios
Library  SeleniumLibrary
Test Setup  Open the browser with Demo App
Test Teardown  Close Browser session
Library     Collections
Resource    ../config/config.robot
Resource    ../pages/registerPage.robot


*** Test Cases ***
Validate Registration Feature
    Fill the Registration Form
    Validate Successful Registration
    Reset Database


#Check Database
#    Connect to sqldb

# CONNECT TO DATABASE AND CLEAR ALL ENTRIES AS TEAR DOWN SUITE

*** Keywords ***
#Connect to sqldb
##    Connect To Database Using Custom Params    sqlite3    database='demo_app.sqlite'
#    Connect To Database Using Custom Params    sqlite3      '/Users/sachinpatil/Signant/Flasky/instance/demo_app.sqlite'
#    @{queryResult}      Query    SELECT * FROM users;
##    Row Count is Greater Than X    SELECT * FROM users;    1
##    Check If Exists In Database    SELECT id FROM user WHERE firstname = 'abc_updated';