from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name="email"
    txt_telphone_name="telphone"
    txt_password_name="password"
    chk_policy_name="agree"
    but_cont_xpath="//input[@value='Continue']"
    text_msg_conf_xpath="//h1[normalize-spece()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver =driver
    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setTelphone(self,tel):
        self.driver.find_element(By.NAME,self.txt_telphone_name).send_keys(tel)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setPrivetPolicy(self):
        self.driver.find_element(By.NAME,self.chk_policy_name).click()

    def ClickContinue(self):
        self.driver.find_element(By.XPATH,self.but_cont_xpath).click()

    def getconfirmationmsg(self):
        try:
           return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None