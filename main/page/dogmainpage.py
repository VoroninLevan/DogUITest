from main.page.basepage import BasePage


class DogMainPage(BasePage):

    URL = 'https://dog.ceo/dog-api/'

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_main(self):
        BasePage.click(self, self.XPATH, "//img[@class='logo']")
        return DogTitlePage(self.driver)

    def navigate_documentation(self):
        BasePage.click(self, self.XPATH, "//a[@href='/dog-api/documentation']")
        return DogDocumentationPage(self.driver)

    def navigate_breeds_list(self):
        BasePage.click(self, self.XPATH, "//a[@href='/dog-api/breeds-list']")
        return DogBreedListPage(self.driver)

    def navigate_about(self):
        BasePage.click(self, self.XPATH, "//a[@href='/dog-api/about']")
        return DogAboutPage(self.driver)

    def populate_email(self, email):
        BasePage.enter(self, self.ID, "mce-EMAIL", email)

    def submit_email(self):
        BasePage.click(self, self.ID, "mc-embedded-subscribe")

    def get_value_email(self):
        return BasePage.get_element(self, self.ID, "mce-EMAIL").get_attribute('value')


class DogDocumentationPage(DogMainPage):

    DOCUMENTATION = 'ENDPOINTS'
    ALL_BREEDS = 0
    RANDOM = 1
    BREED = 2
    SUB_BREED = 3
    BREED_LIST = 4

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return self.get_element(self.XPATH, "//div[@class='api-side']/h3").text

    def get_expected_header(self):
        return self.DOCUMENTATION

    def __navigate_to_all_breeds(self):
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation']")
        return DogDocumentationAllBreedsPage(self.driver)

    def __navigate_to_random(self):
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation/random']")
        return DogDocumentationRandomPage(self.driver)

    def __navigate_to_breed(self):
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation/breed']")
        return DogDocumentationByBreedPage(self.driver)

    def __navigate_to_sub_breed(self):
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/documentation/sub-breed']")
        return DogDocumentationBySubBreedPage(self.driver)

    def __navigate_to_breed_list(self):
        DogMainPage.click(self, self.XPATH, "//a[@href='/dog-api/breed-list']")
        return None

    def switch_tab(self, option):
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

    ALL_BREEDS = 'List all breeds'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return DogDocumentationAllBreedsPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='all']").text

    def get_expected_header(self):
        return self.ALL_BREEDS.upper()


class DogDocumentationRandomPage(DogDocumentationPage):

    RANDOM = 'Display single random image from all dogs collection'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return DogDocumentationRandomPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='all']").text

    def get_expected_header(self):
        return self.RANDOM.upper()


class DogDocumentationByBreedPage(DogDocumentationPage):

    BY_BREED = 'By breed'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return DogDocumentationByBreedPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='breed']").text

    def get_expected_header(self):
        return self.BY_BREED.upper()


class DogDocumentationBySubBreedPage(DogDocumentationPage):

    BY_SUB = 'List all sub-breeds'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return DogDocumentationBySubBreedPage.get_element(self, DogDocumentationPage.XPATH, "//h3[@id='sub-breed']")\
            .text

    def get_expected_header(self):
        return self.BY_SUB.upper()


class DogTitlePage(DogMainPage):

    TITLE_SUB_HEADER = 'The internet\'s biggest collection'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return DogTitlePage.get_element(self, self.XPATH, "//h1[@class='title']").text

    def get_expected_header(self):
        return self.TITLE_SUB_HEADER


class DogBreedListPage(DogMainPage):

    BREED_LIST_HEADER = 'Breeds list'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return DogBreedListPage.get_element(self, DogBreedListPage.XPATH, "//h3").text

    def get_expected_header(self):
        return self.BREED_LIST_HEADER.upper()


class DogAboutPage(DogMainPage):

    ABOUT_HEADER = 'About'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return DogAboutPage.get_element(self, DogAboutPage.XPATH, "//h3[@id='about']").text

    def get_expected_header(self):
        return self.ABOUT_HEADER.upper()
