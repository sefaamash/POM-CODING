import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class QATest(unittest.TestCase):
    #class method is the same method as we learned in java difference is that it is the method which will run everytime when a class run
    @classmethod 
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager.install())
        cls.driver.get("https://login.registernow.io/UserRegistration/RegisterUser?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DSecureWeb%26redirect_uri%3Dhttps%253A%252F%252Fwww.registernow.com.au%252Fsecure%252FSecure.aspx%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520profile%2520username%26state%3DOpenIdConnect.AuthenticationProperties%253DM1hLj1p6UAMa_1_Z4eRN3pG-5XaEEg-xSy7qY-VfviDJ4ZpFnKexuDeF_lORbIiv5pTXoImLfK5ax54qULFIgMfhjcq7SM5IK2L8IhJ_JXiCfvQ7jYlAnNJy6o13khpwdFnfA_-PiJRDHayUR0rzs57HnaMCeRA-WDTA1KKWLUKJRmaQ5UZJI4uqFK7DYtFbuE2thcPCDOEt1UdxZTnov-1I7rjZKajX2uMhvOXtUGQr_o1wi16Cv6owNWcMY1m_cZ5_CyjxxuTPmj0kL9eXbSZH7J76v8cTAilN8vcf2FHOPGk9adOFtCL8BLfBxHWp6_7HnMO4Jysr7aJhAS9sjA%26response_mode%3Dform_post%26nonce%3D637805480342082041.MzdmZWMyNmQtZGEwNC00NjQ4LWFiMjktNzNjNjE2NDc4OWQ5NzU1Yzg2NDAtYWIzOS00YjIwLWI5MDgtMzhlZjY2YzkyMzc1%26StartPage%3DLogin.aspx%26NextPage%3DLoggedIn.aspx%26GuestTicket%26x-client-SKU%3DID_NET461%26x-client-ver%3D5.3.0.0&button=SignUp")
        cls.driver.maximize_window
    def test_fields(self):
        driver=self.driver
        fields=Fields(driver)
        fields.FirstName("Aamash")
        fields.Lastname("Khan")
        fields.usernam("khan4")
        fields.Email("aamashkhan4@gmail.com")
        fields.Emailcn("aamashkhan4@gmail.com")
        fields.passwo('12345678@A')
        fields.cnpasswo('12345678@A')
        fields.Phone("033433")
        fields.subm()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()



class Fields:
    #THIS IS CONSTRUCTOR USED TO INTIALIZE THE FIELDS SO WE DONT HAVE TO INDIVITUALLY MAKE CHANGES FROM EVERYWHERE WE CAN JUST CHANGE FROM HERE AND IT WILL BE APPLICABLE EVERYWHERE
    def __init__(self,driver):
        self.driver=driver
        self.firstName="inputFirstName"
        self.LastName="inputLastName"
        self.username="inputUsername"
        self.passw="inputPassword"
        self.cnpass="inputPasswordConfirm"
        self.email="inputEmail"
        self.cnemail='inputEmailConfirm'
        self.ph="inputMobile"
        self.submit="btnSignUp"
    
    #Now functions for each field
    def FirstName(self,fname):
        self.driver.find_element(By.ID,self.firstName).send_keys(fname)
    def Lastname(self,lname):
        self.driver.find_element(By.ID,self.LastName).send_keys(lname)
   
    def Email(self,mail):
            self.driver.find_element(By.ID,self.email).send_keys(mail)
    def Emailcn(self,cnmail):
            self.driver.find_element(By.ID,self.email).send_keys(cnmail)
    def usernam(self,user):
         self.driver.find_element(By.ID,self.username).send_keys(user)
    
    def passwo(self,pas):
         self.driver.find_element(By.ID,self.passw).send_keys(pas)
    def cnpasswo(self,cnpas):
        self.driver.find_element(By.ID,self.cnpass).send_keys(cnpas)
    def Phone(self,phon):
        self.driver.find_element(By.ID,self.ph).send_keys(phon)
    def subm(self):
        self.driver.find_element(By.CLASS,self.submit).click()#as we click on the submit button so click action is used
    
        