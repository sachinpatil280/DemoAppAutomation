*** Settings ***
Documentation    All the page object and keywords of Register page will be maintained here.
Library    SeleniumLibrary
Library    Collections
Library    ../customLibraries/apiCall.py

*** Variables ***
${register_link}    css:li>a[href='/register']
${username}         id:username
${password}         id:password
${firstname}        id:firstname
${lastname}         id:lastname
${phone}            id:phone
${register_btn}     css:input[type='submit']
${exp_url}          http://localhost:8080/login
&{test_data}        username=TestUser       password=TestUser   firstname=Test  lastname=User   phone=9877123123

*** Keywords ***
Fill the Registration Form
    Set Global Variable    ${test_data}
    click element   ${register_link}
    input text      ${username}       ${test_data.username}
    input text      ${password}       ${test_data.password}
    input text      ${firstname}      ${test_data.firstname}
    input text      ${lastname}       ${test_data.lastname}
    input text      ${phone}          ${test_data.phone}
    click element   ${register_btn}
    Wait Until Location Is      ${exp_url}      4

Validate Successful Registration
    ${url_val}=         Get Location
    Should Be Equal     ${exp_url}          ${url_val}
    ${val}=     get_status   ${test_data.username}     ${test_data.password}
    Should Be Equal    ${val}       SUCCESS