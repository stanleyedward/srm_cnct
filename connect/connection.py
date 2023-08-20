from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import connect.details as dtl 
from connect.setup import Setup
import os
# import pandas as pd
# import numpy as np

class Connection(webdriver.Firefox):
    def __init__(self, driver_path = r'connect/geckodriver-v0.33.0-linux/geckodriver'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        # driver = webdriver.Firefox()
        super(Connection, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

        # with open('connect/test.csv', 'w') as file:
        #     pass

    # def check_setup(self):
    #     # data = pd.read_csv('connect/details.csv', header = None)
    #     checkup = Setup(driver = self)
    #     if type(dtl.USERNAME)==str: #checking if data is not present            
    #         print("details found")
    #     else:
    #         print("login details missing running setup() again")
    #         checkup.setting_up()   
    #         print("run the command again if setup is done")
            
    def open_and_input(self, username, password):
        checkup1 = Setup(driver = self)
        self.get("https://iach.srmist.edu.in/Connect/PortalMain")
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.ID,'LoginUserPassword_auth_username'))).send_keys(username)
        # username_element = self.find_element(By.CSS_SELECTOR,'input[id="LoginUserPassword_auth_username"]')
        # username_element.send_keys(username)
        # username_element.send_keys("asdasd")
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.ID,'LoginUserPassword_auth_password'))).send_keys(password)
        # password_element = self.find_element(By.ID, "LoginUserPassword_auth_password")
        # password_element.send_keys(password)
        # password_element.send_keys("asdasd")
        submit_btn = self.find_element(By.ID, "UserCheck_Login_Button")
        submit_btn.click()

        try:
            WebDriverWait(self,1).until(  
            EC.text_to_be_present_in_element(
                (By.ID, 'usercheck_title_div'), 
                'Network Access Granted'
                )
            )
            print('Network Access Granted')
        
        except:
            error_message_element = self.find_element(By.ID,"LoginUserPassword_error_message")
            error_message = error_message_element.get_attribute('innerHTML')
            print(f'An Error was found: {error_message}/missing credentials')
            if error_message == 'Bad credentials':
                ans = input("want to (re-)input your credentials? [y/n]: ")
                if ans == 'y':
                    checkup1.setting_up()
                    pass
                else:
                    print("exiting...")
                    pass
            else:
                print("exiting...")




# error_message_element = driver.find_element(By.ID,"LoginUserPassword_error_message").get_attribute('innerHTML')
#innerHTML = 'Bad credentials'

# logoff_element = driver.find_element(By.ID, 'UserCheck_Logoff_Button_span')

# access_granted = driver.find_element(By.ID, 'usercheck_title_div')
#innerHTML = 'Network Access Granted'

# bad_cred_element = driver.find_element(By.ID,"LoginUserPassword_error_message").get_attribute('innerHTML')

