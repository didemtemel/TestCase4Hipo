import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):
    def test_firsttest(self):
        # Starting our WebDriver and navigate to Google
        driver_path = "/Users/didem/Downloads/chromedriver"
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("https://www.google.com.tr/")

        # Verifying the website is Google Tr
        language = driver.find_element_by_css_selector("html[lang='tr']").get_attribute("lang")
        self.assertEqual("tr", language, "Webpage is NOT Google TR")

        # Executing the search
        searchField = driver.find_element_by_name("q")
        searchField.send_keys("Hipo Labs")
        searchField.send_keys(Keys.RETURN)

        # Gathering search results to verify hipolabs.com is listed
        hMainPage = driver.find_element_by_xpath("//a[contains(@href,'hipolabs.com')]")
        hMainLink = hMainPage.get_attribute("href")
        self.assertEqual("https://hipolabs.com/", hMainLink ,"hipolabs.com is NOT listed")

        # Opening hipolabs.com
        hMainPage.click()

        # Opening TEAM page in hipolabs.com
        hTeamPage = driver.find_element_by_id("menuMaximizedButtonTeam")
        time.sleep(1)  # Time.sleep function is used to avoid StaleElementReferenceException
        hTeamPage.click()

        # Verifying "APPLY for INTERNSHIP" text is exist
        teamPage_html_source = driver.page_source
        assert "APPLY for INTERNSHIP" in teamPage_html_source, "APPLY for INTERNSHIP text is NOT exist"

        # Taking screenshot
        screenshot_path = '/Users/didem/Desktop/TestCase4Hipo/HipoDriverTest/Screenshots/teampage.png'
        driver.save_screenshot(screenshot_path)


if __name__ == "__main__":
    unittest.main()

