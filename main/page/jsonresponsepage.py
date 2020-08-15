from main.page.basepage import BasePage


class JsonResponsePage(BasePage):
    """
    Representation for JSON response data page
    """

    def __init__(self, driver, url):
        super().__init__(driver)
        driver.get(url)

    def switch_to_raw_data(self):
        """
        Switches to 'Raw Data' tab
        :return:
        """
        self.click(self.ID, 'rawdata-tab')

    def get_raw_json(self):
        """
        Retrieves and returns json as str
        :return: str
        """
        return self.get_element(self.CLASS_NAME, 'data').text
