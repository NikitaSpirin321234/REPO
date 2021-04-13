from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def try_except(func, *args):
    try:
        return func(*args)
    except NoSuchElementException:
        return None


class survey_page:
    def __init__(self, driver, season):
        # self.driver = Chrome()
        self.driver = driver
        self.site_path = "http://" + season + ".survey.moevm.info/"
        self.current_name_teacher = None

    def show_next_teacher(self):
        if self.current_name_teacher is None:
            xpath = '//a[@name]'
        else:
            xpath = f'//a[@name="{self.current_name_teacher}"] /following::div[1][@class="content"]/a[@name]'
        find_func = self.driver.find_element_by_xpath
        next_teacher = try_except(find_func, xpath)
        if next_teacher is None:
            return None
        else:
            self.current_name_teacher = next_teacher.get_attribute("name")
            return self.current_name_teacher

    def choose_rating_relevance(self, rating):
        if self.current_name_teacher is None:
            return None
        else:
            xpath = f'//a[@name="{self.current_name_teacher}"]/following::div[1][@class="content"]' \
                    f'/div[@data-toggle][1]//input[@value="{rating - 1}"]'
        find_func = self.driver.find_element_by_xpath
        radio_rating = try_except(find_func, xpath)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        if radio_rating is None:
            return None
        else:
            radio_rating.click()
            return radio_rating

    def choose_rating_quality(self, rating):
        if self.current_name_teacher is None:
            return None
        else:
            xpath = f'//a[@name="{self.current_name_teacher}"]/following::div[1][@class="content"]' \
                    f'/div[@data-toggle][2]//input[@value="{rating - 1}"]'
        find_func = self.driver.find_element_by_xpath
        radio_rating = try_except(find_func, xpath)
        if radio_rating is None:
            return None
        else:
            radio_rating.click()
            return radio_rating
