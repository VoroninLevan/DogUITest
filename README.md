# DogUITest code challenge

This is an app to test UI side of 'Dog API' web site. Contains own small framework (wrapper over Selenium) to ease navigation, wait times handling, elements interaction.
Test - Page separation in place for easier app maintainability.

### Tests:

* `test_documentation_path_links()` - tests tab links under *Documentation* page, by asserting tab titles.
* `test_menu_path_links()` - tests menu links, by asserting page titles.

NOTE: URL assertion might be used in above tests instead, to verify links->pages

### Parameters

`parameters.xml` used to configure the following:
* `<profile>` - desired browser for testing. Currently supports **firefox** and **chrome**
* `<fullscreen>` - accepts one of two values: **True** or **False**. Set to **True** in order to have fullscreen browser window
* `<width>` - px value, e.g. **1024**, browser window width. NOTE: ignored if `<fullscreen>` set to **True**
* `<height>` - px value, e.g. **768**, browser window height. NOTE: ignored if `<fullscreen>` set to **True**

### Framework:

**Test** from **page** separation - contains **BasePage** class which is a parent class of all page classes

#### BasePage:

Contains navigation methods for interacting with web elements, handles wait times. Parent class for other classes which represent pages.

#### ParameterReader:

Parses parameter.xml file

**NOTE**

In order to use the app, geckodriver/chromedriver executables should be in system path.
`data/drivers/` contains the following versions:
* geckodriver - v0.27.0 (linux)
* chromedriver - v84.0.4147.30 (linux)
