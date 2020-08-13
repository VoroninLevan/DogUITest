import unittest
import xmlrunner as xmlrunner
import main.parserxml as px
from main.page.dogmainpage import DogMainPage
from selenium import webdriver


class Runner(unittest.TestCase):

    def setUp(self):
        if px.get_profile() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.driver.get('https://dog.ceo/dog-api/')

    def test_documentation_path_links(self):
        """

        :return:
        """
        main_page = DogMainPage(self.driver)
        doc_page = main_page.navigate_documentation()
        # Switch to 'List all breeds' tab
        all_breeds_page = doc_page.switch_tab(doc_page.ALL_BREEDS)
        all_breeds_expected = all_breeds_page.get_expected_header()
        all_breeds_header = all_breeds_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(all_breeds_expected, all_breeds_header,
                         ('%s expected, instead found: %s. Page is wrong' % (all_breeds_expected, all_breeds_header)))
        # Switch to 'Random image' tab
        random_page = doc_page.switch_tab(doc_page.RANDOM)
        random_expected_header = random_page.get_expected_header()
        random_header = random_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(random_expected_header, random_header,
                         ('%s expected, instead found: %s. Page is wrong' % (random_expected_header, random_header)))
        # Switch to 'By breed' tab
        breed_page = doc_page.switch_tab(doc_page.BREED)
        breed_expected_header = breed_page.get_expected_header()
        breed_header = breed_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(breed_expected_header, breed_header,
                         ('%s expected, instead found: %s. Page is wrong' % (breed_expected_header, breed_header)))
        # Switch to 'By sub-breed' tab
        sub_breed_page = doc_page.switch_tab(doc_page.SUB_BREED)
        sub_expected_header = sub_breed_page.get_expected_header()
        sub_header = sub_breed_page.get_header()
        # Assert the title to verify the page
        self.assertEqual(sub_expected_header, sub_header,
                         ('%s expected, instead found: %s. Page is wrong' % (sub_expected_header, sub_header)))

    def test_menu_path_links(self):
        """

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

        :return:
        """
        dummy_email = 'dummy@d.c'
        main_page = DogMainPage(self.driver)
        main_page.populate_email(dummy_email)
        self.assertEqual(dummy_email, main_page.get_value_email(), 'Expected conditions failed. Expected ')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False
    )
