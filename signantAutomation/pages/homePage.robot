*** Settings ***
Documentation    All the page object and keywords of Login page will be maintained here.
Library    SeleniumLibrary

*** Variables ***
${login_link}           css:li>a[href='/login']
${login_username}       id:username
${login_password}       id:password
${login_btn}            xpath://input[@value='Log In']
${homepage_username}    css:ul>li>span
${column_count}         css:#content tr
${value_column}         css:#content tr:nth-child() td:nth-child(2)

*** Keywords ***
Login to Demo App
    [Arguments]    ${username}      ${password}
    click element    ${login_link}
    input text    ${login_username}       ${username}
    input text    ${login_password}       ${password}
    click element    ${login_btn}

Validate User Data
    ${data_val}=    Get Dictionary Values   ${test_data}    sort_keys=False
    ${count}=       Get Element Count       ${column_count}
    ${val}=       Evaluate    ${count} + 1
    FOR    ${index}     IN RANGE    2   ${val}
        ${a}=  Get Text    css:#content tr:nth-child(${index}) td:nth-child(2)
        Should Contain    ${data_val}       ${a}
    END
