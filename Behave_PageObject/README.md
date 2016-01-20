# Python + Selenium + Behave + PageObject + Locators

For run go to "Behave_PageObject" folder and just call
`behave`

For run behave in debug mode run
`behave -D BEHAVE_DEBUG_ON_ERROR`
but in that case you need to install *ipdb*:
`sudo pip install ipdb`

For run behave with generating report in XML run:
`behave --junit`

For run specified by tags tests:
`behave --tags=tag1,tag2`

For run all except tagged test:
`behave --tags=-tag3`
