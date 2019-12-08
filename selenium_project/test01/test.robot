*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://www.5itest.cn/login
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    lixue
    Input Password    lx13552442973
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    #Title Should Be    登录

Input Username
    [Arguments]    ${username}
    Input Text    login_username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    login_password    ${password}

Submit Credentials
    Click Button    js-btn-login

Welcome Page Should Be Open
    Title Should Be    Welcome Page