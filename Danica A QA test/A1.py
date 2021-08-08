from selenium import webdriver
import Constants
import Locators
import time


def SignIn(email,password):
    driver = webdriver.Chrome()
    driver.get(f"{Constants.BASE}")

    getStarted = driver.find_element_by_css_selector(Locators.get_start_button_css_s)
    getStarted.click()

    emailF = driver.find_element_by_css_selector(Locators.email_field_css_s)
    passwordF = driver.find_element_by_css_selector(Locators.pass_field_css_s)

    emailF.send_keys(email)
    passwordF.send_keys(password)

    singInB = driver.find_element_by_css_selector(Locators.singin_button_css_s)
    singInB.click()
    time.sleep(2)

SignIn("dantonijevic@mail.com","123123")