import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class BitBucketLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")

    def test_bitbucket_login(self):
        driver = self.driver
        driver.get('https://bitbucket.org')

        driver.maximize_window()
        LoginBtn = driver.find_element_by_xpath('// *[ @ id = "product"] / div[1] / header / div / nav / ul / li[5] / a')
        LoginBtn.click()
        LoginField = driver.find_element_by_xpath('//*[@id="js-email-field"]')
        LoginField.send_keys("testerwsb2017@o2.pl")
        PasswordField = driver.find_element_by_xpath('//*[@id="js-password-field"]')
        PasswordField.send_keys("1qaz2wsx")
        LoginBtn2 = driver.find_element_by_xpath('//*[@id="aid-login-form"]/div[2]/input')
        LoginBtn2.click()
        Wait = WebDriverWait(driver, 5)
        AssertTextAfterLogin = driver.title
        self.assertEqual(AssertTextAfterLogin, 'Overview — Bitbucket')

        def tearDown(self):
            self.driver.quit()






if __name__ == '__main__':
    unittest.main()
