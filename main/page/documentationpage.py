from main.page.dogmainpage import DogMainPage


class DocumentationPage(DogMainPage):

    DOCUMENTATION = 'ENDPOINTS'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return self.get_element(self.XPATH, "//div[@class='api-side']/h3").text

    def get_expected_doc_header(self):
        return self.DOCUMENTATION

    def switch_tab(self, option):
        """

        :param option:
        :return:
        """
        switch = {
            0: DogMainPage.click(self, DogMainPage.XPATH, "//a[@href='/dog-api/documentation']"),
            1: DogMainPage.click(self, DogMainPage.XPATH, "//a[@href='/dog-api/documentation/random']"),
            2: DogMainPage.click(self, DogMainPage.XPATH, "//a[@href='/dog-api/documentation/breed']"),
            3: DogMainPage.click(self, DogMainPage.XPATH, "//a[@href='/dog-api/documentation/sub-breed']"),
            4: DogMainPage.click(self, DogMainPage.XPATH, "//a[@href='/dog-api/breed-list']")
        }
        switch.get(option, 'Invalid option, please use predefined options in class')
