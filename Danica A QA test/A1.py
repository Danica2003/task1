from selenium import webdriver
import Constants
import Locatore


def SingIn(email,password):
    driver = webdriver.Chrome()
    driver.get(f"{Constants.BASE}")

    getStrted = driver.find_element_by_css_selector(Locatore.get_start_button_css_s)
    getStrted.click()

    emailF = driver.find_element_by_css_selector(Locatore.email_field_css_s)
    passwordF = driver.find_element_by_css_selector(Locatore.pass_field_css_s)

    emailF.send_keys(email)
    passwordF.send_keys(password)

    singInB = driver.find_element_by_css_selector(Locatore.singin_button_css_s)
    singInB.click()
