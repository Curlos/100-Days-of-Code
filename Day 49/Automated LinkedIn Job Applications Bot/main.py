from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os


class JobApplicationBot():
    def __init__(self):
        load_dotenv()
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
        self.LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")

        username.send_keys(self.LINKEDIN_EMAIL)
        password.send_keys(self.LINKEDIN_PASSWORD)
        password.send_keys(Keys.ENTER)

    def save_job(self, job_name="software developer", pages=5):
        self.driver.get("https://www.linkedin.com/jobs/search/")
        time.sleep(3)
        job_search = self.driver.find_element_by_css_selector('input.jobs-search-box__text-input.jobs-search'
                                                              '-box__keyboard-text-input')
        job_search.send_keys(job_name)
        job_search.send_keys(Keys.ENTER)
        time.sleep(3)

        disable_messaging = self.driver.find_element_by_id("ember196")
        disable_messaging.click()

        curr_page = 1
        curr_page_str = f"Page {curr_page}"
        saved_jobs = 0

        for i in range(pages):
            start_time = time.time()

            while time.time() - start_time <= 5:
                elem_in_popup = self.driver.find_element_by_css_selector(
                    "a.disabled.ember-view.job-card-container__link.job-card-list__title")
                elem_in_popup.send_keys(Keys.END)

            jobs = self.driver.find_elements_by_css_selector(
                "a.disabled.ember-view.job-card-container__link.job-card-list__title")

            companies = self.driver.find_elements_by_css_selector("a.job-card-container__link.job-card"
                                                                 "-container__company-name.ember-view")
            for i in range(len(jobs)):
                job = jobs[i]
                company = companies[i]
                self.driver.execute_script("arguments[0].scrollIntoView();", job)
                job.click()
                time.sleep(1)

                save_job = self.driver.find_element_by_css_selector(
                    "button.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary")
                save_job.click()
                saved_jobs += 1
                print(f"Saved {job.text} ({company.text})")

            time.sleep(3)

            curr_page += 1
            curr_page_str = f"Page {curr_page}"

            next_page = self.driver.find_element_by_css_selector(f'button[aria-label="{curr_page_str}"]')
            next_page.click()
            time.sleep(3)

        print(f"Saved {saved_jobs} jobs.")

    def apply_for_job(self):
        pass


bot = JobApplicationBot()
bot.login()
bot.save_job()
