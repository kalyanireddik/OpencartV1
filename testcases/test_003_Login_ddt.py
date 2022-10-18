import os.path
import time

import pytest

from pageobjects.HomePage import HomePage
from pageobjects.AccountRegistrationPage import AccountRegistrationPage
from pageobjects.LoginPage import LoginPage
from pageobjects.MyAccountPage import MyaccountPage
from utilities import randomstring
from utilities.readProperties import ReadConfig
from utilities.coustomlogger import LogGen

class Teat_Login_DDT():
    baseURL=ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path=os.path.abspath(os.curdir)+"\\testdata\\opencart_LoginData.xlsx"



    def test_login_ddt(self,setup):
        self.logger.info("**** test_003_Login_Datadriven started ***")
        self.rows=XLUtils.getRowsCount(self.path,"Sheet1")
        lst_status=[]
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("lunching application")

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.email = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.email = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.Password)
            self.lp.clickLogin()
            time.sleep(5)
            self.targetpage=self.lp.isMyAccountPageExists()

            if self.exp == "Valid":
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp == "Invalid":
                if self.targetpage==True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
            self.driver.close()
            if "Fail" not in lst_status:
                assert True
            else:
                assert False
            self.logger.info("****** End Of test_003_login_Datadrvine *******")





















