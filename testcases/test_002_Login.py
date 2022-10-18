import os
import pytest
from pageobjects.HomePage import HomePage
from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.coustomlogger import LogGen

class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self,setup):

        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) +"\\screenshots\\" + "lest_Login")
            assert False

        self.driver.close()























