from start_page import start_page
import unittest
from selenium.webdriver import Chrome


class test_start_page(unittest.TestCase):
    season = "autumn"
    page = start_page(Chrome(), season)
    driver = page.driver
    driver.get(page.site_path)

    # self.driver.implicitly_wait(3)
    # driver.set_page_load_timeout(3)

    def test_choosing_directions(self):
        choosing_direction = self.page.choose_direction(1)
        self.assertNotEqual(choosing_direction, None)
        choosing_direction = self.page.choose_direction(2)
        self.assertNotEqual(choosing_direction, None)
        choosing_direction = self.page.choose_direction(3)
        self.assertNotEqual(choosing_direction, None)
        choosing_direction = self.page.choose_direction(4)
        self.assertNotEqual(choosing_direction, None)

    def test_choosing_semesters_from_first_direction(self):
        self.page.choose_direction(1)
        choosing_sem = self.page.choose_sem(1)
        self.assertNotEqual(choosing_sem, None)
        # self.driver.implicitly_wait(3)
        choosing_sem = self.page.choose_sem(3)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(5)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(7)
        self.assertNotEqual(choosing_sem, None)

    def test_choosing_semesters_from_second_direction(self):
        self.page.choose_direction(2)
        choosing_sem = self.page.choose_sem(1)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(3)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(5)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(7)
        self.assertNotEqual(choosing_sem, None)

    def test_choosing_semesters_from_third_direction(self):
        self.page.choose_direction(3)
        choosing_sem = self.page.choose_sem(1)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(3)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(5)
        self.assertEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(7)
        self.assertEqual(choosing_sem, None)

    def test_choosing_semesters_from_fourth_direction(self):
        self.page.choose_direction(4)
        choosing_sem = self.page.choose_sem(1)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(3)
        self.assertNotEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(5)
        self.assertEqual(choosing_sem, None)
        choosing_sem = self.page.choose_sem(7)
        self.assertEqual(choosing_sem, None)

    def test_input_id(self):
        input_value_id = "123"
        output_value_id = self.page.write_id(input_value_id)
        self.assertNotEqual(output_value_id, None)
        self.assertEqual(input_value_id, output_value_id)

    def test_alert_choosing_sem(self):
        self.page.choose_direction(1)
        url_before_click = self.driver.current_url
        alert = self.page.click_start_button_alert()
        url_after_click = self.driver.current_url
        self.assertEqual(url_before_click, url_after_click)
        alert_text = alert.text
        expected_alert_text = "Пожалуйста, выберите семестр!"
        self.assertEqual(alert_text, expected_alert_text)

    def test_alert_filling_id(self):
        self.page.choose_direction(1)
        self.page.choose_sem(5)
        url_before_click = self.driver.current_url
        alert = self.page.click_start_button_alert()
        url_after_click = self.driver.current_url
        self.assertEqual(url_before_click, url_after_click)
        alert_text = alert.text
        expected_alert_text = 'Пожалуйста, заполните поле "Идентификатор"!'
        self.assertEqual(alert_text, expected_alert_text)

    def test_start_survey(self):
        self.page.choose_direction(1)
        self.page.choose_sem(5)
        # self.page.write_id("123")
        self.page.click_start_button()
