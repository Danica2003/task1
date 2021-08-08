
from selenium import webdriver
import Constants
import requests


def isOnline(Url):
    response = requests.get(Url)
    if(response.status_code==200):
        return True
    else:
        return False

if(isOnline(Constants.BASE)==True):
    print('Website is online')
else:
    print('Website is not online')