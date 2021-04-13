from survey_page import survey_page
from start_page import start_page
from selenium.webdriver import Chrome


import unittest


class test_survey_page(unittest.TestCase):
    season = "autumn"
    driver = Chrome()
    page = start_page(driver, season)
    driver.get(page.site_path)

    def test_validation_1direction_1semestr_survey(self):
        choosing_direction = self.page.choose_direction(1)
        self.assertNotEqual(choosing_direction, None)
        choosing_sem = self.page.choose_sem(1)
        self.assertNotEqual(choosing_sem, None)
        # self.driver.implicitly_wait(3)
        value_id = self.page.write_id("123")
        self.assertNotEqual(value_id, None)
        new_page = self.page.click_start_button()
        self.assertNotEqual(new_page, None)
        next_teacher = new_page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)
        next_teacher = new_page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)
        next_teacher = new_page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)

        rating_relevance = new_page.choose_rating_relevance(2)
        self.assertNotEqual(rating_relevance, None)
        # rating_relevance = new_page.choose_rating_relevance(4)
        # self.assertNotEqual(rating_relevance, None)
        # rating_quality = new_page.choose_rating_quality(3)
        # self.assertNotEqual(rating_quality, None)

