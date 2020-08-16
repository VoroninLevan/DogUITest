from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
    Base Page which contains the wrappers for selenium

    Other page objects should be inherited from this class
    """

    XPATH = By.XPATH
    ID = By.ID
    CLASS_NAME = By.CLASS_NAME

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.short_wait = WebDriverWait(driver, 5)

    def get_sub_element(self, element, identifier):
        """
        Finds and returns sub element of a parent

        :param element: web element -> Parent element
        :param identifier: str -> sub-element xPath
        :return: web element
        """
        try:
            self.wait.until(ec.visibility_of(element))
            return element.find_element_by_xpath("." + identifier)
        except TimeoutException:
            print("Timeout - Cannot find sub-element: " + identifier)

    def get_element(self, by, identifier):
        """
        Finds and returns web element

        :param by: Currently supports following: xPath, Id, Class name
        :param identifier: str ->Elements unique identifier
        :return: web element
        """
        try:
            return self.wait.until(ec.presence_of_element_located((by, identifier))
                                   and ec.element_to_be_clickable((by, identifier)))
        except TimeoutException:
            print("Timeout - Cannot find an element by " + by + ": " + identifier)

    def __get_element(self, by, identifier):
        """
        Finds and returns web element

        :param by: Currently supports following: xPath, Id, Class name
        :param identifier: str ->Elements unique identifier
        :return: web element
        """
        return self.short_wait.until(ec.presence_of_element_located((by, identifier))
                                     and ec.element_to_be_clickable((by, identifier)))

    def get_elements(self, by, identifier):
        """
        Finds and returns list of web elements with the same identifier

        :param by: Currently supports following: xPath, Id, Class name
        :param identifier: str -> Elements unique identifier
        :return: List of web elements
        """
        try:
            return self.wait.until(ec.presence_of_all_elements_located((by, identifier)))
        except TimeoutException:
            print("Timeout - Cannot find an elements by " + by + ": " + identifier)

    def click(self, by, identifier):
        """
        Clicks desired web element

        :param by: Currently supports following: xPath, Id, Class name
        :param identifier: str -> Elements unique identifier
        :return:
        """
        self.get_element(by, identifier).click()

    def enter(self, by, identifier, string):
        """
        Send desired text to the input field

        :param by: Currently supports following: xPath, Id, Class name
        :param identifier: str -> Elements unique identifier
        :param string: str -> Desired text to be send
        :return: -
        """
        self.get_element(by, identifier).send_keys(string)

    def clear_field(self, by, identifier):
        """
        Clears input field

        :param by: Currently supports following: xPath, Id, Class name
        :param identifier: str -> Elements unique identifier
        :return: -
        """
        self.get_element(by, identifier).clear()

    def navigate(self, url):
        """
        Navigates to the pages url

        :param url: str -> Page url
        :return: -
        """
        self.driver.get(url)

    def is_element_exists(self, by, identifier):
        """
        Checks whether element exists on the page

        :param by: Currently supports following: xPath, Id, Class name
        :param identifier: str -> Elements unique identifier
        :return: True - exists / False - not exists
        """
        try:
            self.__get_element(by, identifier)
            return True
        except TimeoutException:
            return False
