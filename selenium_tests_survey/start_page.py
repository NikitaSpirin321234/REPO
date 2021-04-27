# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from survey_page import survey_page
# import chromedriver
# from selenium.webdriver import Chrome
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


def try_except(func, *args):
    try:
        return func(*args)
    except NoSuchElementException:
        return None


class start_page:
    # driver.implicitly_wait(10)

    def __init__(self, driver, season):
        # self.driver = ;
        # self.driver = WebDriver(executable_path="/bin")
        # Webdriver("./venv/bin/chromedriver");
        # self.driver = Chrome()
        self.season = season
        self.driver = driver
        self.site_path = "http://" + season + ".survey.moevm.info/"

    def choose_direction(self, num_direction):
        xpath = f'//div[@class="radio btn_choice_sem"]//input[@value="{num_direction}"]'
        find_func = self.driver.find_element_by_xpath
        radio_direction = try_except(find_func, xpath)
        if radio_direction is None:
            return None
        else:
            radio_direction.click()
            return num_direction

    def choose_sem(self, num_sem):
        xpath = f'//div[@id="div_sem_choice"]//input[@value="{num_sem}"]'
        find_func = self.driver.find_element_by_xpath
        radio_sem = try_except(find_func, xpath)
        if radio_sem is None:
            return None
        else:
            radio_sem.click()
            return num_sem

    def write_id(self, input_id):
        id = "ID"
        find_func = self.driver.find_element_by_id
        field_id = try_except(find_func, id)
        if field_id is None:
            return None
        else:
            field_id.send_keys(input_id)
            value_id = field_id.get_attribute("value")
            return value_id

    def click_start_button(self):
        xpath = f'//div[@id="btn-submit"]//button[@class="btn btn-outline-dark"]'
        find_func = self.driver.find_element_by_xpath
        button_start = try_except(find_func, xpath)
        if button_start is None:
            return None
        else:
            button_start.click()
            return True

    def click_start_button_success(self):
        if self.click_start_button() is True:
            return survey_page(self.driver, self.season)
        else:
            return None

    def click_start_button_alert(self):
        if self.click_start_button() is True:
            return start_page(self.driver, self.season)
        else:
            return None

    def find_alert(self):
        xpath = f'//div[@id="alert"]//div[@role="alert"]//strong'
        find_func = self.driver.find_element_by_xpath
        alert = try_except(find_func, xpath)
        if alert is None:
            return None
        else:
            return alert

    # def click_start_button_success(self):
    #    self.click_start_button()
    #    return


# class startPage(PageFactory):
#     # driver.implicitly_wait(10)
#
#     def __init__(self, season):
#         self.driver = Chrome()
#         self.sitePath = "http://" + season + ".survey.moevm.info/"
#
#     locators ={
#         "radio_direction" ('XPATH', )
#     }
#
#     def choose_direction(self, num_direction):
#         xpath = f'//div[@class="radio btn_choice_sem"]//input[@value="{num_direction}"]'
#         find_func = self.driver.find_element_by_xpath
#         radio_direction = try_except(find_func, xpath)
#         if radio_direction is None:
#             return None
#         else:
#             radio_direction.click()
#             return num_direction
#
#     def choose_sem(self, num_sem):
#         xpath = f'//div[@id="div_sem_choice"]//input[@value="{num_sem}"]'
#         find_func = self.driver.find_element_by_xpath
#         radio_sem = try_except(find_func, xpath)
#         if radio_sem is None:
#             return None
#         else:
#             radio_sem.click()
#             return num_sem
#
#     def write_id(self, input_id):
#         id = "ID"
#         find_func = self.driver.find_element_by_id
#         field_id = try_except(find_func, id)
#         if field_id is None:
#             return None
#         else:
#             field_id.send_keys(input_id)
#             value_id = field_id.get_attribute("value")
#             return value_id
#
#     def click_start_button(self):
#         xpath = f'//div[@id="btn-submit"]//button[@class="btn btn-outline-dark"]'
#         find_func = self.driver.find_element_by_xpath
#         button_start = try_except(find_func, xpath)
#         if button_start is None:
#             return None
#         else:
#             button_start.click()