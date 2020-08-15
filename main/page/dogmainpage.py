from main.page.basepage import BasePage


class DogMainPage(BasePage):
    """
    Representation for 'Main' (menu) page
    """

    URL = 'https://dog.ceo/dog-api/'

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_main(self):
        """
        Navigates to 'Title' page

        :return: DogTitlePage
        """
        BasePage.click(self, self.XPATH, "//img[@class='logo']")
        return DogTitlePage(self.driver)

    def navigate_documentation(self):
        """
        Navigates to 'Documentation' page

        :return: DogDocumentationPage
        """
        BasePage.click(self, self.XPATH, "//a[@href='/dog-api/documentation']")
        return DogDocumentationPage(self.driver)

    def navigate_breeds_list(self):
        """
        Navigates to 'Breed list' page

        :return: DogBreedListPage
        """
        BasePage.click(self, self.XPATH, "//a[@href='/dog-api/breeds-list']")
        return DogBreedListPage(self.driver)

    def navigate_about(self):
        """
        Navigates to 'About' page

        :return: DogAboutPage
        """
        BasePage.click(self, self.XPATH, "//a[@href='/dog-api/about']")
        return DogAboutPage(self.driver)

    def populate_email(self, email):
        """
        Populates email text field with desired data

        :param email: str - desired email
        :return:
        """
        BasePage.enter(self, self.ID, "mce-EMAIL", email)

    def submit_email(self):
        """
        Clicks 'Join' button on subscription form

        :return:
        """
        BasePage.click(self, self.ID, "mc-embedded-subscribe")

    def get_value_email(self):
        """
        Gets the value from email text field

        :return: str
        """
        return BasePage.get_element(self, self.ID, "mce-EMAIL").get_attribute('value')


class DogDocumentationPage(DogMainPage):
    """
    Page object for 'Documentation' page
    Contains methods for interaction with elements
    """
    DOCUMENTATION = 'ENDPOINTS'
    ALL_BREEDS = 0
    RANDOM = 1
    BREED = 2
    SUB_BREED = 3
    BREED_LIST = 4

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        Gets and returns header specified on the page

        :return: str
        """
        return self.get_element(self.XPATH, "//div[@class='api-side']/h3").text

    def get_expected_header(self):
        """
        Gets and returns expected header

        :return: str
        """
        return self.DOCUMENTATION

    def __navigate_to_all_breeds(self):
        """
        Navigates to 'List all breeds' tab page

        :return: DogDocumentationAllBreedsPage
        """
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation']")
        return DogDocumentationAllBreedsPage(self.driver)

    def __navigate_to_random(self):
        """
        Navigates to 'Random images' tab page

        :return: DogDocumentationRandomPage
        """
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation/random']")
        return DogDocumentationRandomPage(self.driver)

    def __navigate_to_breed(self):
        """
        Navigates to 'By Breeds' tab page

        :return: DogDocumentationByBreedPage
        """
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation/breed']")
        return DogDocumentationByBreedPage(self.driver)

    def __navigate_to_sub_breed(self):
        """
        Navigates to 'Sub-Breeds' tab page

        :return: DogDocumentationBySubBreedPage
        """
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation/sub-breed']")
        return DogDocumentationBySubBreedPage(self.driver)

    def __navigate_to_breed_list(self):
        """
        Navigates to 'Breed list' page

        :return: None
        """
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/breed-list']")
        return None

    def switch_tab(self, option):
        """
        Switches between tabs under 'Documentation' page

        :param option: numeric value
        :return: Page Object
        """
        if option == 0:
            return self.__navigate_to_all_breeds()
        elif option == 1:
            return self.__navigate_to_random()
        elif option == 2:
            return self.__navigate_to_breed()
        elif option == 3:
            return self.__navigate_to_sub_breed()
        elif option == 4:
            return self.__navigate_to_breed_list()
        else:
            raise ValueError('Wrong option passed: %d. Please use predefined options')


class DogDocumentationAllBreedsPage(DogDocumentationPage):
    """
    Representation for 'List all breeds' tab page
    """

    ALL_BREEDS = 'List all breeds'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        See overridden method

        :return: str
        """
        return DogDocumentationAllBreedsPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='all']").text

    def get_expected_header(self):
        """
        See overridden method

        :return: str
        """
        return self.ALL_BREEDS.upper()


class DogDocumentationRandomPage(DogDocumentationPage):
    """
    Representation for 'Random image' tab page
    """

    RANDOM = 'Display single random image from all dogs collection'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        See overridden method

        :return: str
        """
        return DogDocumentationRandomPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='all']").text

    def get_expected_header(self):
        """
        See overridden method

        :return: str
        """
        return self.RANDOM.upper()


class DogDocumentationByBreedPage(DogDocumentationPage):
    """
    Representation for 'By breed' tab page
    """

    BY_BREED = 'By breed'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        See overridden method

        :return: str
        """
        return DogDocumentationByBreedPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='breed']").text

    def get_expected_header(self):
        """
        See overridden method

        :return: str
        """
        return self.BY_BREED.upper()


class DogDocumentationBySubBreedPage(DogDocumentationPage):
    """
    Representation for 'By sub-breed' tab page
    """

    BY_SUB = 'List all sub-breeds'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        See overridden method

        :return: str
        """
        return DogDocumentationBySubBreedPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='sub-breed']")\
            .text

    def get_expected_header(self):
        """
        See overridden method

        :return: str
        """
        return self.BY_SUB.upper()


class DogTitlePage(DogMainPage):
    """
    Representation for Title page
    """

    TITLE_SUB_HEADER = 'The internet\'s biggest collection'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        See overridden method

        :return: str
        """
        return DogTitlePage.get_element(self, self.XPATH, "//h1[@class='title']").text

    def get_expected_header(self):
        """
        See overridden method

        :return: str
        """
        return self.TITLE_SUB_HEADER


class DogBreedListPage(DogMainPage):
    """
    Representation for 'Breed list' page
    """

    BREED_LIST_HEADER = 'Breeds list'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        See overridden method

        :return: str
        """
        return DogBreedListPage.get_element(self, DogBreedListPage.XPATH, "//h3").text

    def get_expected_header(self):
        """
        See overridden method

        :return: str
        """
        return self.BREED_LIST_HEADER.upper()


class DogAboutPage(DogMainPage):
    """
    Representation for 'About' page
    """

    ABOUT_HEADER = 'About'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        """
        See overridden method

        :return: str
        """
        return DogAboutPage.get_element(self, DogAboutPage.XPATH, "//h3[@id='about']").text

    def get_expected_header(self):
        """
        See overridden method

        :return: str
        """
        return self.ABOUT_HEADER.upper()
