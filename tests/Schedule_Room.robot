*** Variables ***

${HOSTNAME}             127.0.0.1
${PORT}                 8000
${SERVER}               http://${HOSTNAME}:${PORT}/
${BROWSER}              Chrome
${ONESECOND}      		1.0
${THREESECOND}      	3.0
${FIVESECOND}      		5.0
${TENSECOND}      		10.0
${ONEMINUTE}      		60.0
${USER}      			bundit
${PASS}      			ad123456
${DATE1}          15/05/2018
${DATE2}          16/05/2018

*** Settings ***

# Documentation		  Django Robot Tests
Library         	Selenium2Library  timeout=10  implicit_wait=0
# Library         	DjangoLibrary  ${HOSTNAME}  ${PORT}  path=Project/Project  manage=Project/manage.py  settings=Project.settings
Library           BuiltIn
Library           String
Suite Setup     	Start Django and open Browser
Suite Teardown    Stop Django and close Browser


*** Keywords ***

Start Django and open Browser
  # Start Django
  Open Browser    ${SERVER}    ${BROWSER}
  Maximize Browser Window

Stop Django and close Browser
  Close Browser
  # Stop Django

Generate room
  [Arguments]    ${date}    ${room}    ${period}    ${major}
  Focus                         jquery=[name=date_selected]
  Clear Element Text            xpath=//input[@name='date_selected']
  Press Key                     jquery=[name=date_selected]      ${date}

  Select From List By Label     xpath=//select[@name="room_selected"]     ${room}
  Select From List By Value     xpath=//select[@name="period_selected"]    ${period}
  Select From List By Label     xpath=//select[@name="major_selected"]    ${major}
  Click button                  Generate

*** Test Cases ***

As a visitor I can visit the django default page
  Input Text    			name=username			${USER}
  Input Text    			name=password			${PASS}
  Click Element 			id=btn_login
  Sleep     				${ONESECOND}

visit manage_page before create schedule room
  Click Link    link=จัดห้องสอบ
  Sleep    		${ONESECOND}

create schedule room
  Click button 						      Reset

  Generate room      ${DATE1}      M03      0      Software Development
  Generate room      ${DATE1}      M04      0      Software Development
  Generate room      ${DATE1}      M03      1      Software Development
  Generate room      ${DATE1}      M04      1      Software Development
  Generate room      ${DATE1}      M21      0      Multimedia
  Generate room      ${DATE1}      M21      1      Multimedia
  Generate room      ${DATE1}      M22      0      Network and Communication
  Generate room      ${DATE1}      M23      0      Data Science

  Generate room      ${DATE2}      M03      0      Business Intelligence
  Generate room      ${DATE2}      M03      1      Business Intelligence
  Generate room      ${DATE2}      M04      1      Embedded Systems
  Generate room      ${DATE2}      M04      0      Data Science
  Generate room      ${DATE2}      M21      0      Data Science
  Generate room      ${DATE2}      M21      1      Data Science
  Generate room      ${DATE2}      M21      1      Multimedia
  Generate room      ${DATE2}      M22      0      Multimedia
  Generate room      ${DATE2}      M22      1      Software Development
  Generate room      ${DATE2}      M23      0      Embedded Systems
  Generate room      ${DATE2}      M23      0      Software Development
  Generate room      ${DATE2}      M21      0      Business Intelligence
  Generate room      ${DATE2}      M23      1      Network and Communication

  Sleep     						        ${FIVESECOND}