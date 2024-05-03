import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from data_parsing.config import extract_technologies
from data_parsing.items import Vacancy


class DOUWebParser:
    BASE_URL = "https://jobs.dou.ua/vacancies/?category=Python"

    def __init__(self) -> None:
        self.options = Options()
        self.driver = webdriver.Chrome()

    def _has_pagination(self) -> bool:
        try:
            pagination_button = self.driver.find_element(By.CLASS_NAME, "more-btn > a")
            return pagination_button.is_displayed()
        except NoSuchElementException:
            return False

    def _scroll_whole_page(self) -> None:
        while self._has_pagination():
            more_button = self.driver.find_elements(By.CLASS_NAME, "more-btn > a")[0]
            more_button.click()
            time.sleep(0.2)

    def _get_title(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "g-h2").text

    def _get_location(self) -> str | None:
        if location := self.driver.find_elements(By.CLASS_NAME, "bi-geo-alt-fill"):
            return location[0].text
        return None

    def _get_technologies(self) -> str:
        description = self.driver.find_element(By.CLASS_NAME, "vacancy-section").text
        return ", ".join(extract_technologies(description))

    def _parse_single_vacancy(self, link: WebElement, experience: str) -> Vacancy:
        link.click()
        vacancy = Vacancy(
            title=self._get_title(),
            location=self._get_location(),
            experience=experience,
            technologies=self._get_technologies(),
        )
        self.driver.back()

        return vacancy

    def _get_vacancies_by_experience(self, experience: str) -> list[Vacancy]:
        self._scroll_whole_page()
        vacancy_detail_links = self.driver.find_elements(By.CSS_SELECTOR, ".title > a")

        return [
            self._parse_single_vacancy(link, experience)
            for link in vacancy_detail_links
        ]

    def get_all_vacancies(self) -> list[Vacancy]:
        self.driver.get(self.BASE_URL)

        all_vacancies = []

        for index_of_experience in range(1, 5):
            self.driver.find_elements(
                By.CSS_SELECTOR, ".b-region-filter > ul:first-of-type > li"
            )[index_of_experience].click()
            experience = self.driver.find_element(
                By.CLASS_NAME, "selected"
            ).text.replace("\n×", "")
            vacancies_by_experience = self._get_vacancies_by_experience(experience)
            all_vacancies.extend(vacancies_by_experience)
            self.driver.get(self.BASE_URL)
            time.sleep(0.2)

        return all_vacancies
