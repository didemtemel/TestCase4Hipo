import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):
    def test_firsttest(self):
        # Starting our WebDriver and navigating to Google
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

        # Verify hipolabs.com is listed
        hMainPage = driver.find_element_by_xpath("//a[contains(@href,'hipolabs.com')]")
        hMainLink = hMainPage.get_attribute("href")
        self.assertEqual("https://hipolabs.com/", hMainLink ,"hipolabs.com is NOT listed")

        # Opening hipolabs.com
        hMainPage.click()

        # Verifying hipolabs.com main page is opened (optional)
        hLogo = driver.find_element_by_id("hipoLogo").get_attribute("id")
        self.assertEqual("hipoLogo", hLogo, "Webpage is NOT hipolabs.com's main page")

        # Opening TEAM page in hipolabs.com
        hTeamPage = driver.find_element_by_id("menuMaximizedButtonTeam")
        time.sleep(1)  # Time.sleep function is used to avoid StaleElementReferenceException
        hTeamPage.click()

        # Verifying "APPLY FOR INTERNSHIP" text exist
        teamPage_html_source = driver.page_source
        assert "APPLY FOR INTERNSHIP" in teamPage_html_source, "APPLY FOR INTERNSHIP text does NOT exist"

        # Taking screenshot
        screenshot_path = '/Users/didem/Desktop/TestCase4Hipo/HipoDriverTest/Screenshots/teampage.png'
        driver.save_screenshot(screenshot_path)


if __name__ == "__main__":
    unittest.main()

