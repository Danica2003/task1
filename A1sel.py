from selenium import webdriver
import Constants
import Locators

driver = webdriver.Chrome()
driver.get(f"{Constants.BASE}")
driver.maximize_window()

cookieB = driver.find_element_by_css_selector(Locators.pop_button_css_s)
cookieB.click()

doorButton = driver.find_element_by_css_selector(Locators.door_button_css_s)
doorButton.click()                      # hyperlink doesn't work 

button3Dtour = driver.find_element_by_css_selector(Locators.tour_button_css_s)
button3Dtour.click()

Explore3dbutton = driver.find_element_by_css_selector(Locators.explore_button_css_s)
Explore3dbutton.click()

spot_button = driver.find_element_by_css_selector(Locators.spot_button_css_s)
spot_button.click()