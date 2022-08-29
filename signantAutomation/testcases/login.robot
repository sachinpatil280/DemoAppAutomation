*** Settings ***
Documentation  To Validate Login Scenarios
Library  SeleniumLibrary
Test Setup  Open the browser with Demo App
Test Teardown  Close Browser session
Library     Collections
Resource  ../config/config.robot
Resource    ../pages/homePage.robot


*** Test Cases ***
Validate Login Feature
    Login to Demo App       TestUser     TestUser
    Validate User Data
