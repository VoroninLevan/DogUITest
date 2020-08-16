import json
import unittest
import xmlrunner as xmlrunner
import main.parserxml as px
from main.page.dogmainpage import DogMainPage
from main.page.jsonresponsepage import JsonResponsePage
from selenium import webdriver


class Runner(unittest.TestCase):

    def setUp(self):
        true = 'True'
        if px.get_profile() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        if px.get_full_screen() in true:
            self.driver.fullscreen_window()
        else:
            self.driver.set_window_size(px.get_width(), px.get_height())
        self.driver.get('https://dog.ceo/dog-api/')

    def test_documentation_path_links(self):
        """
        Test navigates through the 'Documentation' tabs and verifies the links to tabs by asserting
        expected titles against given ones.
        NOTE: As the application does not contain complicated workflow and URLs, it is possible to assert the URLs
        instead.

        :return:
        """
        main_page = DogMainPage(self.driver)
        dog_page = main_page.navigate_documentation()
        # Switch to 'List all breeds' tab
        all_breeds_page = dog_page.switch_tab(dog_page.ALL_BREEDS)
        all_breeds_expected = all_breeds_page.get_expected_header()
        all_breeds_header = all_breeds_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(all_breeds_expected, all_breeds_header,
                         ('%s expected, instead found: %s. Page is wrong' % (all_breeds_expected, all_breeds_header)))
        # Switch to 'Random image' tab
        random_page = dog_page.switch_tab(dog_page.RANDOM)
        random_expected_header = random_page.get_expected_header()
        random_header = random_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(random_expected_header, random_header,
                         ('%s expected, instead found: %s. Page is wrong' % (random_expected_header, random_header)))
        # Switch to 'By breed' tab
        breed_page = dog_page.switch_tab(dog_page.BREED)
        breed_expected_header = breed_page.get_expected_header()
        breed_header = breed_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(breed_expected_header, breed_header,
                         ('%s expected, instead found: %s. Page is wrong' % (breed_expected_header, breed_header)))
        # Switch to 'By sub-breed' tab
        sub_breed_page = dog_page.switch_tab(dog_page.SUB_BREED)
        sub_expected_header = sub_breed_page.get_expected_header()
        sub_header = sub_breed_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(sub_expected_header, sub_header,
                         ('%s expected, instead found: %s. Page is wrong' % (sub_expected_header, sub_header)))

    def test_menu_path_links(self):
        """
        Test navigates through the menu options and verifies the page links by asserting
        expected titles against given ones.
        NOTE: As the application does not contain complicated workflow and URLs, it is possible to assert the URLs
        instead.
        NOTE: As the Title page has inner tags in title, it was decided to use substring for assertion

        :return:
        """
        main_page = DogMainPage(self.driver)
        # Navigate to Title (main) page
        title_page = main_page.navigate_main()
        title_expected_header = title_page.get_expected_header()
        title_header = title_page.get_header()
        # Assert the title by sub-string to verify page
        self.assertTrue(title_expected_header in title_header,
                        ('%s expected, instead found: %s. Page is wrong' % (title_expected_header, title_header)))
        # Navigate to 'Documentation' page
        doc_page = main_page.navigate_documentation()
        doc_expected = doc_page.get_expected_header()
        doc_header = doc_page.get_header()
        # Assert the title to verify page
        self.assertEqual(doc_expected, doc_header,
                         ('%s expected, instead found: %s. Page is wrong' % (doc_expected, doc_header)))
        # Navigate to 'Breed list' page
        breed_list_page = main_page.navigate_breeds_list()
        breed_list_expected_header = breed_list_page.get_expected_header()
        breed_list_header = breed_list_page.get_header()
        # Assert the title to verify page
        self.assertEqual(breed_list_expected_header, breed_list_header,
                         ('%s expected, instead found: %s. Page is wrong' %
                          (breed_list_expected_header, breed_list_header)))
        # Navigate to 'About' page
        about_page = main_page.navigate_about()
        about_expected_header = about_page.get_expected_header()
        about_header = about_page.get_header()
        # Assert the title to verify page
        self.assertEqual(about_expected_header, about_header,
                         ('%s expected, instead found: %s. Page is wrong' % (about_expected_header, about_header)))

    def test_email_form(self):
        """
        For testing email text field
        NOTE: Due to email field does not have any restrictions/checks for, e.g. specific patterns, special characters
        (looks like length as well) and due to the value passes on to the external web page which is out of scope -
        there are no visible scenarios here to test, except of pen testing which is out of scope of the task.
        So this is a dummy test for testing the text field.

        :return:
        """
        dummy_email = 'dummy@d.c'
        main_page = DogMainPage(self.driver)
        main_page.populate_email(dummy_email)
        self.assertEqual(dummy_email, main_page.get_value_email(), 'Expected conditions failed.')
        
    def test_multiple_random_image_entries_api(self):
        # Test data
        url = 'https://dog.ceo/api/breeds/image/random/'
        expected_number_of_entries = 3
        # Navigate to response page -> collect raw data (str)
        json_response_page = JsonResponsePage(self.driver, url + str(expected_number_of_entries))
        json_response_page.switch_to_raw_data()
        raw_data = json_response_page.get_raw_json()
        # Load raw data as dict, assert number of entries against expected number
        json_dict = json.loads(raw_data)
        number_of_entries = len(json_dict['message'])
        self.assertEqual(expected_number_of_entries, number_of_entries,
                         '%s number of entries expected, instead %s found' %
                         (expected_number_of_entries, number_of_entries))

    def test_by_sub_breed_entries_api(self):
        # Test data
        url = 'https://dog.ceo/api/breed/hound/list'
        expected_entries = 7
        # Navigate to response page -> collect raw data (str)
        json_response_page = JsonResponsePage(self.driver, url)
        json_response_page.switch_to_raw_data()
        raw_data = json_response_page.get_raw_json()
        # Load raw data as dict, assert number of entries against expected number
        json_dict = json.loads(raw_data)
        number_of_entries = len(json_dict['message'])
        self.assertEqual(expected_entries, number_of_entries,
                         '%s number of entries expected, instead %s found. The amount of entries might be changed.' %
                         (expected_entries, number_of_entries))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False
    )
