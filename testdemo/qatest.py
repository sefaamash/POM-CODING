
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class QATest(unittest.TestCase):
    #class method is the same method as we learned in java difference is that it is the method which will run everytime when a class run
    @classmethod 
    def setupclass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager.install())
        cls.driver.get("https://www.ssuet.edu.pk/ug/#admission-query")
        cls.driver.maximize_window()
    def test_fields(self):
        driver=self.driver
        fields=Fields(driver)
        fields.FirstName("Aamash")
        fields.Lastname("Khan")
        fields.Message("queries")
        fields.Previousqual("INTER")
        fields.SSC("86")
        fields.HSC("75")
        fields.OP("----")
        fields.Prog("SE")
        fields.Email("aamashkhan4@gmail.com")
        fields.Phone("033433")
        fields.subm()
        time.sleep(3)
    @classmethod
    def closingclass(cls):
        cls.driver.close()
        cls.driver.quit()



class Fields:
    #THIS IS CONSTRUCTOR USED TO INTIALIZE THE FIELDS SO WE DONT HAVE TO INDIVITUALLY MAKE CHANGES FROM EVERYWHERE WE CAN JUST CHANGE FROM HERE AND IT WILL BE APPLICABLE EVERYWHERE
    def __init__(self,driver):
        self.driver=driver
        self.firstName="form-field-name"
        self.LastName="form-field-lastname"
        self.message="form-field-message"
        self.previousqual="form-field-field_65f4539"
        self.ssc="form-field-field_d5dc2f5"
        self.hsc="form-field-field_bfc4cb0"
        self.otherper="form-field-field_cba4a89"
        self.prog="form-field-field_d9a34ea"
        self.email="form-field-email"
        self.ph="form-field-field_dad46e3"
        self.submit="elementor-button elementor-size-md elementor-animation-grow"
    
    #Now functions for each field
    def FirstName(self,fname):
        self.driver.find_element(By.ID,self.firstName).send_keys(fname)
    def Lastname(self,lname):
        self.driver.find_element(By.ID,self.LastName).send_keys(lname)
    def Message(self,mess):
        self.driver.find_element(By.ID,self.message).send_keys(mess)
    def Previousqual(self,Pq):
        self.driver.find_element(By.ID,self.previousqual).send_keys(Pq)
    def SSC(self,sc):
        self.driver.find_element(By.ID,self.ssc).send_keys(sc)
    def HSC(self,hs):
        self.driver.find_element(By.ID,self.hsc).send_keys(hs)
    def OP(self,op):
        self.driver.find_element(By.ID,self.otherper).send_keys(op)
    def Prog(self,program):
        self.driver.find_element(By.ID,self.prog).send_keys(program)
    def Email(self,mail):
            self.driver.find_element(By.ID,self.email).send_keys(mail)
    def Phone(self,phon):
        self.driver.find_element(By.ID,self.ph).send_keys(phon)
    def subm(self):
        self.driver.find_element(By.CLASS,self.submit).click()#as we click on the submit button so click action is used