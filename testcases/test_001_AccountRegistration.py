import os

from pageobjects.HomePage import HomePage
from pageobjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomstring
from utilities.readProperties import ReadConfig
from utilities.coustomlogger import LogGen

class Test_001_AccountReg:

    baseURL=ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_account_reg(self,setup):
        self.logger.info("**** test_001_AccountRegistration started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("lunching application")

        self.hp=HomePage(self.driver)
        self.logger.info("clicking on Myaccount -----> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("providing custmoer details for registration")
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("Jhon")
        self.regpage.setLastName("Canedy")
        self.email=randomstring.random_string_generator()+"@gmail.com"
        self.regpage.setEmail("abc0951776091@gmail.com")
        self.regpage.setTelphone('65656565')
        self.regpage.setPassword("abcxyz")
        self.regpage.setPrivetPolicy()
        self.regpage.ClickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()

        if self.confmsg=="Your Account Has Been Created!":
           self.logger.info("account registration is passed")
           assert True
           self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots"+"test_account_reg.")
            self.logger.error("account registration is faild")
            self.driver.close()
            assert False
        self.logger.info("**** test_001_AccountRegistration finished *****")

