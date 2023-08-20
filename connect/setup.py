import pandas as pd 
import numpy as np
from selenium.webdriver.remote.webdriver import WebDriver
class Setup:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def setting_up(self):
        username = input("input username: ")
        password = input("input password: ")

        details = np.column_stack([username,password])
        pd.DataFrame(details).to_csv("connect/details.csv", index = None, header= None)
        print("run the command again after setup is done")