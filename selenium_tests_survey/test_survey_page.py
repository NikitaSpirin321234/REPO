from survey_page import survey_page
from start_page import start_page
from selenium.webdriver import Chrome


import unittest


class test_new_survey_page(unittest.TestCase):
    season = "autumn"
    driver = Chrome()
    page = start_page(driver, season)
    driver.get(page.site_path)

    def tearDown(self):
        # self.driver.refresh()
        print(1)

    def test_validation_1direction_1semester_survey_success(self):
        choosing_direction = self.page.choose_direction(1)
        self.assertNotEqual(choosing_direction, None)
        choosing_sem = self.page.choose_sem(1)
        self.assertNotEqual(choosing_sem, None)
        value_id = self.page.write_id("123")
        self.assertNotEqual(value_id, None)
        self.page = self.page.click_start_button_success()
        self.assertNotEqual(self.page, None)

        next_teacher = self.page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)
        rating_relevance = self.page.choose_rating_relevance(2)
        self.assertNotEqual(rating_relevance, None)
        rating_quality = self.page.choose_rating_quality(3)
        self.assertNotEqual(rating_quality, None)

        next_teacher = self.page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)

        next_teacher = self.page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)
        rating_relevance = self.page.choose_rating_relevance(4)
        self.assertNotEqual(rating_relevance, None)
        rating_quality = self.page.choose_rating_quality(5)
        self.assertNotEqual(rating_quality, None)

        next_teacher = self.page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)

        next_teacher = self.page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)

        self.page = self.page.click_finish_button_success()
        self.assertNotEqual(self.page, None)

        expected_finish_text = "Спасибо за участие в опросе!"
        finish_text = self.page.get_final_text()
        self.assertEqual(finish_text, expected_finish_text)

    def test_validation_1direction_1semester_survey_alert(self):
        choosing_direction = self.page.choose_direction(1)
        self.assertNotEqual(choosing_direction, None)
        choosing_sem = self.page.choose_sem(1)
        self.assertNotEqual(choosing_sem, None)
        value_id = self.page.write_id("123")
        self.assertNotEqual(value_id, None)
        self.page = self.page.click_start_button_success()
        self.assertNotEqual(self.page, None)

        next_teacher = self.page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)
        rating_relevance = self.page.choose_rating_relevance(2)
        self.assertNotEqual(rating_relevance, None)
        rating_quality = self.page.choose_rating_quality(3)
        self.assertNotEqual(rating_quality, None)

        next_teacher = self.page.show_next_teacher()
        self.assertNotEqual(next_teacher, None)
        print(next_teacher)

        self.page = self.page.click_finish_button_alert()
        self.assertNotEqual(self.page, None)

# To DO
        alert = self.page.find_alert()
        self.assertNotEqual(alert, None)

        alert_text = alert.text
        # print(alert_text)
        expected_alert_text = 'Обязательные поля не заполнены'
        self.assertEqual(alert_text, expected_alert_text)

        # rating_relevance = new_survey_page.choose_rating_relevance(4)
        # self.assertNotEqual(rating_relevance, None)
        # rating_quality = new_survey_page.choose_rating_quality(3)
        # self.assertNotEqual(rating_quality, None)

