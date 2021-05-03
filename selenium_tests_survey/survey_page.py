from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from finish_page import finish_page
from selenium.webdriver.common.action_chains import ActionChains


def try_except(func, *args):
    try:
        return func(*args)
    except NoSuchElementException:
        return None


def try_except_find_by_xpath(elem, *args):
    try:
        return elem.find_element_by_xpath(*args)
    except NoSuchElementException:
        return None


class survey_page:
    def __init__(self, driver, season):
        self.season = season
        self.driver = driver
        self.site_path = "http://" + season + ".survey.moevm.info/"
        self.current_name_teacher = None
        self.current_subject = None

    def show_next_teacher(self):
        if self.current_name_teacher is None:
            xpath = '//a[@name]'
        else:
            xpath = f'//a[@name="{self.current_name_teacher}"]/following::div[1][@class="content"]/b[2][text()' \
                    f'="{self.current_subject}"]/following-sibling::a[@name] '
        find_func = self.driver.find_element_by_xpath
        next_teacher = try_except(find_func, xpath)
        if next_teacher is None:
            return None
        else:
            self.current_name_teacher = next_teacher.get_attribute("name")

            xpath = './following::div[1][@class="content"]/b[2]'

            # next_subject = next_teacher.find_element_by_xpath(xpath)

            next_subject = try_except_find_by_xpath(next_teacher, xpath)

            if next_subject is None:
                return None
            else:
                self.current_subject = next_subject.text

        return self.current_name_teacher

    def choose_rating_relevance(self, rating):
        if self.current_name_teacher is None:
            return None
        else:
            xpath = f"//a[@name='{self.current_name_teacher}']/following::div[1][@class='content']/b[2][text(" \
                    f")='{self.current_subject}']/following::div[@data-toggle][1]//input[@value='{rating - 1}'] "
        find_func = self.driver.find_element_by_xpath
        radio_rating = try_except(find_func, xpath)

        if radio_rating is None:
            return None
        else:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))))

            return radio_rating

    def choose_rating_quality(self, rating):
        if self.current_name_teacher is None:
            return None
        else:
            xpath = f"//a[@name='{self.current_name_teacher}']/following::div[1][@class='content']/b[2][text(" \
                    f")='{self.current_subject}']/following::div[@data-toggle][2]//input[@value='{rating - 1}'] "
        find_func = self.driver.find_element_by_xpath
        radio_rating = try_except(find_func, xpath)
        if radio_rating is None:
            return None
        else:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))))
            return radio_rating

    def click_finish_button(self):
        xpath = f'//div[@id="div_submit_results"]//button[@id="submit_results"]'
        find_func = self.driver.find_element_by_xpath
        button_finish = try_except(find_func, xpath)
        if button_finish is None:
            return None
        else:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))))
            return True

    def click_finish_button_success(self):
        if self.click_finish_button() is True:
            return finish_page(self.driver, self.season)
        else:
            return None

    def click_finish_button_alert(self):
        if self.click_finish_button() is True:
            return survey_page(self.driver, self.season)
        else:
            return None

    def find_alert(self):
        xpath = '//div[@id="div_submit_results"]//div[@role="alert"]//strong'
        find_func = self.driver.find_element_by_xpath
        alert = try_except(find_func, xpath)
        if alert is None:
            return None
        else:
            return alert

            # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            # self.driver.execute_script("arguments[0].scrollIntoView();",
            #                            WebDriverWait(self.driver, 20).until(
            #                                EC.visibility_of_element_located((By.XPATH, xpath))))
            # ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 20).until(
            #     EC.element_to_be_clickable((By.XPATH, xpath)))).click().perform()
            # ActionChains(self.driver).move_to_element(radio_rating).perform()
            # WebDriverWait(self.driver, 3).until(EC.invisibility_of_element(radio_rating))
            # WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            # radio_rating.click()
            # ActionChains(self.driver).move_to_element_with_offset(radio_rating, 50, 50).click().perform()
            # self.driver.implicitly_wait(8)

            # self.driver.execute_script("arguments[0].scrollIntoView();", radio_rating)

            # WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable((By.XPATH, xpath)))

            # radio_rating.click()

            # ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(xpath)).perform()

            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # radio_rating.click()
